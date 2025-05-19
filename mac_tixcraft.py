#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import sys
import platform
import webbrowser
import time
import threading
import subprocess
import PySimpleGUI as sg
import requests
import datetime

def get_app_root():
    # 讀取檔案裡的參數值
    basis = ""
    if hasattr(sys, 'frozen'):
        basis = sys.executable
    else:
        basis = sys.argv[0]
    app_root = os.path.dirname(basis)
    return app_root

def load_json():
    app_root = get_app_root()
    
    # overwrite config path.
    config_filepath = os.path.join(app_root, 'settings.json')
    
    config_dict = None
    if os.path.isfile(config_filepath):
        with open(config_filepath) as json_data:
            config_dict = json.load(json_data)
    
    return config_dict

def send_line_notification(message, line_notify_token=None, line_message_api_enabled=False, line_message_api_token=None, line_message_api_user_id=None):
    """發送LINE通知"""
    success = False
    
    # 輸出調試信息
    print("開始發送LINE通知...")
    print(f"LINE Notify啟用: {bool(line_notify_token and len(line_notify_token) > 0)}")
    print(f"LINE Messaging API啟用: {line_message_api_enabled}")
    
    # 先嘗試LINE Notify
    if line_notify_token and len(line_notify_token) > 0:
        try:
            url = "https://notify-api.line.me/api/notify"
            headers = {
                "Authorization": "Bearer " + line_notify_token
            }
            payload = {'message': message}
            print(f"發送LINE Notify請求到 {url}")
            response = requests.post(url, headers=headers, data=payload)
            if response.status_code == 200:
                print("LINE Notify發送成功！")
                success = True
            else:
                print(f"LINE Notify發送失敗，狀態碼: {response.status_code}")
        except Exception as e:
            print(f"LINE Notify發送異常: {e}")
    
    # 如果LINE Notify沒有配置或發送失敗，嘗試LINE Messaging API
    if not success and line_message_api_enabled and line_message_api_token and line_message_api_user_id:
        # 驗證參數
        if len(line_message_api_token) < 10:
            print(f"LINE Messaging API令牌太短，長度: {len(line_message_api_token)}")
            return False
            
        if len(line_message_api_user_id) < 10:
            print(f"LINE Messaging API用戶ID太短，長度: {len(line_message_api_user_id)}")
            return False
        
        try:
            url = 'https://api.line.me/v2/bot/message/push'
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + line_message_api_token
            }
            data = {
                'to': line_message_api_user_id,
                'messages': [
                    {
                        'type': 'text',
                        'text': message
                    }
                ]
            }
            print(f"發送LINE Messaging API請求到 {url}")
            print(f"使用的消息: {message}")
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 200:
                print("LINE Messaging API發送成功！")
                success = True
            else:
                print(f"LINE Messaging API發送失敗，狀態碼: {response.status_code}，回應: {response.text}")
        except Exception as e:
            print(f"LINE Messaging API發送異常: {e}")
    
    return success

def create_alert_window(config_dict):
    """創建提醒窗口，用於設置檢測時間和間隔"""
    default_check_interval = 5  # 默認檢查間隔（秒）
    
    layout = [
        [sg.Text('Mac版 TixBot 輔助工具', font=('Helvetica', 16))],
        [sg.Text('此工具會在指定時間自動打開搶票頁面，並發送LINE通知')],
        [sg.Text('目標時間 (HH:MM:SS)'), sg.Input('10:00:00', key='-TARGET_TIME-', size=(10, 1))],
        [sg.Text('檢查間隔（秒）'), sg.Input(str(default_check_interval), key='-INTERVAL-', size=(5, 1))],
        [sg.Text('選擇網站:')],
        [sg.Radio('TixCraft', 'SITE', key='-TIXCRAFT-', default=True), 
         sg.Radio('KKTIX', 'SITE', key='-KKTIX-')],
        [sg.Text('自訂URL:'), sg.Input('', key='-CUSTOM_URL-', size=(30, 1))],
        [sg.Checkbox('開啟時發送LINE通知', key='-SEND_LINE-', default=True)],
        [sg.Button('立即打開搶票頁面'), sg.Button('設置並監控'), sg.Button('退出')]
    ]
    
    window = sg.Window('Mac版 TixBot 輔助工具', layout, finalize=True)
    
    monitoring_thread = None
    stop_event = threading.Event()
    
    while True:
        event, values = window.read(timeout=1000)
        
        if event == sg.WIN_CLOSED or event == '退出':
            if monitoring_thread and monitoring_thread.is_alive():
                stop_event.set()
                monitoring_thread.join(timeout=1)
            break
        
        elif event == '立即打開搶票頁面':
            url = get_url_from_values(values, config_dict)
            open_browser(url)
            if values['-SEND_LINE-']:
                send_line_notification_from_config("搶票頁面已經打開，請盡快操作！", config_dict)
                
        elif event == '設置並監控':
            if monitoring_thread and monitoring_thread.is_alive():
                stop_event.set()
                monitoring_thread.join(timeout=1)
                stop_event.clear()
                window['設置並監控'].update('設置並監控')
            else:
                try:
                    target_time = values['-TARGET_TIME-']
                    interval = int(values['-INTERVAL-'])
                    
                    monitoring_thread = threading.Thread(
                        target=monitor_time,
                        args=(target_time, interval, values, config_dict, stop_event)
                    )
                    monitoring_thread.daemon = True
                    monitoring_thread.start()
                    
                    window['設置並監控'].update('停止監控')
                    sg.popup(f'開始監控，目標時間: {target_time}', non_blocking=True)
                except Exception as e:
                    sg.popup_error(f'設置錯誤: {e}')
    
    window.close()

def get_url_from_values(values, config_dict):
    """根據設置獲取URL"""
    if values['-CUSTOM_URL-'].strip():
        return values['-CUSTOM_URL-'].strip()
    
    # 從配置中獲取首頁URL
    homepage = config_dict.get("homepage", "https://tixcraft.com")
    
    if values['-TIXCRAFT-']:
        if homepage == "https://tixcraft.com":
            return "https://tixcraft.com/user/changeLanguage/lang/zh_tw"
        return homepage
    elif values['-KKTIX-']:
        return "https://kktix.com/"
    
    return homepage

def send_line_notification_from_config(message, config_dict):
    """從配置中讀取LINE設置並發送通知"""
    # LINE Notify設置
    line_notify_enabled = config_dict.get("line_notify", {}).get("enable", False)
    line_notify_token = config_dict.get("line_notify", {}).get("token", "")
    
    # LINE Messaging API設置
    line_message_api_enabled = config_dict.get("line_message_api", {}).get("enable", False)
    line_message_api_token = config_dict.get("line_message_api", {}).get("channel_access_token", "")
    line_message_api_user_id = config_dict.get("line_message_api", {}).get("user_id", "")
    
    # 如果配置了自定義消息，則使用自定義消息
    custom_message = None
    if line_notify_enabled and "message" in config_dict.get("line_notify", {}):
        custom_message = config_dict["line_notify"]["message"]
    elif line_message_api_enabled and "message" in config_dict.get("line_message_api", {}):
        custom_message = config_dict["line_message_api"]["message"]
    
    if custom_message:
        message = custom_message
    
    # 發送LINE通知
    return send_line_notification(
        message,
        line_notify_token if line_notify_enabled else None,
        line_message_api_enabled,
        line_message_api_token,
        line_message_api_user_id
    )

def open_browser(url):
    """打開瀏覽器訪問指定URL"""
    print(f"打開URL: {url}")
    
    try:
        # 首選使用webbrowser模塊
        webbrowser.open(url)
        print("已使用webbrowser模塊打開瀏覽器")
        return True
    except Exception as e:
        print(f"使用webbrowser模塊失敗: {e}")
        
        # 如果失敗，在Mac上嘗試使用open命令
        if platform.system() == "Darwin":
            try:
                subprocess.run(['open', url], check=True)
                print("已使用open命令打開瀏覽器")
                return True
            except Exception as e2:
                print(f"使用open命令失敗: {e2}")
        
        # 如果兩種方法都失敗，嘗試使用Chrome瀏覽器
        try:
            chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
            subprocess.run([chrome_path, url], check=False)
            print("已使用Chrome直接打開瀏覽器")
            return True
        except Exception as e3:
            print(f"使用Chrome直接打開失敗: {e3}")
            
        return False

def monitor_time(target_time, interval, values, config_dict, stop_event):
    """監控時間並在指定時間打開瀏覽器"""
    try:
        # 解析目標時間
        hour, minute, second = map(int, target_time.split(':'))
        
        while not stop_event.is_set():
            current_time = datetime.datetime.now().time()
            target = datetime.time(hour, minute, second)
            
            # 計算時間差（秒）
            current_seconds = current_time.hour * 3600 + current_time.minute * 60 + current_time.second
            target_seconds = target.hour * 3600 + target.minute * 60 + target.second
            time_diff = target_seconds - current_seconds
            
            # 如果差距小於或等於0，表示已到達目標時間
            if time_diff <= 0:
                url = get_url_from_values(values, config_dict)
                open_browser(url)
                
                if values['-SEND_LINE-']:
                    send_line_notification_from_config("搶票時間到！系統已自動打開搶票頁面，請盡快操作！", config_dict)
                
                # 任務完成，結束監控
                break
            
            # 更新倒計時顯示
            if time_diff < 60:  # 如果少於60秒，每秒更新
                print(f"倒計時: {time_diff}秒")
            else:
                minutes, seconds = divmod(time_diff, 60)
                hours, minutes = divmod(minutes, 60)
                print(f"倒計時: {hours}小時 {minutes}分鐘 {seconds}秒")
            
            # 等待指定的間隔時間
            for _ in range(interval):
                if stop_event.is_set():
                    break
                time.sleep(1)
    
    except Exception as e:
        print(f"監控時間出錯: {e}")

def main():
    """主函數"""
    print("啟動Mac版TixBot輔助工具...")
    
    # 讀取配置
    config_dict = load_json()
    
    if config_dict is None:
        print("無法讀取設定，使用默認值...")
        config_dict = {
            "homepage": "https://tixcraft.com",
            "line_notify": {"enable": False, "token": ""},
            "line_message_api": {"enable": False, "channel_access_token": "", "user_id": ""}
        }
    
    # 創建GUI窗口
    create_alert_window(config_dict)

if __name__ == "__main__":
    main() 