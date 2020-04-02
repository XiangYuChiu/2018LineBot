from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import os

ToolManAC = os.environ.get('ToolManAC')
ToolManPW = os.environ.get('ToolManPW')

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi(ToolManAC)
# Channel Secret
handler = WebhookHandler(ToolManPW)

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'
######################################################################
# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
@app.route("/ConfirmTemplate/")
def handle_message(event):
    reply_arr=[]
    if (event.message.text == '123'):   #獲取測試訊息
        reply_arr.append(TextSendMessage(text='第一則文字訊息') )
        reply_arr.append(TextSendMessage(text='第二則回復訊息') )
    elif(event.message.text == 'Wifi'): 
        reply_arr.append(TextSendMessage(text='ASUS-RT51U: \nPassword: d0645758\n\ndlink-F392:\nPassword: 51232960\n\nASUS_Zenfone3:\nPassword: D0645758\n'))
    elif(event.message.text == '生存場地'):
        reply_arr.append(TextSendMessage(text='各場地資料彙整\n場地地圖 https://goo.gl/dV8xwq\n各場地資料彙整如下\n\n'))
        reply_arr.append(TextSendMessage(text='山湖戰術中心\n官網:  https://www.facebook.com/hillfoxtacticsCenter/\n導航直接搜尋 山狐戰術中心\n收費場 半天200/人 全天300/人溪湖戰役\n官網:  https://www.facebook.com/XIHUAirsoftWar/\nGoogle 導航溪湖戰役即可\n收費場 入場費平日200/人 假日300/人 \n有販賣飲料/出租裝備\n\n'))
        reply_arr.append(TextSendMessage(text='烏日橋下\n地址:  https://goo.gl/maps/6eFPrSx4AU42\n橋下鐵絲網後就是活動場地 為免費場地\n可走筏子溪東街或新鎮和路再轉至橋下\n請禮讓偶爾出現的工程車在那邊施工\n\n春田惡魔島\n官網:  https://goo.gl/E4gPqY\n導航” 春田惡魔島” 或東山樂園再往上一點\n收費場 250/人\n有販賣簡單的飲料\n\n大甲野戰場\n地址：台中市大甲區同安里中山路二段1195巷32號\n導航：台中市大甲區長壽東西七路（靠近省道\n收費場 150/人\n\n清水66眷村\nGoogle導航至”港區藝術中心”\n在鎮政路、鱉峰路380巷與藝術街所圍起來的廢棄房區\n入口須從農田靠近鱉峰路380巷的缺口進去\n***為軍方土地，進去遊玩請保持低調****\n\n'))
        reply_arr.append(TextSendMessage(text='台灣民俗村\n官網: https://www.facebook.com/TFV.gun/\n導航請搜尋”日華大飯店”\n入場費 150/人\n\nJEA共同決戰區生存遊戲訓練基地\n網址 https://www.facebook.com/jea.shootingclub/\n地址 苗栗縣後龍鎮龍坑里十班坑172號\n收費場 半天200/人 有提供裝備出借\n\n南投千秋戰場\n網址:  https://www.facebook.com/groups/299470600702193/?fref=nf\n地址;  南投市千秋里菓稟路3號\n收費場 100/人/半天\n\n'))
    elif(event.message.text == '生存地圖'):
        reply_arr.append(TextSendMessage(text='台中生存遊戲 Google Map: https://goo.gl/dV8xwq'))
    elif(event.message.text == '槍店'):
        reply_arr.append(TextSendMessage(text='KUI 酷愛生存遊戲專賣 - 台中總店\n地址： 406台中市北屯區軍功路一段243-1號\n營業時間:13:00~21:30\n電話： 04-24376402\n露天:https://www.ruten.com.tw/user/index00.php?s=paymy168\n\nKUI 酷愛生存遊戲專賣 - 台中西屯店\n地址： 407台中市西屯區福雅路335號\n營業時間:13:00~21:30\n電話：04-24653131\n\n'))
        reply_arr.append(TextSendMessage(text='IDCF艾利斯生存遊戲工作坊台中店\n地址： 407台中市西屯區西屯路二段上石北二巷15號 地下一樓\n營業時間:13:30~22:30\n電話： 04-24522047\n露天:https://www.ruten.com.tw/user/index00.php?s=sky19840716\n\n'))
        reply_arr.append(TextSendMessage(text='翔準生存遊戲專賣\n地址:508彰化縣和美鎮彰新路二段479號\n營業時間:12:00~22:00\n電話:04-7353481\n官網:https://www.aog.com.tw/\n露天賣場1:https://www.ruten.com.tw/user/index00.php?s=zzzlin8899\n露天賣場2:https://www.ruten.com.tw/user/index00.php?s=and888999\n\nBCS武器空間生存遊戲專賣 台中美村店\n地址:403台中市西區美村路一段109號\n營業時間:13:00~22:00\n電話:04-23269483\n露天:https://www.ruten.com.tw/user/index00.php?s=bcsbcs\n\nBCS武器空間生存遊戲專賣-台中NOVA英才店\n地址:403台中市西區英才路508號2號2樓241櫃位\n營業時間:11:00~21:30\n電話:04-23293192\n\n金和勝玩具-西屯店\n地址:407台中市西屯區西屯路三段79-8號\n營業時間14:00~22:00\n電話:04-24511795\n露天:https://www.ruten.com.tw/user/index00.php?s=a400258\n\n金和勝玩具-彰化店\n地址:500彰化縣彰化市中央路9號\n電話:04-7621300\n\n'))
        reply_arr.append(TextSendMessage(text='BCS武器空間生存遊戲專賣 台中美村店\n地址:403台中市西區美村路一段109號\n營業時間:13:00~22:00\n電話:04-23269483\n露天:https://www.ruten.com.tw/user/index00.php?s=bcsbcs\n\nBCS武器空間生存遊戲專賣-台中NOVA英才店\n地址:403台中市西區英才路508號2號2樓241櫃位\n營業時間:11:00~21:30\n電話:04-23293192\n\n'))
        reply_arr.append(TextSendMessage(text='金和勝玩具-西屯店\n地址:407台中市西屯區西屯路三段79-8號\n營業時間14:00~22:00\n電話:04-24511795\n露天:https://www.ruten.com.tw/user/index00.php?s=a400258\n\n金和勝玩具-彰化店\n地址:500彰化縣彰化市中央路9號\n電話:04-7621300\n\n'))
    elif(event.message.text == '推廣'):
        reply_arr.append(TemplateSendMessage(
            alt_text = '推廣查詢(請用手機操作)',  # 當你發送到你的Line bot 群組的時候，通知的名稱
            template = ButtonsTemplate(
                thumbnail_image_url = 'https://i.imgur.com/6Rj7CIx.jpg',  # 你的按鈕模板的圖片是什麼
                title = '推廣的各位大家好\n請問要啥哪間教室的電腦資訊呢?',  # 你的標題名稱
                text = '請選擇你要的項目：',  # 應該算是一個副標題
                # 下面主要就是你希望使用者點擊了按鈕會有哪些動作，最多只能有四個action！超過會報錯喔！
                actions = [
                    # 說真的這個我不知道要幹嘛用，可能後台可以收數據？我點了就回應我 postback text，至於data我就不熟了
                    PostbackAction(
                        label = '商502',  # 在按鈕模板上顯示的名稱
                        text = '商502',  # 點擊會顯示的文字
                        data = 'action=buy&itemid=1'  # 這個...我真的就不知道了～
                    ),
                    # 跟上面差不多
                    MessageAction(
                        label = '商108',   # 在按鈕模板上顯示的名稱
                        text = '108',  # 點擊會顯示的文字
                    )
                ]
            )
         ))
    elif(event.message.text == '商502'):
        reply_arr.append(TemplateSendMessage(
            alt_text = '商502查詢(請用手機操作)',  # 當你發送到你的Line bot 群組的時候，通知的名稱
            template = ButtonsTemplate(
                thumbnail_image_url = 'https://i.imgur.com/I5wvD3u.jpg',  # 你的按鈕模板的圖片是什麼
                title = '商502',  # 你的標題名稱
                text = '請選擇你要的項目：',  # 應該算是一個副標題
                # 下面主要就是你希望使用者點擊了按鈕會有哪些動作，最多只能有四個action！超過會報錯喔！
                actions = [
                    # 說真的這個我不知道要幹嘛用，可能後台可以收數據？我點了就回應我 postback text，至於data我就不熟了
                    PostbackAction(
                        label = '導師機',  # 在按鈕模板上顯示的名稱
                        text = '商502導師機',  # 點擊會顯示的文字
                        data = 'action=buy&itemid=1'  # 這個...我真的就不知道了～
                    ),
                    # 跟上面差不多
                    MessageAction(
                        label = '學生機',   # 在按鈕模板上顯示的名稱
                        text = '商502學生機',  # 點擊會顯示的文字
                    ),
                    MessageAction(
                        label = '3D列印機',   # 在按鈕模板上顯示的名稱
                        text = '3D列印機',  # 點擊會顯示的文字
                    ),
                    MessageAction(
                        label = '雜物',
                        text = '商502電腦周邊雜物',
                    )
                ]
            )
        ))
    elif(event.message.text == '商502導師機'):
        reply_arr.append(TemplateSendMessage(
            alt_text = '商502導師機查詢(請用手機操作)',  # 當你發送到你的Line bot 群組的時候，通知的名稱
            template = ButtonsTemplate(
                thumbnail_image_url = 'https://i.imgur.com/TBcAqsh.jpg',  # 你的按鈕模板的圖片是什麼
                title = '商502導師機查詢',  # 你的標題名稱
                text = '請選擇你要的項目：',  # 應該算是一個副標題
                # 下面主要就是你希望使用者點擊了按鈕會有哪些動作，最多只能有四個action！超過會報錯喔！
                actions = [
                    # 說真的這個我不知道要幹嘛用，可能後台可以收數據？我點了就回應我 postback text，至於data我就不熟了
                    PostbackAction(
                        label = '程式項目',  # 在按鈕模板上顯示的名稱
                        text = '商502導師機程式項目',  # 點擊會顯示的文字
                        data = 'action=buy&itemid=1'  # 這個...我真的就不知道了～
                    ),
                    # 跟上面差不多
                    MessageAction(
                        label = '系統資訊',   # 在按鈕模板上顯示的名稱
                        text = '商502導師機系統資訊',  # 點擊會顯示的文字
                    ),
                    MessageAction(
                        label = '故障資訊',   # 在按鈕模板上顯示的名稱
                        text = '商502導師機故障資訊',  # 點擊會顯示的文字
                    ),
                    MessageAction(
                        label = '回到推廣首頁',
                        text = '推廣',
                    )
                ]
            )
        ))
     elif(event.message.text == '商502學生機'):
        reply_arr.append(TemplateSendMessage(
            alt_text = '商502學生機查詢(請用手機操作)',  # 當你發送到你的Line bot 群組的時候，通知的名稱
            template = ButtonsTemplate(
                thumbnail_image_url = 'https://i.imgur.com/lh0w50B.jpg',  # 你的按鈕模板的圖片是什麼
                title = '商502學生機查詢',  # 你的標題名稱
                text = '請選擇你要的項目：',  # 應該算是一個副標題
                # 下面主要就是你希望使用者點擊了按鈕會有哪些動作，最多只能有四個action！超過會報錯喔！
                actions = [
                    # 說真的這個我不知道要幹嘛用，可能後台可以收數據？我點了就回應我 postback text，至於data我就不熟了
                    PostbackAction(
                        label = '程式項目',  # 在按鈕模板上顯示的名稱
                        text = '商502學生機程式項目',  # 點擊會顯示的文字
                        data = 'action=buy&itemid=1'  # 這個...我真的就不知道了～
                    ),
                    # 跟上面差不多
                    MessageAction(
                        label = '系統資訊',   # 在按鈕模板上顯示的名稱
                        text = '商502學生機系統資訊',  # 點擊會顯示的文字
                    ),
                    MessageAction(
                        label = '故障資訊',   # 在按鈕模板上顯示的名稱
                        text = '商502學生機故障資訊',  # 點擊會顯示的文字
                    ),
                    MessageAction(
                        label = '回到推廣首頁',
                        text = '推廣',
                    )
                ]
            )
        ))
    elif(event.message.text == '3D列印機'):
        reply_arr.append(TemplateSendMessage(
            alt_text = '3D列印機查詢(請用手機操作)',  # 當你發送到你的Line bot 群組的時候，通知的名稱
            template = ButtonsTemplate(
                thumbnail_image_url = 'https://i.imgur.com/0QBHMrg.jpg',  # 你的按鈕模板的圖片是什麼
                title = '3D列印機查詢',  # 你的標題名稱
                text = '請選擇你要的項目：',  # 應該算是一個副標題
                # 下面主要就是你希望使用者點擊了按鈕會有哪些動作，最多只能有四個action！超過會報錯喔！
                actions = [
                    # 說真的這個我不知道要幹嘛用，可能後台可以收數據？我點了就回應我 postback text，至於data我就不熟了
                    PostbackAction(
                        label = '程式項目',  # 在按鈕模板上顯示的名稱
                        text = '商502學生機程式項目',  # 點擊會顯示的文字
                        data = 'action=buy&itemid=1'  # 這個...我真的就不知道了～
                    ),
                    # 跟上面差不多
                    MessageAction(
                        label = '系統資訊',   # 在按鈕模板上顯示的名稱
                        text = '商502學生機系統資訊',  # 點擊會顯示的文字
                    ),
                    MessageAction(
                        label = '故障資訊',   # 在按鈕模板上顯示的名稱
                        text = '商502學生機故障資訊',  # 點擊會顯示的文字
                    ),
                    MessageAction(
                        label = '回到推廣首頁',
                        text = '推廣',
                    )
                ]
            )
        ))
    
    line_bot_api.reply_message(event.reply_token,reply_arr)     #LINE BOT回復訊息
#######################################################################
if __name__ == "__main__":
    app.run()
    
