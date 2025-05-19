#!/usr/bin/env python3
#encoding=utf-8
# 'seleniumwire' and 'selenium 4' raise error when running python 2.x
# PS: python 2.x will be removed in future.
try:
    # for Python2
    from Tkinter import *
    import ttk
    import tkMessageBox as messagebox
except ImportError:
    # for Python3
    from tkinter import *
    from tkinter import ttk
    from tkinter import messagebox
    import tkinter.messagebox
import os
import sys
import platform
import json
import webbrowser
import pyperclip
import datetime

CONST_APP_VERSION = u"MaxBot (2023.01.13)"

CONST_FROM_TOP_TO_BOTTOM = u"from top to bottom"
CONST_FROM_BOTTOM_TO_TOP = u"from bottom to top"
CONST_RANDOM = u"random"
CONST_SELECT_ORDER_DEFAULT = CONST_FROM_TOP_TO_BOTTOM
CONST_SELECT_OPTIONS_DEFAULT = (CONST_FROM_TOP_TO_BOTTOM, CONST_FROM_BOTTOM_TO_TOP, CONST_RANDOM)
CONST_SELECT_OPTIONS_ARRAY = [CONST_FROM_TOP_TO_BOTTOM, CONST_FROM_BOTTOM_TO_TOP, CONST_RANDOM]
CONST_ADBLOCK_PLUS_ADVANCED_FILTER_DEFAULT = '''tixcraft.com###topAlert
tixcraft.com##.col-md-7.col-xs-12.mg-top
tixcraft.com##.topBar.alert-box.emergency
tixcraft.com##.footer.clearfix
tixcraft.com##.row.process-wizard.process-wizard-info
tixcraft.com##.nav-line
tixcraft.com##.page-info.row.line-btm.mg-0'''
CONST_CAPTCHA_SOUND_FILENAME_DEFAULT = "ding-dong.wav"
CONST_HOMEPAGE_DEFAULT = "https://tixcraft.com"

# 全局变量
UI_PADDING_X = 15

translate={}

URL_DONATE = 'https://max-everyday.com/about/#donate'
URL_HELP = 'https://max-everyday.com/2018/03/tixcraft_bot/'
URL_RELEASE = 'https://github.com/max32002/tixcraft_bot/releases'
URL_FB = 'https://www.facebook.com/maxbot.ticket'

def load_translate():
    translate = {}
    en_us={}
    en_us["homepage"] = 'Homepage'
    en_us["browser"] = 'Browser'
    en_us["language"] = 'Language'
    en_us["ticket_number"] = 'Ticker Number'

    en_us["auto_check_agree"] = 'Auto check agree checkbox'
    en_us["enable"] = 'Enable'

    en_us["auto_press_next_step_button"] = 'Auto Press Next Step Button'
    en_us["auto_fill_ticket_number"] = 'Auto Fill Ticket Number'
    en_us["area_select_order"] = 'Area select order'
    en_us["area_keyword"] = 'Area Keyword'
    en_us["and"] = 'And with'
    en_us["auto_guess_options"] = 'Guess Options in Question'
    en_us["user_guess_string"] = 'Fill This Answer in Question'

    en_us["date_auto_select"] = 'Date Auto Select'
    en_us["date_select_order"] = 'Date select order'
    en_us["date_keyword"] = 'Date Keyword'
    en_us["pass_date_is_sold_out"] = 'Pass date is sold out'
    en_us["auto_reload_coming_soon_page"] = 'Reload coming soon page'
    
    en_us["area_auto_select"] = 'Area Auto Select'
    #en_us["area_select_order"] = 'Area select order'
    en_us["area_keyword_1"] = 'Area Keyword #1'
    en_us["area_keyword_2"] = 'Area Keyword #2'
    en_us["area_keyword_3"] = 'Area Keyword #3'
    en_us["area_keyword_4"] = 'Area Keyword #4'
    en_us["pass_1_seat_remaining"] = 'Pass 1 seat remaining'
    en_us["ocr_captcha"] = 'OCR captcha'
    en_us["ocr_captcha_with_submit"] = 'After guess auto submit'
    en_us["ocr_captcha_force_submit"] = 'Allow submit wrong answer'

    en_us["preference"] = 'Preference'
    en_us["advanced"] = 'Advanced'
    en_us["about"] = 'About'

    en_us["run"] = 'Run'
    en_us["save"] = 'Save'
    en_us["exit"] = 'Close'
    en_us["copy"] = 'Copy'
    en_us["restore_defaults"] = 'Restore Defaults'
    en_us["done"] = 'Done'

    en_us["facebook_account"] = 'Facebook account'
    en_us["kktix_account"] = 'KKTIX account'
    en_us["play_captcha_sound"] = 'Play sound when captcha'
    en_us["captcha_sound_filename"] = 'captcha sound filename'
    en_us["adblock_plus_enable"] = 'Adblock Plus Extension'
    en_us["adblock_plus_memo"] = 'Default adblock is disable'
    en_us["adblock_plus_settings"] = "Adblock Advanced Filter"
    
    # 添加保存登入狀態的翻譯 - 英文
    en_us["save_login_status"] = 'Save browser login status'
    en_us["save_login_status_memo"] = 'Keep Google and other websites logged in'

    en_us["line_notify_enable"] = 'LINE Notify'
    en_us["line_notify_token"] = 'LINE Notify Access Token'
    en_us["line_notify_message"] = 'Notification Message'

    en_us["line_message_api_enable"] = 'LINE Messaging API (Recommend)'
    en_us["line_message_api_channel_access_token"] = 'Channel Access Token'
    en_us["line_message_api_user_id"] = 'User ID / Group ID'
    en_us["line_message_api_message"] = 'Notification Message'

    en_us["maxbot_slogan"] = 'MaxBot is a FREE and open source bot program. Wish you good luck.'
    en_us["donate"] = 'Donate'
    en_us["help"] = 'Help'
    en_us["release"] = 'Release'
    en_us["test_send"] = 'Test Send'

    zh_tw={}
    zh_tw["homepage"] = '售票網站'
    zh_tw["browser"] = '瀏覽器'
    zh_tw["language"] = '語言'
    zh_tw["ticket_number"] = '門票張數'

    zh_tw["auto_check_agree"] = '自動勾選同意'

    zh_tw["enable"] = '啟用'
    zh_tw["auto_press_next_step_button"] = '自動點選下一步按鈕'
    zh_tw["auto_fill_ticket_number"] = '自動輸入張數'
    zh_tw["area_select_order"] = '區域排序方式'
    zh_tw["area_keyword"] = '區域關鍵字'
    zh_tw["and"] = '而且（同列）'
    zh_tw["auto_guess_options"] = '自動猜測驗證問題'
    zh_tw["user_guess_string"] = '在驗證問題中填寫此答案'

    zh_tw["date_auto_select"] = '日期自動點選'
    zh_tw["date_select_order"] = '日期排序方式'
    zh_tw["date_keyword"] = '日期關鍵字'
    zh_tw["pass_date_is_sold_out"] = '避開「搶購一空」的日期'
    zh_tw["auto_reload_coming_soon_page"] = '自動刷新倒數中的日期頁面'

    zh_tw["area_auto_select"] = '區域自動點選'
    #zh_tw["area_select_order"] = '區域排序方式'
    zh_tw["area_keyword_1"] = '區域關鍵字 #1'
    zh_tw["area_keyword_2"] = '區域關鍵字 #2'
    zh_tw["area_keyword_3"] = '區域關鍵字 #3'
    zh_tw["area_keyword_4"] = '區域關鍵字 #4'
    zh_tw["pass_1_seat_remaining"] = '避開「剩餘 1」的區域'
    zh_tw["ocr_captcha"] = '猜測驗證碼'
    zh_tw["ocr_captcha_with_submit"] = '猜測後自動送出'
    zh_tw["ocr_captcha_force_submit"] = '允許送出錯的驗證碼'

    zh_tw["preference"] = '偏好設定'
    zh_tw["advanced"] = '進階設定'
    zh_tw["about"] = '關於'

    zh_tw["run"] = '啟動搶票'
    zh_tw["save"] = '存檔'
    zh_tw["exit"] = '離開'
    zh_tw["copy"] = '複製'
    zh_tw["restore_defaults"] = '恢復預設值'
    zh_tw["done"] = '完成'
    zh_tw["test_send"] = '測試發送'

    zh_tw["facebook_account"] = 'Facebook 帳號'
    zh_tw["kktix_account"] = 'KKTIX 帳號'
    zh_tw["play_captcha_sound"] = '輸入驗證碼時播放音效'
    zh_tw["captcha_sound_filename"] = '驗證碼用音效檔'
    zh_tw["adblock_plus_enable"] = 'Adblock 瀏覽器擴充功能'
    zh_tw["adblock_plus_memo"] = 'Adblock 功能預設關閉'
    zh_tw["adblock_plus_settings"] = "Adblock 進階過濾規則"
    
    # 添加保存登入狀態的翻譯 - 繁體中文
    zh_tw["save_login_status"] = '保存瀏覽器登入狀態'
    zh_tw["save_login_status_memo"] = '保持Google等網站的登入狀態'

    zh_tw["line_notify_enable"] = 'LINE Notify 通知'
    zh_tw["line_notify_token"] = 'LINE Notify 訪問令牌'
    zh_tw["line_notify_message"] = '通知訊息'

    zh_tw["line_message_api_enable"] = 'LINE Messaging API (推薦)'
    zh_tw["line_message_api_channel_access_token"] = 'Channel Access Token'
    zh_tw["line_message_api_user_id"] = '使用者ID / 群組ID'
    zh_tw["line_message_api_message"] = '通知訊息'

    zh_tw["maxbot_slogan"] = 'MaxBot 是一個免費的開源機器人程序。\n祝您搶票成功。'
    zh_tw["donate"] = '打賞'
    zh_tw["help"] = '使用教學'
    zh_tw["release"] = '所有可用版本'

    zh_cn={}
    zh_cn["homepage"] = '售票网站'
    zh_cn["browser"] = '浏览器'
    zh_cn["language"] = '语言'
    zh_cn["ticket_number"] = '门票张数'

    zh_cn["auto_check_agree"] = '自动勾选同意'
    zh_cn["enable"] = '启用'

    zh_cn["auto_press_next_step_button"] = '自动点选下一步按钮'
    zh_cn["auto_fill_ticket_number"] = '自动输入张数'
    zh_cn["area_select_order"] = '区域排序方式'
    zh_cn["area_keyword"] = '区域关键字'
    zh_cn["and"] = '而且（同列）'
    zh_cn["auto_guess_options"] = '自动猜测验证问题'
    zh_cn["user_guess_string"] = '在验证问题中填写此答案'

    zh_cn["date_auto_select"] = '日期自动点选'
    zh_cn["date_select_order"] = '日期排序方式'
    zh_cn["date_keyword"] = '日期关键字'
    zh_cn["pass_date_is_sold_out"] = '避开"抢购一空"的日期'
    zh_cn["auto_reload_coming_soon_page"] = '自动刷新倒数中的日期页面'

    zh_cn["area_auto_select"] = '区域自动点选'
    #zh_cn["area_select_order"] = '区域排序方式'
    zh_cn["area_keyword_1"] = '区域关键字 #1'
    zh_cn["area_keyword_2"] = '区域关键字 #2'
    zh_cn["area_keyword_3"] = '区域关键字 #3'
    zh_cn["area_keyword_4"] = '区域关键字 #4'
    zh_cn["pass_1_seat_remaining"] = '避开"剩余 1"的区域'
    zh_cn["ocr_captcha"] = '猜测验证码'
    zh_cn["ocr_captcha_with_submit"] = '猜测后自动送出'
    zh_cn["ocr_captcha_force_submit"] = '允许送出错的验证码'

    zh_cn["preference"] = '偏好设定'
    zh_cn["advanced"] = '進階設定'
    zh_cn["about"] = '关于'
    zh_cn["copy"] = '复制'

    zh_cn["run"] = '启动抢票'
    zh_cn["save"] = '存盘'
    zh_cn["exit"] = '离开'
    zh_cn["copy"] = '复制'
    zh_cn["restore_defaults"] = '恢复默认值'
    zh_cn["done"] = '完成'
    zh_cn["test_send"] = '测试发送'

    zh_cn["facebook_account"] = 'Facebook 帐号'
    zh_cn["kktix_account"] = 'KKTIX 帐号'
    zh_cn["play_captcha_sound"] = '输入验证码时播放音效'
    zh_cn["captcha_sound_filename"] = '验证码用音效档'
    zh_cn["adblock_plus_enable"] = 'Adblock 浏览器扩充功能'
    zh_cn["adblock_plus_memo"] = 'Adblock 功能预设关闭'
    zh_cn["adblock_plus_settings"] = "Adblock 进阶过滤规则"
    
    # 添加保存登入狀態的翻譯 - 簡體中文
    zh_cn["save_login_status"] = '保存浏览器登录状态'
    zh_cn["save_login_status_memo"] = '保持Google等网站的登录状态'

    zh_cn["line_notify_enable"] = 'LINE Notify 通知'
    zh_cn["line_notify_token"] = 'LINE Notify 访问令牌'
    zh_cn["line_notify_message"] = '通知消息'

    zh_cn["line_message_api_enable"] = 'LINE Messaging API (推荐)'
    zh_cn["line_message_api_channel_access_token"] = 'Channel Access Token'
    zh_cn["line_message_api_user_id"] = '用户ID / 群组ID'
    zh_cn["line_message_api_message"] = '通知消息'

    zh_cn["maxbot_slogan"] = 'MaxBot 是一个免费的开源机器人程序。\n祝您抢票成功。'
    zh_cn["donate"] = '打赏'
    zh_cn["help"] = '使用教学'
    zh_cn["release"] = '所有可用版本'

    ja_jp={}
    ja_jp["homepage"] = 'ホームページ'
    ja_jp["browser"] = 'ブラウザ'
    ja_jp["language"] = '言語'
    ja_jp["ticket_number"] = '枚数'

    ja_jp["auto_check_agree"] = '自動的に同意をチェック'
    ja_jp["enable"] = '有効'

    ja_jp["auto_press_next_step_button"] = '次を自動で押す'
    ja_jp["auto_fill_ticket_number"] = '枚数自動入力'
    ja_jp["area_select_order"] = 'エリアソート方法'
    ja_jp["area_keyword"] = 'エリアキーワード'
    ja_jp["and"] = 'そして（同列）'
    ja_jp["auto_guess_options"] = '自動推測検証問題'
    ja_jp["user_guess_string"] = '質問に回答を記入'

    ja_jp["date_auto_select"] = '日付自動選択'
    ja_jp["date_select_order"] = '日付のソート方法'
    ja_jp["date_keyword"] = '日付キーワード'
    ja_jp["pass_date_is_sold_out"] = '「売り切れ」公演を避ける'
    ja_jp["auto_reload_coming_soon_page"] = '公開予定のページをリロード'

    ja_jp["area_auto_select"] = 'エリア自動選択'
    #ja_jp["area_select_order"] = 'エリアソート方法'
    ja_jp["area_keyword_1"] = 'エリアキーワード #1'
    ja_jp["area_keyword_2"] = 'エリアキーワード #2'
    ja_jp["area_keyword_3"] = 'エリアキーワード #3'
    ja_jp["area_keyword_4"] = 'エリアキーワード #4'
    ja_jp["pass_1_seat_remaining"] = '「1 席残り」エリアは避ける'
    ja_jp["ocr_captcha"] = 'キャプチャを推測する'
    ja_jp["ocr_captcha_with_submit"] = '提出で推測した後'
    zh_cn["ocr_captcha_force_submit"] = '間違った回答の送信を許可する'

    ja_jp["preference"] = '設定'
    ja_jp["advanced"] = '高度な設定'
    ja_jp["about"] = '情報'

    ja_jp["run"] = '実行'
    ja_jp["save"] = '保存'
    ja_jp["exit"] = '閉じる'
    ja_jp["copy"] = 'コピー'
    ja_jp["restore_defaults"] = 'デフォルトに戻す'
    ja_jp["done"] = '終わり'
    ja_jp["test_send"] = 'テスト送信'

    ja_jp["facebook_account"] = 'Facebookのアカウント'
    ja_jp["kktix_account"] = 'KKTIXのアカウント'
    ja_jp["play_captcha_sound"] = 'キャプチャ時に音を鳴らす'
    ja_jp["captcha_sound_filename"] = 'サウンドファイル名'

    ja_jp["adblock_plus_enable"] = 'Adblock 拡張機能'
    ja_jp["adblock_plus_memo"] = 'Adblock デフォルトは無効です'
    ja_jp["adblock_plus_settings"] = "Adblock 高度なフィルター"
    ja_jp["maxbot_slogan"] = 'MaxBot は無料のオープン ソース ボット プログラムです。チケットの成功をお祈りします。'
    ja_jp["donate"] = '寄付'
    ja_jp["help"] = '利用方法'
    ja_jp["release"] = 'リリース'

    ja_jp["line_notify_enable"] = 'LINE Notify 通知'
    ja_jp["line_notify_token"] = 'LINE Notify アクセストークン'
    ja_jp["line_notify_message"] = '通知メッセージ'

    ja_jp["line_message_api_enable"] = 'LINE Messaging API (おすすめ)'
    ja_jp["line_message_api_channel_access_token"] = 'Channel Access Token'
    ja_jp["line_message_api_user_id"] = 'ユーザーID / グループID'
    ja_jp["line_message_api_message"] = '通知メッセージ'
    
    translate['en_us']=en_us
    translate['zh_tw']=zh_tw
    translate['zh_cn']=zh_cn
    translate['ja_jp']=ja_jp
    return translate

def get_app_root():
    # 讀取檔案裡的參數值
    basis = ""
    if hasattr(sys, 'frozen'):
        basis = sys.executable
    else:
        basis = sys.argv[0]
    app_root = os.path.dirname(basis)
    return app_root

def get_default_config():
    config_dict={}

    config_dict["homepage"] = CONST_HOMEPAGE_DEFAULT
    config_dict["browser"] = "chrome"
    config_dict["language"] = "English"
    config_dict["ticket_number"] = 2
    config_dict["pass_1_seat_remaining"] = True
    config_dict["auto_check_agree"] = True
    config_dict["ocr_captcha"] = {}
    config_dict["ocr_captcha"]["enable"] = True
    config_dict["ocr_captcha"]["auto_submit"] = False
    config_dict["ocr_captcha"]["force_submit"] = False

    config_dict['kktix']={}
    config_dict["kktix"]["auto_press_next_step_button"] = True
    config_dict["kktix"]["auto_fill_ticket_number"] = True
    config_dict["kktix"]["area_mode"] = CONST_SELECT_ORDER_DEFAULT
    config_dict["kktix"]["area_keyword_1"] = ""
    config_dict["kktix"]["area_keyword_1_and"] = ""
    config_dict["kktix"]["area_keyword_2"] = ""
    config_dict["kktix"]["area_keyword_2_and"] = ""
    config_dict["kktix"]["auto_guess_options"] = False
    config_dict["kktix"]["user_guess_string"] = ""

    config_dict['tixcraft']={}
    config_dict["tixcraft"]["date_auto_select"] = {}
    config_dict["tixcraft"]["date_auto_select"]["enable"] = True
    config_dict["tixcraft"]["date_auto_select"]["date_keyword"] = ""
    config_dict["tixcraft"]["area_auto_select"] = {}
    config_dict["tixcraft"]["area_auto_select"]["enable"] = True
    config_dict["tixcraft"]["area_auto_select"]["area_keyword_1"] = ""
    config_dict["tixcraft"]["area_auto_select"]["area_keyword_2"] = ""
    config_dict["tixcraft"]["area_auto_select"]["area_keyword_3"] = ""
    config_dict["tixcraft"]["area_auto_select"]["area_keyword_4"] = ""

    config_dict["tixcraft"]["date_auto_select"]["mode"] = CONST_SELECT_ORDER_DEFAULT
    config_dict["tixcraft"]["area_auto_select"]["mode"] = CONST_SELECT_ORDER_DEFAULT

    config_dict["tixcraft"]["pass_date_is_sold_out"] = True
    config_dict["tixcraft"]["auto_reload_coming_soon_page"] = True
    config_dict["tixcraft"]["presale_code"] = ""

    config_dict['advanced']={}

    config_dict['advanced']['play_captcha_sound']={}
    config_dict["advanced"]["play_captcha_sound"]["enable"] = True
    config_dict["advanced"]["play_captcha_sound"]["filename"] = CONST_CAPTCHA_SOUND_FILENAME_DEFAULT

    config_dict["advanced"]["facebook_account"] = ""
    config_dict["advanced"]["kktix_account"] = ""
    config_dict["advanced"]["adblock_plus_enable"] = False
    
    # 添加保存登入狀態選項
    config_dict["advanced"]["save_login_status"] = True

    # LINE Notify配置（将于2025年3月31日停止服务）
    config_dict['line_notify']={}
    config_dict["line_notify"]["enable"] = False
    config_dict["line_notify"]["token"] = ""
    config_dict["line_notify"]["message"] = "成功进入支付页面！请尽快完成付款。"

    # LINE Messaging API配置（LINE Notify的替代方案）
    config_dict['line_message_api']={}
    config_dict["line_message_api"]["enable"] = False
    config_dict["line_message_api"]["channel_access_token"] = ""
    config_dict["line_message_api"]["user_id"] = ""
    config_dict["line_message_api"]["message"] = "成功进入支付页面！请尽快完成付款。"

    config_dict['debug']=False

    return config_dict

def load_json():
    app_root = get_app_root()

    # overwrite config path.
    config_filepath = os.path.join(app_root, 'settings.json')

    config_dict = None
    if os.path.isfile(config_filepath):
        with open(config_filepath) as json_data:
            config_dict = json.load(json_data)
    else:
        config_dict = get_default_config()
    return config_filepath, config_dict

def btn_restore_defaults_clicked(language_code):
    app_root = get_app_root()
    config_filepath = os.path.join(app_root, 'settings.json')

    config_dict = get_default_config()
    import json
    with open(config_filepath, 'w') as outfile:
        json.dump(config_dict, outfile)
    messagebox.showinfo(translate[language_code]["restore_defaults"], translate[language_code]["done"])

    global root
    load_GUI(root, config_dict)

def btn_save_clicked(language_code):
    btn_save_act(language_code)

def btn_save_act(language_code, slience_mode=False):
    app_root = get_app_root()
    config_filepath = os.path.join(app_root, 'settings.json')

    config_dict = get_default_config()

    # read user input
    global combo_homepage
    global combo_browser
    global combo_language
    global combo_ticket_number
    global chk_state_pass_1_seat_remaining
    global chk_state_auto_check_agree

    global chk_state_auto_press_next_step_button
    global chk_state_auto_fill_ticket_number
    global txt_kktix_area_keyword_1
    global txt_kktix_area_keyword_1_and
    global txt_kktix_area_keyword_2
    global txt_kktix_area_keyword_2_and
    # disable password brute force attack
    global txt_kktix_answer_dictionary
    global txt_kktix_user_guess_string

    global chk_state_auto_guess_options

    global chk_state_date_auto_select
    global txt_date_keyword
    global chk_state_area_auto_select
    global txt_area_keyword_1
    global txt_area_keyword_2
    global txt_area_keyword_3
    global txt_area_keyword_4

    global combo_date_auto_select_mode
    global combo_area_auto_select_mode

    global chk_state_pass_date_is_sold_out
    global chk_state_auto_reload_coming_soon_page
    global txt_presale_code

    global txt_facebook_account
    global txt_kktix_account
    global chk_state_play_captcha_sound
    global txt_captcha_sound_filename
    global chk_state_adblock_plus
    global chk_state_ocr_captcha
    global chk_state_ocr_captcha_with_submit
    global chk_state_ocr_captcha_force_submit

    is_all_data_correct = True

    if is_all_data_correct:
        if combo_homepage.get().strip()=="":
            is_all_data_correct = False
            messagebox.showerror("Error", "Please enter homepage")
        else:
            config_dict["homepage"] = combo_homepage.get().strip()

    if is_all_data_correct:
        if combo_browser.get().strip()=="":
            is_all_data_correct = False
            messagebox.showerror("Error", "Please select a browser: chrome or firefox")
        else:
            config_dict["browser"] = combo_browser.get().strip()

    if is_all_data_correct:
        if combo_language.get().strip()=="":
            is_all_data_correct = False
            messagebox.showerror("Error", "Please select a language")
        else:
            config_dict["language"] = combo_language.get().strip()
            # display as new language.
            language_code = get_language_code_by_name(config_dict["language"])

    if is_all_data_correct:
        if combo_ticket_number.get().strip()=="":
            is_all_data_correct = False
            messagebox.showerror("Error", "Please select a value")
        else:
            config_dict["ticket_number"] = int(combo_ticket_number.get().strip())

    if is_all_data_correct:
        config_dict["pass_1_seat_remaining"] = bool(chk_state_pass_1_seat_remaining.get())
        config_dict["auto_check_agree"] = bool(chk_state_auto_check_agree.get())

        config_dict["kktix"]["auto_press_next_step_button"] = bool(chk_state_auto_press_next_step_button.get())
        config_dict["kktix"]["auto_fill_ticket_number"] = bool(chk_state_auto_fill_ticket_number.get())
        config_dict["kktix"]["area_mode"] = combo_kktix_area_mode.get().strip()
        config_dict["kktix"]["area_keyword_1"] = txt_kktix_area_keyword_1.get().strip()
        config_dict["kktix"]["area_keyword_1_and"] = txt_kktix_area_keyword_1_and.get().strip()
        config_dict["kktix"]["area_keyword_2"] = txt_kktix_area_keyword_2.get().strip()
        config_dict["kktix"]["area_keyword_2_and"] = txt_kktix_area_keyword_2_and.get().strip()
        # disable password brute force attack
        #config_dict["kktix"]["answer_dictionary"] = txt_kktix_answer_dictionary.get().strip()
        config_dict["kktix"]["auto_guess_options"] = bool(chk_state_auto_guess_options.get())
        config_dict["kktix"]["user_guess_string"] = txt_kktix_user_guess_string.get().strip()

        config_dict["tixcraft"]["date_auto_select"]["enable"] = bool(chk_state_date_auto_select.get())
        config_dict["tixcraft"]["date_auto_select"]["date_keyword"] = txt_date_keyword.get().strip()

        config_dict["tixcraft"]["area_auto_select"]["enable"] = bool(chk_state_area_auto_select.get())
        config_dict["tixcraft"]["area_auto_select"]["area_keyword_1"] = txt_area_keyword_1.get().strip()
        config_dict["tixcraft"]["area_auto_select"]["area_keyword_2"] = txt_area_keyword_2.get().strip()
        config_dict["tixcraft"]["area_auto_select"]["area_keyword_3"] = txt_area_keyword_3.get().strip()
        config_dict["tixcraft"]["area_auto_select"]["area_keyword_4"] = txt_area_keyword_4.get().strip()

        config_dict["tixcraft"]["date_auto_select"]["mode"] = combo_date_auto_select_mode.get().strip()
        config_dict["tixcraft"]["area_auto_select"]["mode"] = combo_area_auto_select_mode.get().strip()

        config_dict["tixcraft"]["pass_date_is_sold_out"] = bool(chk_state_pass_date_is_sold_out.get())
        config_dict["tixcraft"]["auto_reload_coming_soon_page"] = bool(chk_state_auto_reload_coming_soon_page.get())
        config_dict["tixcraft"]["presale_code"] = txt_presale_code.get().strip()

        config_dict["advanced"]["play_captcha_sound"]["enable"] = bool(chk_state_play_captcha_sound.get())
        config_dict["advanced"]["play_captcha_sound"]["filename"] = txt_captcha_sound_filename.get().strip()

        config_dict["advanced"]["facebook_account"] = txt_facebook_account.get().strip()
        config_dict["advanced"]["kktix_account"] = txt_kktix_account.get().strip()
        config_dict["advanced"]["adblock_plus_enable"] = bool(chk_state_adblock_plus.get())
        
        # 保存登入狀態設定
        global chk_state_save_login_status
        config_dict["advanced"]["save_login_status"] = bool(chk_state_save_login_status.get())
        
        config_dict["ocr_captcha"] = {}
        config_dict["ocr_captcha"]["enable"] = bool(chk_state_ocr_captcha.get())
        config_dict["ocr_captcha"]["auto_submit"] = bool(chk_state_ocr_captcha_with_submit.get())
        config_dict["ocr_captcha"]["force_submit"] = bool(chk_state_ocr_captcha_force_submit.get())

        # 保存LINE Notify设置
        global chk_state_line_notify
        global txt_line_notify_token
        global txt_line_notify_message
        
        config_dict["line_notify"] = {}
        config_dict["line_notify"]["enable"] = bool(chk_state_line_notify.get())
        config_dict["line_notify"]["token"] = txt_line_notify_token.get().strip()
        config_dict["line_notify"]["message"] = txt_line_notify_message.get().strip()
        
        # 保存LINE Messaging API設定
        global chk_state_line_message_api
        global txt_line_message_api_token
        global txt_line_message_api_user_id
        global txt_line_message_api_message
        
        config_dict["line_message_api"] = {}
        config_dict["line_message_api"]["enable"] = bool(chk_state_line_message_api.get())
        
        # 验证并保存Channel Access Token
        channel_access_token = txt_line_message_api_token.get().strip()

            
        config_dict["line_message_api"]["channel_access_token"] = channel_access_token
        
        # 验证并保存User ID
        user_id = txt_line_message_api_user_id.get().strip()
        if bool(chk_state_line_message_api.get()) and len(user_id) < 10:
            # 如果启用了LINE Messaging API但User ID格式不正确，显示警告并禁用功能
            messagebox.showwarning(translate[language_code]["save"], "LINE Messaging API User ID格式不正确，将禁用此功能")
            config_dict["line_message_api"]["enable"] = False
            chk_state_line_message_api.set(False)
            
        config_dict["line_message_api"]["user_id"] = user_id
        config_dict["line_message_api"]["message"] = txt_line_message_api_message.get().strip()

    # save config.
    if is_all_data_correct:
        import json
        with open(config_filepath, 'w') as outfile:
            json.dump(config_dict, outfile)

        if not slience_mode:
            messagebox.showinfo(translate[language_code]["save"], translate[language_code]["done"])

    return is_all_data_correct

def btn_run_clicked(language_code):
    import subprocess

    print('run button pressed.')
    Root_Dir = ""
    save_ret = btn_save_act(language_code, slience_mode=True)
    print("save config result:", save_ret)
    if save_ret:
        if hasattr(sys, 'frozen'):
            print("execute in frozen mode")

            # check platform here.
            if platform.system() == 'Darwin':
                print("execute MacOS python script")
                subprocess.Popen("./chrome_tixcraft", shell=True)
            if platform.system() == 'Linux':
                print("execute linux binary")
                subprocess.Popen("./chrome_tixcraft", shell=True)
            if platform.system() == 'Windows':
                print("execute .exe binary.")
                subprocess.Popen("chrome_tixcraft.exe", shell=True)
        else:
            interpreter_binary = 'python'
            interpreter_binary_alt = 'python3'
            if platform.system() == 'Darwin':
                # try python3 before python.
                interpreter_binary = 'python3'
                interpreter_binary_alt = 'python'
            print("execute in shell mode.")
            working_dir = os.path.dirname(os.path.realpath(__file__))
            #print("script path:", working_dir)
            #messagebox.showinfo(title="Debug0", message=working_dir)

            # some python3 binary, running in 'python' command.
            try:
                print('try', interpreter_binary)
                s=subprocess.Popen([interpreter_binary, 'chrome_tixcraft.py'], cwd=working_dir)
                #s=subprocess.Popen(['./chrome_tixcraft'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=working_dir)
                #s=subprocess.run(['python3', 'chrome_tixcraft.py'], cwd=working_dir)
                #messagebox.showinfo(title="Debug1", message=str(s))
            except Exception as exc:
                print('try', interpreter_binary_alt)
                try:
                    s=subprocess.Popen([interpreter_binary_alt, 'chrome_tixcraft.py'], cwd=working_dir)
                except Exception as exc:
                    msg=str(exc)
                    print("exeption:", msg)
                    #messagebox.showinfo(title="Debug2", message=msg)
                    pass

def btn_preview_sound_clicked():
    global txt_captcha_sound_filename
    new_sound_filename = txt_captcha_sound_filename.get().strip()
    #print("new_sound_filename:", new_sound_filename)
    app_root = get_app_root()
    new_sound_filename = os.path.join(app_root, new_sound_filename)
    play_mp3_async(new_sound_filename)

def btn_test_line_messaging_api_clicked(language_code):
    # 导入tkinter.messagebox
    from tkinter import messagebox
    # 导入mac_tixcraft中的函数
    from mac_tixcraft import send_line_notification
    
    # 获取Channel Access Token和User ID
    line_message_api_token = txt_line_message_api_token.get().strip()
    line_message_api_user_id = txt_line_message_api_user_id.get().strip()
    
    # 创建错误和成功消息的多语言版本
    error_token_too_short = {
        'zh_tw': "Channel Access Token 長度不足，請確保已正確填寫",
        'zh_cn': "Channel Access Token 长度不足，请确保已正确填写",
        'en_us': "Channel Access Token length is too short, please make sure it's correctly filled in",
        'ja_jp': "Channel Access Tokenの長さが足りません、正しく入力されていることを確認してください"
    }
    
    error_userid_too_short = {
        'zh_tw': "User ID / Group ID 長度不足，請確保已正確填寫",
        'zh_cn': "User ID / Group ID 长度不足，请确保已正确填写",
        'en_us': "User ID / Group ID length is too short, please make sure it's correctly filled in",
        'ja_jp': "User ID / Group IDの長さが足りません、正しく入力されていることを確認してください"
    }
    
    success_message = {
        'zh_tw': "測試訊息已成功發送！請在 LINE 應用中查看。",
        'zh_cn': "测试消息已成功发送！请在 LINE 应用中查看。",
        'en_us': "Test message has been sent successfully! Please check your LINE app.",
        'ja_jp': "テストメッセージが正常に送信されました！LINEアプリで確認してください。"
    }
    
    error_message = {
        'zh_tw': "訊息發送失敗，請檢查設定和網絡連接。",
        'zh_cn': "消息发送失败，请检查配置和网络连接。",
        'en_us': "Message sending failed, please check your configuration and network connection.",
        'ja_jp': "メッセージの送信に失敗しました。設定とネットワーク接続を確認してください。"
    }
    
    exception_message = {
        'zh_tw': "發送測試訊息時出現異常: ",
        'zh_cn': "发送测试消息时出现异常: ",
        'en_us': "Exception occurred when sending test message: ",
        'ja_jp': "テストメッセージの送信中に例外が発生しました: "
    }
    
    error_title = {
        'zh_tw': "錯誤",
        'zh_cn': "错误",
        'en_us': "Error",
        'ja_jp': "エラー"
    }
    
    success_title = {
        'zh_tw': "成功",
        'zh_cn': "成功",
        'en_us': "Success",
        'ja_jp': "成功"
    }
    
    # 获取当前语言设置
    current_lang = language_code if language_code in error_token_too_short else 'en_us'
    
    # 验证参数
    if len(line_message_api_token) < 30:
        messagebox.showerror(error_title[current_lang], error_token_too_short[current_lang])
        return
    
    if len(line_message_api_user_id) < 10:
        messagebox.showerror(error_title[current_lang], error_userid_too_short[current_lang])
        return
    
    # 创建多语言测试消息
    test_messages = {
        'zh_tw': "這是一條測試訊息，如果您收到了，說明 LINE Messaging API 配置正確。",
        'zh_cn': "这是一条测试消息，如果您收到了，说明 LINE Messaging API 配置正确。",
        'en_us': "This is a test message. If you received it, your LINE Messaging API configuration is correct.",
        'ja_jp': "これはテストメッセージです。受信できた場合、LINE Messaging APIの設定は正しいです。"
    }
    
    # 发送测试消息
    try:
        result = send_line_notification(
            test_messages[current_lang],
            None,  # 不使用 LINE Notify
            True,  # 使用 LINE Messaging API
            line_message_api_token,
            line_message_api_user_id
        )
        
        if result:
            messagebox.showinfo(success_title[current_lang], success_message[current_lang])
        else:
            messagebox.showerror(error_title[current_lang], error_message[current_lang])
    except Exception as e:
        messagebox.showerror(error_title[current_lang], exception_message[current_lang] + str(e))

def play_mp3_async(sound_filename):
    import threading
    threading.Thread(target=play_mp3, args=(sound_filename,), daemon=True).start()

def play_mp3(sound_filename):
    from playsound import playsound
    try:
        playsound(sound_filename)
    except Exception as exc:
        msg=str(exc)
        print("play sound exeption:", msg)
        if platform.system() == 'Windows':
            import winsound
            try:
                winsound.PlaySound(sound_filename, winsound.SND_FILENAME)
            except Exception as exc2:
                pass

def open_url(url):
    webbrowser.open_new(url)

def btn_exit_clicked():
    root.destroy()

def btn_donate_clicked():
    open_url.open(URL_DONATE)

def btn_help_clicked():
    open_url.open(URL_HELP)

def btn_copy_clicked():
    pyperclip.copy(CONST_ADBLOCK_PLUS_ADVANCED_FILTER_DEFAULT)

def callbackTicketNumberOnChange(event):
    showHidePass1SeatRemaining()

def callbackLanguageOnChange(event):
    applyNewLanguage()

def get_language_code_by_name(new_language):
    language_code = "en_us"
    if u'繁體中文' in new_language:
        language_code = 'zh_tw'
    if u'簡体中文' in new_language:
        language_code = 'zh_cn'
    if u'日本語' in new_language:
        language_code = 'ja_jp'
    #print("new language code:", language_code)

    return language_code

def applyNewLanguage():
    global combo_language
    new_language = combo_language.get().strip()
    #print("new language value:", new_language)

    language_code=get_language_code_by_name(new_language)

    global lbl_homepage
    global lbl_browser
    global lbl_language
    global lbl_ticket_number
    global lbl_pass_1_seat_remaining
    global lbl_auto_check_agree

    # for kktix
    global lbl_auto_press_next_step_button
    global lbl_auto_fill_ticket_number
    global lbl_kktix_area_mode
    global lbl_kktix_area_keyword_1
    global lbl_kktix_area_keyword_1_and_text
    global lbl_kktix_area_keyword_2
    global lbl_kktix_area_keyword_2_and_text
    global lbl_auto_guess_options
    global lbl_user_guess_string

    # for tixcraft
    global lbl_date_auto_select
    global lbl_date_auto_select_mode
    global lbl_date_keyword
    global lbl_area_auto_select
    global lbl_area_auto_select_mode
    global lbl_area_keyword_1
    global lbl_area_keyword_2
    global lbl_area_keyword_3
    global lbl_area_keyword_4
    global lbl_pass_date_is_sold_out
    global lbl_auto_reload_coming_soon_page
    global lbl_presale_code
    global lbl_ocr_captcha
    global lbl_ocr_captcha_with_submit
    global lbl_ocr_captcha_force_submit

    # for checkbox
    global chk_pass_1_seat_remaining
    global chk_auto_check_agree

    global chk_auto_press_next_step_button
    global chk_auto_fill_ticket_number
    global chk_auto_guess_options
    global chk_date_auto_select
    global chk_area_auto_select
    global chk_pass_date_is_sold_out
    global chk_auto_reload_coming_soon_page
    global chk_play_captcha_sound
    global chk_adblock_plus
    global chk_ocr_captcha
    global chk_ocr_captcha_with_sumit
    global chk_ocr_captcha_force_sumit

    global tabControl

    global lbl_slogan
    global lbl_help
    global lbl_donate
    global lbl_release

    global lbl_adblock_plus
    global lbl_adblock_plus_memo
    global lbl_adblock_plus_settings

    lbl_homepage.config(text=translate[language_code]["homepage"])
    lbl_browser.config(text=translate[language_code]["browser"])
    lbl_language.config(text=translate[language_code]["language"])
    lbl_ticket_number.config(text=translate[language_code]["ticket_number"])
    lbl_pass_1_seat_remaining.config(text=translate[language_code]["pass_1_seat_remaining"])
    lbl_auto_check_agree.config(text=translate[language_code]["auto_check_agree"])

    lbl_auto_press_next_step_button.config(text=translate[language_code]["auto_press_next_step_button"])
    lbl_auto_fill_ticket_number.config(text=translate[language_code]["auto_fill_ticket_number"])
    lbl_kktix_area_mode.config(text=translate[language_code]["area_select_order"])
    lbl_kktix_area_keyword_1.config(text=translate[language_code]["area_keyword_1"])
    lbl_kktix_area_keyword_1_and_text.config(text=translate[language_code]["and"])
    lbl_kktix_area_keyword_2.config(text=translate[language_code]["area_keyword_2"])
    lbl_kktix_area_keyword_2_and_text.config(text=translate[language_code]["and"])
    lbl_auto_guess_options.config(text=translate[language_code]["auto_guess_options"])
    lbl_user_guess_string.config(text=translate[language_code]["user_guess_string"])
    
    lbl_date_auto_select.config(text=translate[language_code]["date_auto_select"])
    lbl_date_auto_select_mode.config(text=translate[language_code]["date_select_order"])
    lbl_date_keyword.config(text=translate[language_code]["date_keyword"])
    lbl_area_auto_select.config(text=translate[language_code]["area_auto_select"])
    lbl_area_auto_select_mode.config(text=translate[language_code]["area_select_order"])
    lbl_area_keyword_1.config(text=translate[language_code]["area_keyword_1"])
    lbl_area_keyword_2.config(text=translate[language_code]["area_keyword_2"])
    lbl_area_keyword_3.config(text=translate[language_code]["area_keyword_3"])
    lbl_area_keyword_4.config(text=translate[language_code]["area_keyword_4"])
    lbl_pass_date_is_sold_out.config(text=translate[language_code]["pass_date_is_sold_out"])
    lbl_auto_reload_coming_soon_page.config(text=translate[language_code]["auto_reload_coming_soon_page"])
    lbl_presale_code.config(text=translate[language_code]["user_guess_string"])
    lbl_ocr_captcha.config(text=translate[language_code]["ocr_captcha"])
    lbl_ocr_captcha_with_submit.config(text=translate[language_code]["ocr_captcha_with_submit"])
    lbl_ocr_captcha_force_submit.config(text=translate[language_code]["ocr_captcha_force_submit"])

    chk_pass_1_seat_remaining.config(text=translate[language_code]["enable"])
    chk_auto_check_agree.config(text=translate[language_code]["enable"])
    chk_auto_press_next_step_button.config(text=translate[language_code]["enable"])
    chk_auto_fill_ticket_number.config(text=translate[language_code]["enable"])
    chk_auto_guess_options.config(text=translate[language_code]["enable"])
    chk_date_auto_select.config(text=translate[language_code]["enable"])
    chk_area_auto_select.config(text=translate[language_code]["enable"])
    chk_pass_date_is_sold_out.config(text=translate[language_code]["enable"])
    chk_auto_reload_coming_soon_page.config(text=translate[language_code]["enable"])
    chk_play_captcha_sound.config(text=translate[language_code]["enable"])
    chk_adblock_plus.config(text=translate[language_code]["enable"])
    chk_ocr_captcha.config(text=translate[language_code]["enable"])
    chk_ocr_captcha_with_sumit.config(text=translate[language_code]["enable"])
    chk_ocr_captcha_force_sumit.config(text=translate[language_code]["enable"])

    tabControl.tab(0, text=translate[language_code]["preference"])
    tabControl.tab(1, text=translate[language_code]["advanced"])
    tabControl.tab(2, text=translate[language_code]["about"])

    global lbl_facebook_account
    global lbl_kktix_account
    global lbl_play_captcha_sound
    global lbl_captcha_sound_filename
    lbl_facebook_account.config(text=translate[language_code]["facebook_account"])
    lbl_kktix_account.config(text=translate[language_code]["kktix_account"])
    lbl_play_captcha_sound.config(text=translate[language_code]["play_captcha_sound"])
    lbl_captcha_sound_filename.config(text=translate[language_code]["captcha_sound_filename"])

    lbl_slogan.config(text=translate[language_code]["maxbot_slogan"])
    lbl_help.config(text=translate[language_code]["help"])
    lbl_donate.config(text=translate[language_code]["donate"])
    lbl_release.config(text=translate[language_code]["release"])

    lbl_adblock_plus.config(text=translate[language_code]["adblock_plus_enable"])
    lbl_adblock_plus_memo.config(text=translate[language_code]["adblock_plus_memo"])
    lbl_adblock_plus_settings.config(text=translate[language_code]["adblock_plus_settings"])

    global btn_run
    global btn_save
    global btn_exit
    global btn_restore_defaults

    btn_run.config(text=translate[language_code]["run"])
    btn_save.config(text=translate[language_code]["save"])
    if btn_exit:
        btn_exit.config(text=translate[language_code]["exit"])
    btn_restore_defaults.config(text=translate[language_code]["restore_defaults"])

def callbackHomepageOnChange(event):
    showHideBlocks()

def callbackDateAutoOnChange():
    showHideTixcraftBlocks()

def showHideBlocks():
    global UI_PADDING_X

    global frame_group_kktix
    global frame_group_kktix_index
    global frame_group_tixcraft
    global frame_group_tixcraft_index

    global combo_homepage

    new_homepage = combo_homepage.get().strip()
    #print("new homepage value:", new_homepage)

    BLOCK_STYLE_TIXCRAFT = 0
    BLOCK_STYLE_KKTIX = 1
    STYLE_KKTIX_DOMAIN_LIST = ['kktix']

    show_block_index = BLOCK_STYLE_TIXCRAFT
    for domain_name in STYLE_KKTIX_DOMAIN_LIST:
        if domain_name in new_homepage:
            show_block_index = BLOCK_STYLE_KKTIX

    if show_block_index == BLOCK_STYLE_KKTIX:
        frame_group_kktix.grid(column=0, row=frame_group_kktix_index, padx=UI_PADDING_X)
        frame_group_tixcraft.grid_forget()

    else:
        frame_group_tixcraft.grid(column=0, row=frame_group_tixcraft_index, padx=UI_PADDING_X)
        frame_group_kktix.grid_forget()

    showHideTixcraftBlocks()
    showHidePass1SeatRemaining()
    showHideOcrCaptchaWithSubmit()

def showHideOcrCaptchaWithSubmit():
    global chk_state_ocr_captcha
    is_ocr_captcha_enable = bool(chk_state_ocr_captcha.get())

    global ocr_captcha_with_submit_index
    global lbl_ocr_captcha_with_submit
    global chk_ocr_captcha_with_sumit

    if is_ocr_captcha_enable:
        # show.
        lbl_ocr_captcha_with_submit.grid(column=0, row=ocr_captcha_with_submit_index, sticky = E)
        chk_ocr_captcha_with_sumit.grid(column=1, row=ocr_captcha_with_submit_index, sticky = W)
    else:
        # hide
        lbl_ocr_captcha_with_submit.grid_forget()
        chk_ocr_captcha_with_sumit.grid_forget()

    global chk_state_ocr_captcha_with_submit
    is_ocr_captcha_auto_submit_enable = bool(chk_state_ocr_captcha_with_submit.get())

    global ocr_captcha_force_submit_index
    global lbl_ocr_captcha_force_submit
    global chk_ocr_captcha_force_sumit

    if is_ocr_captcha_auto_submit_enable:
        # show.
        lbl_ocr_captcha_force_submit.grid(column=0, row=ocr_captcha_force_submit_index, sticky = E)
        chk_ocr_captcha_force_sumit.grid(column=1, row=ocr_captcha_force_submit_index, sticky = W)
    else:
        # hide
        lbl_ocr_captcha_force_submit.grid_forget()
        chk_ocr_captcha_force_sumit.grid_forget()

def showHidePass1SeatRemaining():
    global combo_ticket_number
    ticket_number_int = int(combo_ticket_number.get().strip())

    global pass_1_seat_remaining_index
    global lbl_pass_1_seat_remaining
    global chk_pass_1_seat_remaining

    if ticket_number_int > 1:
        # show.
        lbl_pass_1_seat_remaining.grid(column=0, row=pass_1_seat_remaining_index, sticky = E)
        chk_pass_1_seat_remaining.grid(column=1, row=pass_1_seat_remaining_index, sticky = W)
    else:
        # hide
        lbl_pass_1_seat_remaining.grid_forget()
        chk_pass_1_seat_remaining.grid_forget()

# purpose: show detail blocks if master field is enable.
def showHideTixcraftBlocks():
    # for tixcraft show/hide enable.
    # field 1
    global chk_state_date_auto_select

    global date_auto_select_mode_index
    global lbl_date_auto_select_mode
    global combo_date_auto_select_mode

    global date_keyword_index
    global lbl_date_keyword
    global txt_date_keyword

    # field 2
    global chk_area_auto_select

    global area_auto_select_index
    global lbl_area_auto_select_mode
    global combo_area_auto_select_mode

    global area_keyword_1_index
    global area_keyword_2_index
    global area_keyword_3_index
    global area_keyword_4_index

    global lbl_area_keyword_1
    global lbl_area_keyword_2
    global lbl_area_keyword_3
    global lbl_area_keyword_4

    global txt_area_keyword_1
    global txt_area_keyword_2
    global txt_area_keyword_3
    global txt_area_keyword_4

    is_date_set_to_enable = bool(chk_state_date_auto_select.get())
    is_area_set_to_enable = bool(chk_state_area_auto_select.get())
    #print("now is_date_set_to_enable value:", is_date_set_to_enable)
    #print("now is_area_set_to_enable value:", is_area_set_to_enable)

    if is_date_set_to_enable:
        # show
        lbl_date_auto_select_mode.grid(column=0, row=date_auto_select_mode_index, sticky = E)
        combo_date_auto_select_mode.grid(column=1, row=date_auto_select_mode_index, sticky = W)

        lbl_date_keyword.grid(column=0, row=date_keyword_index, sticky = E)
        txt_date_keyword.grid(column=1, row=date_keyword_index, sticky = W)
    else:
        # hide
        lbl_date_auto_select_mode.grid_forget()
        combo_date_auto_select_mode.grid_forget()

        lbl_date_keyword.grid_forget()
        txt_date_keyword.grid_forget()

    if is_area_set_to_enable:
        # show
        lbl_area_auto_select_mode.grid(column=0, row=area_auto_select_index, sticky = E)
        combo_area_auto_select_mode.grid(column=1, row=area_auto_select_index, sticky = W)

        lbl_area_keyword_1.grid(column=0, row=area_keyword_1_index, sticky = E)
        txt_area_keyword_1.grid(column=1, row=area_keyword_1_index, sticky = W)

        lbl_area_keyword_2.grid(column=0, row=area_keyword_2_index, sticky = E)
        txt_area_keyword_2.grid(column=1, row=area_keyword_2_index, sticky = W)

        lbl_area_keyword_3.grid(column=0, row=area_keyword_3_index, sticky = E)
        txt_area_keyword_3.grid(column=1, row=area_keyword_3_index, sticky = W)

        lbl_area_keyword_4.grid(column=0, row=area_keyword_4_index, sticky = E)
        txt_area_keyword_4.grid(column=1, row=area_keyword_4_index, sticky = W)
    else:
        # hide
        lbl_area_auto_select_mode.grid_forget()
        combo_area_auto_select_mode.grid_forget()

        lbl_area_keyword_1.grid_forget()
        txt_area_keyword_1.grid_forget()

        lbl_area_keyword_2.grid_forget()
        txt_area_keyword_2.grid_forget()

        lbl_area_keyword_3.grid_forget()
        txt_area_keyword_3.grid_forget()

        lbl_area_keyword_4.grid_forget()
        txt_area_keyword_4.grid_forget()


def PreferenctTab(root, config_dict, language_code, UI_PADDING_X):
    homepage = CONST_HOMEPAGE_DEFAULT
    ticket_number = 2
    pass_1_seat_remaining_enable = False
    auto_check_agree_enable = False

    auto_press_next_step_button = False
    auto_fill_ticket_number = False

    kktix_area_mode = ""
    kktix_area_keyword_1 = ""
    kktix_area_keyword_1_and = ""
    kktix_area_keyword_2 = ""
    kktix_area_keyword_2_and = ""
    # disable password brute force attack
    # PS: because of the question is always variable.
    #kktix_answer_dictionary = ""
    auto_guess_options = False
    user_guess_string = ""

    date_auto_select_enable = None
    date_auto_select_mode = ""
    date_keyword = ""

    area_auto_select_enable = None
    area_auto_select_mode = ""
    area_keyword_1 = ""
    area_keyword_2 = ""
    area_keyword_3 = ""
    area_keyword_4 = ""

    pass_date_is_sold_out_enable = False
    auto_reload_coming_soon_page_enable = True
    presale_code = ""

    debugMode = False

    # read config.
    homepage = config_dict["homepage"]
    browser = config_dict["browser"]
    language = config_dict["language"]
    debugMode = config_dict["debug"]

    # default ticket number
    # 說明：自動選擇的票數
    ticket_number = config_dict["ticket_number"]
    pass_1_seat_remaining_enable = config_dict["pass_1_seat_remaining"]
    auto_check_agree_enable = config_dict["auto_check_agree"]

    # for ["kktix"]
    auto_press_next_step_button = config_dict["kktix"]["auto_press_next_step_button"]
    auto_fill_ticket_number = config_dict["kktix"]["auto_fill_ticket_number"]
    kktix_area_mode = config_dict["kktix"]["area_mode"].strip()
    if not kktix_area_mode in CONST_SELECT_OPTIONS_ARRAY:
        kktix_area_mode = CONST_SELECT_ORDER_DEFAULT
    kktix_area_keyword_1 = config_dict["kktix"]["area_keyword_1"].strip()
    kktix_area_keyword_1_and = config_dict["kktix"]["area_keyword_1_and"].strip()
    kktix_area_keyword_2 = config_dict["kktix"]["area_keyword_2"].strip()
    kktix_area_keyword_2_and = config_dict["kktix"]["area_keyword_2_and"].strip()
    auto_guess_options = config_dict["kktix"]["auto_guess_options"]
    user_guess_string = config_dict["kktix"]["user_guess_string"].strip()

    # disable password brute force attack
    # PS: feature disabled.
    if 'answer_dictionary' in config_dict["kktix"]:
        kktix_answer_dictionary = config_dict["kktix"]["answer_dictionary"]
        if kktix_answer_dictionary is None:
            kktix_answer_dictionary = ""
        kktix_answer_dictionary = kktix_answer_dictionary.strip()

    # for ["tixcraft"]
    date_auto_select_enable = config_dict["tixcraft"]["date_auto_select"]["enable"]
    date_auto_select_mode = config_dict["tixcraft"]["date_auto_select"]["mode"]
    if not date_auto_select_mode in CONST_SELECT_OPTIONS_ARRAY:
        date_auto_select_mode = CONST_SELECT_ORDER_DEFAULT
    date_keyword = config_dict["tixcraft"]["date_auto_select"]["date_keyword"].strip()
    area_auto_select_enable = config_dict["tixcraft"]["area_auto_select"]["enable"]
    area_auto_select_mode = config_dict["tixcraft"]["area_auto_select"]["mode"]
    if not area_auto_select_mode in CONST_SELECT_OPTIONS_ARRAY:
        area_auto_select_mode = CONST_SELECT_ORDER_DEFAULT
    area_keyword_1 = config_dict["tixcraft"]["area_auto_select"]["area_keyword_1"].strip()
    area_keyword_2 = config_dict["tixcraft"]["area_auto_select"]["area_keyword_2"].strip()
    area_keyword_3 = config_dict["tixcraft"]["area_auto_select"]["area_keyword_3"].strip()
    area_keyword_4 = config_dict["tixcraft"]["area_auto_select"]["area_keyword_4"].strip()
    pass_date_is_sold_out_enable = config_dict["tixcraft"]["pass_date_is_sold_out"]
    auto_reload_coming_soon_page_enable = config_dict["tixcraft"]["auto_reload_coming_soon_page"]
    presale_code = config_dict["tixcraft"]["presale_code"].strip()

    # output config:
    print("setting app version", CONST_APP_VERSION)
    print("python version", platform.python_version())
    print("platform", platform.platform())
    print("homepage", homepage)
    print("ticket_number", ticket_number)
    print("pass_1_seat_remaining", pass_1_seat_remaining_enable)
    print("auto_check_agree", auto_check_agree_enable)

    # for kktix
    print("==[kktix]==")
    print("auto_press_next_step_button", auto_press_next_step_button)
    print("auto_fill_ticket_number", auto_fill_ticket_number)
    print("kktix_area_mode", kktix_area_mode)
    print("kktix_area_keyword_1", kktix_area_keyword_1)
    print("kktix_area_keyword_1_and", kktix_area_keyword_1_and)
    # disable password brute force attack
    #print("kktix_answer_dictionary", kktix_answer_dictionary)
    print("auto_guess_options", auto_guess_options)
    print("user_guess_string", user_guess_string)

    # for tixcraft
    print("==[tixcraft]==")
    print("date_auto_select_enable", date_auto_select_enable)
    print("date_auto_select_mode", date_auto_select_mode)
    print("date_keyword", date_keyword)

    print("area_auto_select_enable", area_auto_select_enable)
    print("area_auto_select_mode", area_auto_select_mode)
    print("area_keyword_1", area_keyword_1)
    print("area_keyword_2", area_keyword_2)
    print("area_keyword_3", area_keyword_3)
    print("area_keyword_4", area_keyword_4)

    print("pass_date_is_sold_out", pass_date_is_sold_out_enable)

    print("auto_reload_coming_soon_page", auto_reload_coming_soon_page_enable)
    print("presale_code", presale_code)

    print("debug Mode", debugMode)

    global lbl_homepage
    global lbl_ticket_number

    global lbl_kktix
    global lbl_tixcraft

    row_count = 0

    frame_group_header = Frame(root)
    group_row_count = 0

    # first row need padding Y
    lbl_homepage = Label(frame_group_header, text=translate[language_code]['homepage'])
    lbl_homepage.grid(column=0, row=group_row_count, sticky = E)

    global combo_homepage
    combo_homepage = ttk.Combobox(frame_group_header, state="readonly")
    combo_homepage['values']= ("https://kktix.com","https://tixcraft.com","https://www.indievox.com/","https://www.famiticket.com.tw","http://www.urbtix.hk/","https://www.cityline.com/","https://ticket.ibon.com.tw/")
    combo_homepage.set(homepage)
    combo_homepage.bind("<<ComboboxSelected>>", callbackHomepageOnChange)
    combo_homepage.grid(column=1, row=group_row_count, sticky = W)

    group_row_count+=1

    lbl_ticket_number = Label(frame_group_header, text=translate[language_code]['ticket_number'])
    lbl_ticket_number.grid(column=0, row=group_row_count, sticky = E)

    global combo_ticket_number
    # for text format.
    # PS: some user keyin wrong type. @_@;
    '''
    global combo_ticket_number_value
    combo_ticket_number_value = StringVar(frame_group_header, value=ticket_number)
    combo_ticket_number = Entry(frame_group_header, width=20, textvariable = combo_ticket_number_value)
    combo_ticket_number.grid(column=1, row=group_row_count, sticky = W)
    '''
    combo_ticket_number = ttk.Combobox(frame_group_header, state="readonly")
    combo_ticket_number['values']= ("1","2","3","4","5","6","7","8","9","10","11","12")
    #combo_ticket_number.current(0)
    combo_ticket_number.set(str(ticket_number))
    combo_ticket_number.bind("<<ComboboxSelected>>", callbackTicketNumberOnChange)
    combo_ticket_number.grid(column=1, row=group_row_count, sticky = W)

    group_row_count+=1

    global pass_1_seat_remaining_index
    pass_1_seat_remaining_index = group_row_count

    global lbl_pass_1_seat_remaining
    lbl_pass_1_seat_remaining = Label(frame_group_header, text=translate[language_code]['pass_1_seat_remaining'])
    lbl_pass_1_seat_remaining.grid(column=0, row=group_row_count, sticky = E)

    global chk_state_pass_1_seat_remaining
    chk_state_pass_1_seat_remaining = BooleanVar()
    chk_state_pass_1_seat_remaining.set(pass_1_seat_remaining_enable)

    global chk_pass_1_seat_remaining
    chk_pass_1_seat_remaining = Checkbutton(frame_group_header, text=translate[language_code]['enable'], variable=chk_state_pass_1_seat_remaining)
    chk_pass_1_seat_remaining.grid(column=1, row=group_row_count, sticky = W)

    group_row_count+=1

    global lbl_auto_check_agree
    lbl_auto_check_agree = Label(frame_group_header, text=translate[language_code]['auto_check_agree'])
    lbl_auto_check_agree.grid(column=0, row=group_row_count, sticky = E)

    global chk_state_auto_check_agree
    chk_state_auto_check_agree = BooleanVar()
    chk_state_auto_check_agree.set(auto_check_agree_enable)

    global chk_auto_check_agree
    chk_auto_check_agree = Checkbutton(frame_group_header, text=translate[language_code]['enable'], variable=chk_state_auto_check_agree)
    chk_auto_check_agree.grid(column=1, row=group_row_count, sticky = W)

    frame_group_header.grid(column=0, row=row_count, sticky = W, padx=UI_PADDING_X)

    row_count+=1

    # for sub group KKTix.
    global frame_group_kktix
    frame_group_kktix = Frame(root)
    group_row_count = 0

    # start sub group...
    group_row_count+=1

    global lbl_auto_press_next_step_button
    lbl_auto_press_next_step_button = Label(frame_group_kktix, text=translate[language_code]['auto_press_next_step_button'])
    lbl_auto_press_next_step_button.grid(column=0, row=group_row_count, sticky = E)

    global chk_state_auto_press_next_step_button
    chk_state_auto_press_next_step_button = BooleanVar()
    chk_state_auto_press_next_step_button.set(auto_press_next_step_button)

    global chk_auto_press_next_step_button
    chk_auto_press_next_step_button = Checkbutton(frame_group_kktix, text=translate[language_code]['enable'], variable=chk_state_auto_press_next_step_button)
    chk_auto_press_next_step_button.grid(column=1, row=group_row_count, sticky = W)

    group_row_count+=1

    global lbl_auto_fill_ticket_number
    lbl_auto_fill_ticket_number = Label(frame_group_kktix, text=translate[language_code]['auto_fill_ticket_number'])
    lbl_auto_fill_ticket_number.grid(column=0, row=group_row_count, sticky = E)

    global chk_state_auto_fill_ticket_number
    chk_state_auto_fill_ticket_number = BooleanVar()
    chk_state_auto_fill_ticket_number.set(auto_fill_ticket_number)

    global chk_auto_fill_ticket_number
    chk_auto_fill_ticket_number = Checkbutton(frame_group_kktix, text=translate[language_code]['enable'], variable=chk_state_auto_fill_ticket_number)
    chk_auto_fill_ticket_number.grid(column=1, row=group_row_count, sticky = W)

    group_row_count+=1

    global lbl_kktix_area_mode
    lbl_kktix_area_mode = Label(frame_group_kktix, text=translate[language_code]['area_select_order'])
    lbl_kktix_area_mode.grid(column=0, row=group_row_count, sticky = E)

    global combo_kktix_area_mode
    global combo_kktix_area_mode_index
    combo_kktix_area_mode_index = group_row_count
    combo_kktix_area_mode = ttk.Combobox(frame_group_kktix, state="readonly")
    combo_kktix_area_mode['values']= CONST_SELECT_OPTIONS_DEFAULT
    combo_kktix_area_mode.set(kktix_area_mode)
    combo_kktix_area_mode.grid(column=1, row=group_row_count, sticky = W)

    group_row_count+=1

    global lbl_kktix_area_keyword_1
    lbl_kktix_area_keyword_1 = Label(frame_group_kktix, text=translate[language_code]['area_keyword_1'])
    lbl_kktix_area_keyword_1.grid(column=0, row=group_row_count, sticky = E)

    global txt_kktix_area_keyword_1
    txt_kktix_area_keyword_1_value = StringVar(frame_group_kktix, value=kktix_area_keyword_1)
    txt_kktix_area_keyword_1 = Entry(frame_group_kktix, width=20, textvariable = txt_kktix_area_keyword_1_value)
    txt_kktix_area_keyword_1.grid(column=1, row=group_row_count, sticky = W)

    group_row_count+=1

    lbl_kktix_area_keyword_1_and_label = Label(frame_group_kktix, text="")
    lbl_kktix_area_keyword_1_and_label.grid(column=0, row=group_row_count, sticky = E)

    global lbl_kktix_area_keyword_1_and_text
    lbl_kktix_area_keyword_1_and_text = Label(frame_group_kktix, text=translate[language_code]["and"])
    lbl_kktix_area_keyword_1_and_text.grid(column=1, row=group_row_count, sticky = W)

    group_row_count+=1

    lbl_kktix_area_keyword_1_tmp = Label(frame_group_kktix, text="")
    lbl_kktix_area_keyword_1_tmp.grid(column=0, row=group_row_count, sticky = E)

    global txt_kktix_area_keyword_1_and
    txt_kktix_area_keyword_1_and_value = StringVar(frame_group_kktix, value=kktix_area_keyword_1_and)
    txt_kktix_area_keyword_1_and = Entry(frame_group_kktix, width=20, textvariable = txt_kktix_area_keyword_1_and_value)
    txt_kktix_area_keyword_1_and.grid(column=1, row=group_row_count, sticky = W)

    group_row_count+=1

    global lbl_kktix_area_keyword_2
    lbl_kktix_area_keyword_2 = Label(frame_group_kktix, text=translate[language_code]['area_keyword_2'])
    lbl_kktix_area_keyword_2.grid(column=0, row=group_row_count, sticky = E)

    global txt_kktix_area_keyword_2
    txt_kktix_area_keyword_2_value = StringVar(frame_group_kktix, value=kktix_area_keyword_2)
    txt_kktix_area_keyword_2 = Entry(frame_group_kktix, width=20, textvariable = txt_kktix_area_keyword_2_value)
    txt_kktix_area_keyword_2.grid(column=1, row=group_row_count, sticky = W)

    group_row_count+=1

    lbl_kktix_area_keyword_2_and_label = Label(frame_group_kktix, text="")
    lbl_kktix_area_keyword_2_and_label.grid(column=0, row=group_row_count, sticky = E)

    global lbl_kktix_area_keyword_2_and_text
    lbl_kktix_area_keyword_2_and_text = Label(frame_group_kktix, text=translate[language_code]['and'])
    lbl_kktix_area_keyword_2_and_text.grid(column=1, row=group_row_count, sticky = W)

    group_row_count+=1

    lbl_kktix_area_keyword_2_tmp = Label(frame_group_kktix, text="")
    lbl_kktix_area_keyword_2_tmp.grid(column=0, row=group_row_count, sticky = E)

    global txt_kktix_area_keyword_2_and
    txt_kktix_area_keyword_2_and_value = StringVar(frame_group_kktix, value=kktix_area_keyword_2_and)
    txt_kktix_area_keyword_2_and = Entry(frame_group_kktix, width=20, textvariable = txt_kktix_area_keyword_2_and_value)
    txt_kktix_area_keyword_2_and.grid(column=1, row=group_row_count, sticky = W)

    #group_row_count+=1

    # disable password brute force attack
    global lbl_kktix_answer_dictionary
    #lbl_kktix_answer_dictionary = Label(frame_group_kktix, text="Answer Dictionary")
    #lbl_kktix_answer_dictionary.grid(column=0, row=group_row_count, sticky = E)

    global txt_kktix_answer_dictionary
    global txt_kktix_answer_dictionary_index
    txt_kktix_answer_dictionary_index = group_row_count
    #txt_kktix_answer_dictionary_value = StringVar(frame_group_kktix, value=kktix_answer_dictionary)
    #txt_kktix_answer_dictionary = Entry(frame_group_kktix, width=20, textvariable = txt_kktix_answer_dictionary_value)
    #txt_kktix_answer_dictionary.grid(column=1, row=group_row_count, sticky = W)

    group_row_count+=1

    global lbl_auto_guess_options
    lbl_auto_guess_options = Label(frame_group_kktix, text=translate[language_code]['auto_guess_options'])
    lbl_auto_guess_options.grid(column=0, row=group_row_count, sticky = E)

    global chk_state_auto_guess_options
    chk_state_auto_guess_options = BooleanVar()
    chk_state_auto_guess_options.set(auto_guess_options)

    global chk_auto_guess_options
    chk_auto_guess_options = Checkbutton(frame_group_kktix, text=translate[language_code]['enable'], variable=chk_state_auto_guess_options)
    chk_auto_guess_options.grid(column=1, row=group_row_count, sticky = W)

    group_row_count+=1

    global lbl_user_guess_string
    lbl_user_guess_string = Label(frame_group_kktix, text=translate[language_code]['user_guess_string'])
    lbl_user_guess_string.grid(column=0, row=group_row_count, sticky = E)

    global txt_kktix_user_guess_string
    txt_kktix_user_guess_string_value = StringVar(frame_group_kktix, value=user_guess_string)
    txt_kktix_user_guess_string = Entry(frame_group_kktix, width=20, textvariable = txt_kktix_user_guess_string_value)
    txt_kktix_user_guess_string.grid(column=1, row=group_row_count, sticky = W)


    global frame_group_kktix_index
    frame_group_kktix_index = row_count
    #PS: don't need show when onload(), because show/hide block will load again.
    #frame_group_kktix.grid(column=0, row=row_count, sticky = W, padx=UI_PADDING_X)

    row_count+=1

    # for sub group tixcraft.
    global frame_group_tixcraft
    frame_group_tixcraft = Frame(root)
    group_row_count = 0

    # start sub group.
    group_row_count+=1

    global lbl_date_auto_select
    lbl_date_auto_select = Label(frame_group_tixcraft, text=translate[language_code]['date_auto_select'])
    lbl_date_auto_select.grid(column=0, row=group_row_count, sticky = E)

    global chk_state_date_auto_select
    chk_state_date_auto_select = BooleanVar()
    chk_state_date_auto_select.set(date_auto_select_enable)

    global chk_date_auto_select
    chk_date_auto_select = Checkbutton(frame_group_tixcraft, text=translate[language_code]['enable'], variable=chk_state_date_auto_select, command=callbackDateAutoOnChange)
    chk_date_auto_select.grid(column=1, row=group_row_count, sticky = W)

    group_row_count+=1

    global date_auto_select_mode_index
    date_auto_select_mode_index = group_row_count

    global lbl_date_auto_select_mode
    lbl_date_auto_select_mode = Label(frame_group_tixcraft, text=translate[language_code]['date_select_order'])
    lbl_date_auto_select_mode.grid(column=0, row=date_auto_select_mode_index, sticky = E)

    global combo_date_auto_select_mode
    combo_date_auto_select_mode = ttk.Combobox(frame_group_tixcraft, state="readonly")
    combo_date_auto_select_mode['values']= (CONST_FROM_TOP_TO_BOTTOM, CONST_FROM_BOTTOM_TO_TOP)
    combo_date_auto_select_mode.set(date_auto_select_mode)
    combo_date_auto_select_mode.grid(column=1, row=date_auto_select_mode_index, sticky = W)

    group_row_count+=1

    global date_keyword_index
    date_keyword_index = group_row_count

    global lbl_date_keyword
    lbl_date_keyword = Label(frame_group_tixcraft, text=translate[language_code]['date_keyword'])
    lbl_date_keyword.grid(column=0, row=date_keyword_index, sticky = E)

    global txt_date_keyword
    txt_date_keyword_value = StringVar(frame_group_tixcraft, value=date_keyword)
    txt_date_keyword = Entry(frame_group_tixcraft, width=20, textvariable = txt_date_keyword_value)
    txt_date_keyword.grid(column=1, row=date_keyword_index, sticky = W)

    group_row_count+=1

    global lbl_pass_date_is_sold_out
    lbl_pass_date_is_sold_out = Label(frame_group_tixcraft, text=translate[language_code]['pass_date_is_sold_out'])
    lbl_pass_date_is_sold_out.grid(column=0, row=group_row_count, sticky = E)

    global chk_state_pass_date_is_sold_out
    chk_state_pass_date_is_sold_out = BooleanVar()
    chk_state_pass_date_is_sold_out.set(pass_date_is_sold_out_enable)

    global chk_pass_date_is_sold_out
    chk_pass_date_is_sold_out = Checkbutton(frame_group_tixcraft, text=translate[language_code]['enable'], variable=chk_state_pass_date_is_sold_out)
    chk_pass_date_is_sold_out.grid(column=1, row=group_row_count, sticky = W)

    group_row_count+=1

    global lbl_auto_reload_coming_soon_page
    lbl_auto_reload_coming_soon_page = Label(frame_group_tixcraft, text=translate[language_code]['auto_reload_coming_soon_page'])
    lbl_auto_reload_coming_soon_page.grid(column=0, row=group_row_count, sticky = E)

    global chk_state_auto_reload_coming_soon_page
    chk_state_auto_reload_coming_soon_page = BooleanVar()
    chk_state_auto_reload_coming_soon_page.set(auto_reload_coming_soon_page_enable)

    global chk_auto_reload_coming_soon_page
    chk_auto_reload_coming_soon_page = Checkbutton(frame_group_tixcraft, text=translate[language_code]['enable'], variable=chk_state_auto_reload_coming_soon_page)
    chk_auto_reload_coming_soon_page.grid(column=1, row=group_row_count, sticky = W)

    group_row_count+=1

    global lbl_date_hr
    lbl_date_hr = Label(frame_group_tixcraft, text='')
    lbl_date_hr.grid(column=0, row=group_row_count, sticky = E, columnspan=2)

    group_row_count+=1

    global lbl_area_auto_select
    lbl_area_auto_select = Label(frame_group_tixcraft, text=translate[language_code]['area_auto_select'])
    lbl_area_auto_select.grid(column=0, row=group_row_count, sticky = E)

    global chk_state_area_auto_select
    chk_state_area_auto_select = BooleanVar()
    chk_state_area_auto_select.set(area_auto_select_enable)

    global chk_area_auto_select
    chk_area_auto_select = Checkbutton(frame_group_tixcraft, text=translate[language_code]['enable'], variable=chk_state_area_auto_select, command=callbackDateAutoOnChange)
    chk_area_auto_select.grid(column=1, row=group_row_count, sticky = W)

    group_row_count+=1

    global area_auto_select_index
    area_auto_select_index = group_row_count

    global lbl_area_auto_select_mode
    lbl_area_auto_select_mode = Label(frame_group_tixcraft, text=translate[language_code]['area_auto_select'])
    lbl_area_auto_select_mode.grid(column=0, row=area_auto_select_index, sticky = E)

    global combo_area_auto_select_mode
    combo_area_auto_select_mode = ttk.Combobox(frame_group_tixcraft, state="readonly")
    combo_area_auto_select_mode['values']= CONST_SELECT_OPTIONS_DEFAULT
    combo_area_auto_select_mode.set(area_auto_select_mode)
    combo_area_auto_select_mode.grid(column=1, row=area_auto_select_index, sticky = W)

    group_row_count+=1

    global area_keyword_1_index
    area_keyword_1_index = group_row_count

    global lbl_area_keyword_1
    lbl_area_keyword_1 = Label(frame_group_tixcraft, text=translate[language_code]['area_keyword_1'])
    lbl_area_keyword_1.grid(column=0, row=area_keyword_1_index, sticky = E)

    global txt_area_keyword_1
    txt_area_keyword_1_value = StringVar(frame_group_tixcraft, value=area_keyword_1)
    txt_area_keyword_1 = Entry(frame_group_tixcraft, width=20, textvariable = txt_area_keyword_1_value)
    txt_area_keyword_1.grid(column=1, row=area_keyword_1_index, sticky = W)

    group_row_count+=1

    global area_keyword_2_index
    area_keyword_2_index = group_row_count

    global lbl_area_keyword_2
    lbl_area_keyword_2 = Label(frame_group_tixcraft, text=translate[language_code]['area_keyword_2'])
    lbl_area_keyword_2.grid(column=0, row=area_keyword_2_index, sticky = E)

    global txt_area_keyword_2
    txt_area_keyword_2_value = StringVar(frame_group_tixcraft, value=area_keyword_2)
    txt_area_keyword_2 = Entry(frame_group_tixcraft, width=20, textvariable = txt_area_keyword_2_value)
    txt_area_keyword_2.grid(column=1, row=area_keyword_2_index, sticky = W)

    group_row_count+=1

    global area_keyword_3_index
    area_keyword_3_index = group_row_count

    global lbl_area_keyword_3
    lbl_area_keyword_3 = Label(frame_group_tixcraft, text=translate[language_code]['area_keyword_3'])
    lbl_area_keyword_3.grid(column=0, row=area_keyword_3_index, sticky = E)

    global txt_area_keyword_3
    txt_area_keyword_3_value = StringVar(frame_group_tixcraft, value=area_keyword_3)
    txt_area_keyword_3 = Entry(frame_group_tixcraft, width=20, textvariable = txt_area_keyword_3_value)
    txt_area_keyword_3.grid(column=1, row=area_keyword_3_index, sticky = W)

    group_row_count+=1

    global area_keyword_4_index
    area_keyword_4_index = group_row_count

    global lbl_area_keyword_4
    lbl_area_keyword_4 = Label(frame_group_tixcraft, text=translate[language_code]['area_keyword_4'])
    lbl_area_keyword_4.grid(column=0, row=area_keyword_4_index, sticky = E)

    global txt_area_keyword_4
    txt_area_keyword_4_value = StringVar(frame_group_tixcraft, value=area_keyword_4)
    txt_area_keyword_4 = Entry(frame_group_tixcraft, width=20, textvariable = txt_area_keyword_4_value)
    txt_area_keyword_4.grid(column=1, row=area_keyword_4_index, sticky = W)

    group_row_count+=1

    global lbl_presale_code
    lbl_presale_code = Label(frame_group_tixcraft, text=translate[language_code]['user_guess_string'])
    lbl_presale_code.grid(column=0, row=group_row_count, sticky = E)

    global txt_presale_code
    txt_presale_code_value = StringVar(frame_group_tixcraft, value=presale_code)
    txt_presale_code = Entry(frame_group_tixcraft, width=20, textvariable = txt_presale_code_value)
    txt_presale_code.grid(column=1, row=group_row_count, sticky = W)

    group_row_count+=1

    global lbl_ocr_captcha
    lbl_ocr_captcha = Label(frame_group_tixcraft, text=translate[language_code]['ocr_captcha'])
    lbl_ocr_captcha.grid(column=0, row=group_row_count, sticky = E)

    global chk_state_ocr_captcha
    chk_state_ocr_captcha = BooleanVar()
    chk_state_ocr_captcha.set(config_dict['ocr_captcha']["enable"])

    global chk_ocr_captcha
    chk_ocr_captcha = Checkbutton(frame_group_tixcraft, text=translate[language_code]['enable'], variable=chk_state_ocr_captcha, command=showHideOcrCaptchaWithSubmit)
    chk_ocr_captcha.grid(column=1, row=group_row_count, sticky = W)

    group_row_count+=1

    global ocr_captcha_with_submit_index
    ocr_captcha_with_submit_index = group_row_count

    global lbl_ocr_captcha_with_submit
    lbl_ocr_captcha_with_submit = Label(frame_group_tixcraft, text=translate[language_code]['ocr_captcha_with_submit'])
    lbl_ocr_captcha_with_submit.grid(column=0, row=ocr_captcha_with_submit_index, sticky = E)

    global chk_state_ocr_captcha_with_submit
    chk_state_ocr_captcha_with_submit = BooleanVar()
    chk_state_ocr_captcha_with_submit.set(config_dict['ocr_captcha']["auto_submit"])

    global chk_ocr_captcha_with_sumit
    chk_ocr_captcha_with_sumit = Checkbutton(frame_group_tixcraft, text=translate[language_code]['enable'], variable=chk_state_ocr_captcha_with_submit, command=showHideOcrCaptchaWithSubmit)
    chk_ocr_captcha_with_sumit.grid(column=1, row=group_row_count, sticky = W)

    group_row_count+=1

    global ocr_captcha_force_submit_index
    ocr_captcha_force_submit_index = group_row_count

    global lbl_ocr_captcha_force_submit
    lbl_ocr_captcha_force_submit = Label(frame_group_tixcraft, text=translate[language_code]['ocr_captcha_force_submit'])
    lbl_ocr_captcha_force_submit.grid(column=0, row=ocr_captcha_force_submit_index, sticky = E)

    global chk_state_ocr_captcha_force_submit
    chk_state_ocr_captcha_force_submit = BooleanVar()
    chk_state_ocr_captcha_force_submit.set(config_dict['ocr_captcha']["force_submit"])

    global chk_ocr_captcha_force_sumit
    chk_ocr_captcha_force_sumit = Checkbutton(frame_group_tixcraft, text=translate[language_code]['enable'], variable=chk_state_ocr_captcha_force_submit)
    chk_ocr_captcha_force_sumit.grid(column=1, row=group_row_count, sticky = W)

    # final flush.
    global frame_group_tixcraft_index
    frame_group_tixcraft_index = row_count
    #PS: don't need show when onload(), because show/hide block will load again.
    #frame_group_tixcraft.grid(column=0, row=row_count, sticky = W, padx=UI_PADDING_X)

    showHideBlocks()

def AdvancedTab(root, config_dict, language_code, UI_PADDING_X):
    row_count = 0

    frame_group_header = Frame(root)
    group_row_count = 0

    facebook_account = ""
    kktix_account = ""
    play_captcha_sound = False
    captcha_sound_filename = CONST_CAPTCHA_SOUND_FILENAME_DEFAULT
    adblock_plus_enable = False
    line_notify_enable = False
    line_notify_token = ""
    line_notify_message = "成功进入支付页面！请尽快完成付款。"

    if 'advanced' in config_dict:
        facebook_account = config_dict["advanced"]["facebook_account"].strip()
        kktix_account = config_dict["advanced"]["kktix_account"].strip()
        if 'play_captcha_sound' in config_dict["advanced"]:
            if 'enable' in config_dict["advanced"]["play_captcha_sound"]:
                play_captcha_sound = config_dict["advanced"]["play_captcha_sound"]["enable"]
            if 'filename' in config_dict["advanced"]["play_captcha_sound"]:
                captcha_sound_filename = config_dict["advanced"]["play_captcha_sound"]["filename"].strip()
        if 'adblock_plus_enable' in config_dict["advanced"]:
            adblock_plus_enable = config_dict["advanced"]["adblock_plus_enable"]

    if 'line_notify' in config_dict:
        if 'enable' in config_dict["line_notify"]:
            line_notify_enable = config_dict["line_notify"]["enable"]
        if 'token' in config_dict["line_notify"]:
            line_notify_token = config_dict["line_notify"]["token"].strip()
        if 'message' in config_dict["line_notify"]:
            line_notify_message = config_dict["line_notify"]["message"].strip()

    # for kktix
    print("==[advanced]==")
    print("browser", config_dict['browser'])
    print("language", config_dict['language'])
    print("facebook_account", facebook_account)
    print("kktix_account", kktix_account)
    print("play_captcha_sound", play_captcha_sound)
    print("captcha_sound_filename", captcha_sound_filename)
    print("adblock_plus_enable", adblock_plus_enable)

    # assign default value.
    if captcha_sound_filename is None:
        captcha_sound_filename = ""
    if len(captcha_sound_filename)==0:
        captcha_sound_filename = captcha_sound_filename_default


    global lbl_browser
    lbl_browser = Label(frame_group_header, text=translate[language_code]['browser'])
    lbl_browser.grid(column=0, row=group_row_count, sticky = E)

    global combo_browser
    combo_browser = ttk.Combobox(frame_group_header, state="readonly")
    combo_browser['values']= ("chrome","firefox")
    #combo_browser.current(0)
    combo_browser.set(config_dict['browser'])
    combo_browser.grid(column=1, row=group_row_count, sticky = W)

    group_row_count+=1

    global lbl_language
    lbl_language = Label(frame_group_header, text=translate[language_code]['language'])
    lbl_language.grid(column=0, row=group_row_count, sticky = E)

    global combo_language
    combo_language = ttk.Combobox(frame_group_header, state="readonly")
    combo_language['values']= ("English","繁體中文","簡体中文","日本語")
    #combo_language.current(0)
    combo_language.set(config_dict['language'])
    combo_language.bind("<<ComboboxSelected>>", callbackLanguageOnChange)
    combo_language.grid(column=1, row=group_row_count, sticky = W)

    group_row_count +=1

    global lbl_facebook_account
    lbl_facebook_account = Label(frame_group_header, text=translate[language_code]['facebook_account'])
    lbl_facebook_account.grid(column=0, row=group_row_count, sticky = E)

    global txt_facebook_account
    txt_facebook_account_value = StringVar(frame_group_header, value=facebook_account)
    txt_facebook_account = Entry(frame_group_header, width=35, textvariable = txt_facebook_account_value)
    txt_facebook_account.grid(column=1, row=group_row_count, sticky = W)

    group_row_count +=1

    global lbl_kktix_account
    lbl_kktix_account = Label(frame_group_header, text=translate[language_code]['kktix_account'])
    lbl_kktix_account.grid(column=0, row=group_row_count, sticky = E)

    global txt_kktix_account
    txt_kktix_account_value = StringVar(frame_group_header, value=kktix_account)
    txt_kktix_account = Entry(frame_group_header, width=35, textvariable = txt_kktix_account_value)
    txt_kktix_account.grid(column=1, row=group_row_count, sticky = W)

    group_row_count +=1

    global lbl_play_captcha_sound
    lbl_play_captcha_sound = Label(frame_group_header, text=translate[language_code]['play_captcha_sound'])
    lbl_play_captcha_sound.grid(column=0, row=group_row_count, sticky = E)

    global chk_state_play_captcha_sound
    chk_state_play_captcha_sound = BooleanVar()
    chk_state_play_captcha_sound.set(play_captcha_sound)

    global chk_play_captcha_sound
    chk_play_captcha_sound = Checkbutton(frame_group_header, text=translate[language_code]['enable'], variable=chk_state_play_captcha_sound)
    chk_play_captcha_sound.grid(column=1, row=group_row_count, sticky = W)

    group_row_count +=1

    global lbl_captcha_sound_filename
    lbl_captcha_sound_filename = Label(frame_group_header, text=translate[language_code]['captcha_sound_filename'])
    lbl_captcha_sound_filename.grid(column=0, row=group_row_count, sticky = E)

    #print("captcha_sound_filename:", captcha_sound_filename)
    global txt_captcha_sound_filename
    txt_captcha_sound_filename_value = StringVar(frame_group_header, value=captcha_sound_filename)
    txt_captcha_sound_filename = Entry(frame_group_header, width=35, textvariable = txt_captcha_sound_filename_value)
    txt_captcha_sound_filename.grid(column=1, row=group_row_count, sticky = W)

    icon_play_filename = "icon_play_1.gif"
    icon_play_img = PhotoImage(file=icon_play_filename)

    lbl_icon_play = Label(frame_group_header, image=icon_play_img, cursor="hand2")
    lbl_icon_play.image = icon_play_img
    lbl_icon_play.grid(column=3, row=group_row_count)
    lbl_icon_play.bind("<Button-1>", lambda e: btn_preview_sound_clicked())

    group_row_count +=1

    global lbl_adblock_plus
    lbl_adblock_plus = Label(frame_group_header, text=translate[language_code]['adblock_plus_enable'])
    lbl_adblock_plus.grid(column=0, row=group_row_count, sticky = E)

    global chk_state_adblock_plus
    chk_state_adblock_plus = BooleanVar()
    chk_state_adblock_plus.set(adblock_plus_enable)

    global chk_adblock_plus
    chk_adblock_plus = Checkbutton(frame_group_header, text=translate[language_code]['enable'], variable=chk_state_adblock_plus)
    chk_adblock_plus.grid(column=1, row=group_row_count, sticky = W)

    group_row_count +=1

    # 保存登入狀態選項
    save_login_status = False
    if 'save_login_status' in config_dict["advanced"]:
        save_login_status = config_dict["advanced"]["save_login_status"]
    
    global lbl_save_login_status
    lbl_save_login_status = Label(frame_group_header, text=translate[language_code]['save_login_status'])
    lbl_save_login_status.grid(column=0, row=group_row_count, sticky = E)

    global chk_state_save_login_status
    chk_state_save_login_status = BooleanVar()
    chk_state_save_login_status.set(save_login_status)

    global chk_save_login_status
    chk_save_login_status = Checkbutton(frame_group_header, text=translate[language_code]['enable'], variable=chk_state_save_login_status)
    chk_save_login_status.grid(column=1, row=group_row_count, sticky = W)

    group_row_count +=1
    
    lbl_save_login_status_ps = Label(frame_group_header, text='')
    lbl_save_login_status_ps.grid(column=0, row=group_row_count, sticky = E)

    global lbl_save_login_status_memo
    lbl_save_login_status_memo = Label(frame_group_header, text=translate[language_code]['save_login_status_memo'])
    lbl_save_login_status_memo.grid(column=1, row=group_row_count, sticky = W)

    group_row_count +=1

    lbl_adblock_plus_ps = Label(frame_group_header, text='')
    lbl_adblock_plus_ps.grid(column=0, row=group_row_count, sticky = E)

    global lbl_adblock_plus_memo
    lbl_adblock_plus_memo = Label(frame_group_header, text=translate[language_code]['adblock_plus_memo'])
    lbl_adblock_plus_memo.grid(column=1, row=group_row_count, sticky = W)

    group_row_count +=1

    global lbl_adblock_plus_settings
    lbl_adblock_plus_settings = Label(frame_group_header, text=translate[language_code]['adblock_plus_settings'])
    lbl_adblock_plus_settings.grid(column=0, row=group_row_count, sticky = E+N)

    txt_adblock_plus_settings = Text(frame_group_header, width=35, height=6)
    txt_adblock_plus_settings.grid(column=1, row=group_row_count, sticky = W)
    txt_adblock_plus_settings.insert("1.0", CONST_ADBLOCK_PLUS_ADVANCED_FILTER_DEFAULT)

    icon_copy_filename = "icon_copy_2.gif"
    icon_copy_img = PhotoImage(file=icon_copy_filename)

    lbl_icon_copy = Label(frame_group_header, image=icon_copy_img, cursor="hand2")
    lbl_icon_copy.image = icon_copy_img
    lbl_icon_copy.grid(column=3, row=group_row_count, sticky = W+N)
    lbl_icon_copy.bind("<Button-1>", lambda e: btn_copy_clicked())

    frame_group_header.grid(column=0, row=row_count, padx=UI_PADDING_X)

    # LINE Notify 启用/禁用
    global lbl_line_notify
    lbl_line_notify = Label(frame_group_header, text=translate[language_code]['line_notify_enable'])
    lbl_line_notify.grid(column=0, row=group_row_count, sticky = E)

    global chk_state_line_notify
    chk_state_line_notify = BooleanVar()
    chk_state_line_notify.set(line_notify_enable)

    global chk_line_notify
    chk_line_notify = Checkbutton(frame_group_header, text=translate[language_code]['enable'], variable=chk_state_line_notify)
    chk_line_notify.grid(column=1, row=group_row_count, sticky = W)

    group_row_count +=1

    # LINE Notify token
    global lbl_line_notify_token
    lbl_line_notify_token = Label(frame_group_header, text=translate[language_code]['line_notify_token'])
    lbl_line_notify_token.grid(column=0, row=group_row_count, sticky = E)

    global txt_line_notify_token
    txt_line_notify_token_value = StringVar(frame_group_header, value=line_notify_token)
    txt_line_notify_token = Entry(frame_group_header, width=35, textvariable = txt_line_notify_token_value)
    txt_line_notify_token.grid(column=1, row=group_row_count, sticky = W)

    group_row_count +=1

    # LINE Notify 消息文本
    global lbl_line_notify_message
    lbl_line_notify_message = Label(frame_group_header, text=translate[language_code]['line_notify_message'])
    lbl_line_notify_message.grid(column=0, row=group_row_count, sticky = E)

    global txt_line_notify_message
    txt_line_notify_message_value = StringVar(frame_group_header, value=line_notify_message)
    txt_line_notify_message = Entry(frame_group_header, width=35, textvariable = txt_line_notify_message_value)
    txt_line_notify_message.grid(column=1, row=group_row_count, sticky = W)

    group_row_count +=1
    
    # LINE Messaging API区域标题
    line_message_api_title_label = Label(frame_group_header, text="—————— LINE Messaging API ——————")
    line_message_api_title_label.grid(column=0, row=group_row_count, columnspan=2, sticky="ew")
    
    group_row_count +=1
    
    # 获取LINE Messaging API设置
    line_message_api_enable = False
    line_message_api_token = ""
    line_message_api_user_id = ""
    line_message_api_message = "成功进入支付页面！请尽快完成付款。"
    
    if 'line_message_api' in config_dict:
        if 'enable' in config_dict["line_message_api"]:
            line_message_api_enable = config_dict["line_message_api"]["enable"]
        if 'channel_access_token' in config_dict["line_message_api"]:
            line_message_api_token = config_dict["line_message_api"]["channel_access_token"].strip()
        if 'user_id' in config_dict["line_message_api"]:
            line_message_api_user_id = config_dict["line_message_api"]["user_id"].strip()
        if 'message' in config_dict["line_message_api"]:
            line_message_api_message = config_dict["line_message_api"]["message"].strip()
    
    # LINE Messaging API 启用/禁用
    global lbl_line_message_api
    lbl_line_message_api = Label(frame_group_header, text=translate[language_code]['line_message_api_enable'])
    lbl_line_message_api.grid(column=0, row=group_row_count, sticky = E)

    global chk_state_line_message_api
    chk_state_line_message_api = BooleanVar()
    chk_state_line_message_api.set(line_message_api_enable)

    global chk_line_message_api
    chk_line_message_api = Checkbutton(frame_group_header, text=translate[language_code]['enable'], variable=chk_state_line_message_api)
    chk_line_message_api.grid(column=1, row=group_row_count, sticky = W)

    group_row_count +=1

    # LINE Messaging API Channel Access Token
    global lbl_line_message_api_token
    lbl_line_message_api_token = Label(frame_group_header, text=translate[language_code]['line_message_api_channel_access_token'])
    lbl_line_message_api_token.grid(column=0, row=group_row_count, sticky = E)

    global txt_line_message_api_token
    txt_line_message_api_token_value = StringVar(frame_group_header, value=line_message_api_token)
    txt_line_message_api_token = Entry(frame_group_header, width=35, textvariable = txt_line_message_api_token_value)
    txt_line_message_api_token.grid(column=1, row=group_row_count, sticky = W)

    group_row_count +=1

    # LINE Messaging API User ID / Group ID
    global lbl_line_message_api_user_id
    lbl_line_message_api_user_id = Label(frame_group_header, text=translate[language_code]['line_message_api_user_id'])
    lbl_line_message_api_user_id.grid(column=0, row=group_row_count, sticky = E)

    global txt_line_message_api_user_id
    txt_line_message_api_user_id_value = StringVar(frame_group_header, value=line_message_api_user_id)
    txt_line_message_api_user_id = Entry(frame_group_header, width=35, textvariable = txt_line_message_api_user_id_value)
    txt_line_message_api_user_id.grid(column=1, row=group_row_count, sticky = W)

    group_row_count +=1

    # LINE Messaging API 消息文本
    global lbl_line_message_api_message
    lbl_line_message_api_message = Label(frame_group_header, text=translate[language_code]['line_message_api_message'])
    lbl_line_message_api_message.grid(column=0, row=group_row_count, sticky = E)

    global txt_line_message_api_message
    txt_line_message_api_message_value = StringVar(frame_group_header, value=line_message_api_message)
    txt_line_message_api_message = Entry(frame_group_header, width=35, textvariable = txt_line_message_api_message_value)
    txt_line_message_api_message.grid(column=1, row=group_row_count, sticky = W)

    group_row_count +=1
    
    # 添加LINE Messaging API測試按鈕
    global btn_test_line_message_api
    btn_test_line_message_api = ttk.Button(frame_group_header, text=translate[language_code]['test_send'], command=lambda: btn_test_line_messaging_api_clicked(language_code))
    btn_test_line_message_api.grid(column=1, row=group_row_count, sticky = W)
    
    group_row_count +=1
    
    # 添加LINE Messaging API说明
    line_notify_end_message = {
        'zh_tw': "LINE Notify將於2025年3月31日停止服務，建議改用LINE Messaging API",
        'zh_cn': "LINE Notify将于2025年3月31日停止服务，建议改用LINE Messaging API",
        'en_us': "LINE Notify will stop service on March 31, 2025. LINE Messaging API is recommended instead.",
        'ja_jp': "LINE Notifyは2025年3月31日にサービスを終了します。LINE Messaging APIの使用をお勧めします。"
    }
    
    line_message_api_notice = Label(frame_group_header, text=line_notify_end_message.get(language_code, line_notify_end_message['en_us']), fg="red")
    line_message_api_notice.grid(column=0, row=group_row_count, columnspan=2, sticky="ew")
    
    group_row_count +=1
    
    # 添加LINE Messaging API使用说明
    line_guide_message = {
        'zh_tw': "獲取Channel Access Token和User ID指南:",
        'zh_cn': "获取Channel Access Token和User ID指南:",
        'en_us': "Guide to get Channel Access Token and User ID:",
        'ja_jp': "Channel Access TokenとUser IDを取得するガイド:"
    }
    
    line_message_api_help = Label(frame_group_header, text=line_guide_message.get(language_code, line_guide_message['en_us']), fg="blue", cursor="hand2")
    line_message_api_help.grid(column=0, row=group_row_count, columnspan=2, sticky="w")
    line_message_api_help.bind("<Button-1>", lambda e: open_url("https://developers.line.biz/en/docs/messaging-api/getting-started/"))
    
    group_row_count +=1

    global lbl_slogan
    global lbl_help
    global lbl_donate
    global lbl_release

    # lbl_slogan = Label(frame_group_header, text=translate[language_code]['maxbot_slogan'], wraplength=400, justify="center")
    # lbl_slogan.grid(column=0, row=group_row_count, columnspan=2)

    # group_row_count +=1

    # lbl_help = Label(frame_group_header, text=translate[language_code]['help'])
    # lbl_help.grid(column=0, row=group_row_count, sticky = E)

    # lbl_help_url = Label(frame_group_header, text=URL_HELP, fg="blue", cursor="hand2")
    # lbl_help_url.grid(column=1, row=group_row_count, sticky = W)
    # lbl_help_url.bind("<Button-1>", lambda e: open_url(URL_HELP))

    # group_row_count +=1

    # lbl_donate = Label(frame_group_header, text=translate[language_code]['donate'])
    # lbl_donate.grid(column=0, row=group_row_count, sticky = E)

    # lbl_donate_url = Label(frame_group_header, text=URL_DONATE, fg="blue", cursor="hand2")
    # lbl_donate_url.grid(column=1, row=group_row_count, sticky = W)
    # lbl_donate_url.bind("<Button-1>", lambda e: open_url(URL_DONATE))

    # group_row_count +=1

    # lbl_release = Label(frame_group_header, text=translate[language_code]['release'])
    # lbl_release.grid(column=0, row=group_row_count, sticky = E)

    # lbl_release_url = Label(frame_group_header, text=URL_RELEASE, fg="blue", cursor="hand2")
    # lbl_release_url.grid(column=1, row=group_row_count, sticky = W)
    # lbl_release_url.bind("<Button-1>", lambda e: open_url(URL_RELEASE))

    # group_row_count +=1

    # lbl_fb_fans = Label(frame_group_header, text=u'Facebook')
    # lbl_fb_fans.grid(column=0, row=group_row_count, sticky = E)

    # lbl_fb_fans_url = Label(frame_group_header, text=URL_FB, fg="blue", cursor="hand2")
    # lbl_fb_fans_url.grid(column=1, row=group_row_count, sticky = W)
    # lbl_fb_fans_url.bind("<Button-1>", lambda e: open_url(URL_FB))

    frame_group_header.grid(column=0, row=row_count)

def AboutTab(root, language_code):
    frame_group_header = Frame(root)
    group_row_count = 0

    logo_filename = "maxbot_logo2_single.ppm"
    try:
        logo_img = PhotoImage(file=logo_filename)
        lbl_logo = Label(frame_group_header, image=logo_img)
        lbl_logo.image = logo_img
        lbl_logo.grid(column=0, row=group_row_count, columnspan=2)
    except Exception as exc:
        pass
    
    group_row_count += 1
    
    lbl_app_name = Label(frame_group_header, text=CONST_APP_VERSION, font=("Helvetica", 16))
    lbl_app_name.grid(column=0, row=group_row_count, columnspan=2)
    
    group_row_count += 1
    
    lbl_copyright = Label(frame_group_header, text="Copyright (c) 2018-2023")
    lbl_copyright.grid(column=0, row=group_row_count, columnspan=2)
    
    group_row_count += 1
    
    lbl_help = Label(frame_group_header, text=translate[language_code]['help'])
    lbl_help.grid(column=0, row=group_row_count, sticky = E)

    lbl_help_url = Label(frame_group_header, text=URL_HELP, fg="blue", cursor="hand2")
    lbl_help_url.grid(column=1, row=group_row_count, sticky = W)
    lbl_help_url.bind("<Button-1>", lambda e: open_url(URL_HELP))
    
    group_row_count += 1
    
    lbl_donate = Label(frame_group_header, text=translate[language_code]['donate'])
    lbl_donate.grid(column=0, row=group_row_count, sticky = E)

    lbl_donate_url = Label(frame_group_header, text=URL_DONATE, fg="blue", cursor="hand2")
    lbl_donate_url.grid(column=1, row=group_row_count, sticky = W)
    lbl_donate_url.bind("<Button-1>", lambda e: open_url(URL_DONATE))
    
    frame_group_header.grid(column=0, row=0, padx=UI_PADDING_X)

def get_action_bar(root, language_code):
    frame_action = Frame(root)

    global btn_run
    global btn_save
    global btn_exit
    global btn_restore_defaults

    btn_run = ttk.Button(frame_action, text=translate[language_code]['run'], command= lambda: btn_run_clicked(language_code))
    btn_run.grid(column=0, row=0)

    btn_save = ttk.Button(frame_action, text=translate[language_code]['save'], command= lambda: btn_save_clicked(language_code) )
    btn_save.grid(column=1, row=0)

    btn_exit = ttk.Button(frame_action, text=translate[language_code]['exit'], command=btn_exit_clicked)
    #btn_exit.grid(column=2, row=0)

    btn_restore_defaults = ttk.Button(frame_action, text=translate[language_code]['restore_defaults'], command= lambda: btn_restore_defaults_clicked(language_code))
    btn_restore_defaults.grid(column=2, row=0)

    return frame_action

def clearFrame(frame):
    # destroy all widgets from frame
    for widget in frame.winfo_children():
       widget.destroy()

def load_GUI(root, config_dict):
    clearFrame(root)

    language_code="en_us"
    if not config_dict is None:
        if u'language' in config_dict:
            language_code = get_language_code_by_name(config_dict["language"])

    row_count = 0

    global tabControl
    tabControl = ttk.Notebook(root)
    tab1 = Frame(tabControl)
    tabControl.add(tab1, text=translate[language_code]['preference'])
    tab2 = Frame(tabControl)
    tabControl.add(tab2, text=translate[language_code]['advanced'])
    tab3 = Frame(tabControl)
    tabControl.add(tab3, text=translate[language_code]['about'])
    tabControl.grid(column=0, row=row_count)
    tabControl.select(tab1)

    row_count+=1

    frame_action = get_action_bar(root, language_code)
    frame_action.grid(column=0, row=row_count)

    global UI_PADDING_X
    PreferenctTab(tab1, config_dict, language_code, UI_PADDING_X)
    AdvancedTab(tab2, config_dict, language_code, UI_PADDING_X)
    AboutTab(tab3, language_code)

def main():
    global translate
    # only need to load translate once.
    translate = load_translate()

    global root
    root = Tk()
    root.title(CONST_APP_VERSION)
    
    # 設置窗口大小並允許調整大小
    root.geometry("600x680")
    root.minsize(550, 600)
    
    # for icon.
    icon_filepath = __file__.split("settings.py")[0] + "icon.ico"
    if os.path.exists(icon_filepath):
        try:
            root.iconbitmap(icon_filepath)
        except Exception as exc:
            pass

    global config_filepath
    global config_dict
    global combo_homepage

    # initial variables.
    # for saved password usage.
    config_filepath, config_dict = load_json()

    load_GUI(root, config_dict)
    root.mainloop()

if __name__ == "__main__":
    main()
