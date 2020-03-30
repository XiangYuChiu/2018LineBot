from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('hXgcnkaAxXj4+xTcmEOZCVrU8Pwk5kS9qiB6gJX7msIlOYJkwTO4bFzh2lgFgbdnROSB3apQGarvQS6REB+JDANY1CUuL82RFEORBleo1Ogi3OJzsQZSK8fhTZIr//BQ8CVSdxrT25otDcm/hqsVBgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('338644819138a86bd22b88b740255b03')

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
def handle_message(event):
    if (event.message.text == '123'):   #獲取測試訊息
        replymessage = ('234')          #設定回復訊息(replymessage)
    elif(event.message.text == 'Wifi'): 
        replymessage = (' ASUS-RT51U: \n Password: d0645758\n\n dlink-F392:\n Password: 51232960\n\n ASUS_Zenfone3:\n Password: D0645758\n')  
    elif(event.message.text == '生存場地'):
        counter = 0
        while(counter<=2):
            if(counter == 1):
                replymessage = ('各場地資料彙整\n場地地圖 https://goo.gl/dV8xwq\n各場地資料彙整如下\n\n')
            elif(counter == 2):
                replymessage = ('山湖戰術中心\n官網:  https://www.facebook.com/hillfoxtacticsCenter/\n導航直接搜尋 山狐戰術中心\n收費場 半天200/人 全天300/人')
        #溪湖戰役\n官網:  https://www.facebook.com/XIHUAirsoftWar/\nGoogle 導航溪湖戰役即可\n收費場 入場費平日200/人 假日300/人 \n有販賣飲料/出租裝備\n\n
        #烏日橋下\n地址:  https://goo.gl/maps/6eFPrSx4AU42\n橋下鐵絲網後就是活動場地 為免費場地\n可走筏子溪東街或新鎮和路再轉至橋下\n請禮讓偶爾出現的工程車在那邊施工\n\n
        #春田惡魔島\n官網:  https://goo.gl/E4gPqY\n導航” 春田惡魔島” 或東山樂園再往上一點\n收費場 250/人\n有販賣簡單的飲料\n\n
        #大甲野戰場\n地址：台中市大甲區同安里中山路二段1195巷32號\n導航：台中市大甲區長壽東西七路（靠近省道\n收費場 150/人\n\n
        #清水66眷村\nGoogle導航至”港區藝術中心”\n在鎮政路、鱉峰路380巷與藝術街所圍起來的廢棄房區\n入口須從農田靠近鱉峰路380巷的缺口進去\n***為軍方土地，進去遊玩請保持低調****\n\n
        #台灣民俗村\n官網: https://www.facebook.com/TFV.gun/\n導航請搜尋”日華大飯店”\n入場費 150/人\n\n
        #JEA共同決戰區生存遊戲訓練基地\n網址 https://www.facebook.com/jea.shootingclub/\n地址 苗栗縣後龍鎮龍坑里十班坑172號\n收費場 半天200/人 有提供裝備出借\n\n
        #南投千秋戰場\n網址:  https://www.facebook.com/groups/299470600702193/?fref=nf\n地址;  南投市千秋里菓稟路3號\n收費場 100/人/半天\n\n
            counter += 1
            message = TextSendMessage(text=replymessage)               #將回復訊息(replymessage)輸入LINE BOT(message)
            line_bot_api.reply_message(event.reply_token, message)     #LINE BOT回復訊息
        
    message = TextSendMessage(text=replymessage)               #將回復訊息(replymessage)輸入LINE BOT(message)
    line_bot_api.reply_message(event.reply_token, message)     #LINE BOT回復訊息
#######################################################################
if __name__ == "__main__":
    app.run()
    
