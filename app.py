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
        replymessage = ('234')               #設定回復訊息(replymessage)
    message = TextSendMessage(text=replymessage)               #將回復訊息(replymessage)輸入LINE BOT(message)
    #line_bot_api.reply_message(event.reply_token, message)     #LINE BOT回復訊息
    
    if(wven.message.text == '2'):
        message = ImagemapSendMessage(
        base_url='https://example.com/base',
        alt_text='this is an imagemap',
        base_size=BaseSize(height=1040, width=1040),
        actions=[
            URIImagemapAction(
                link_uri='https://example.com/',
            )
                area=ImagemapArea(x=0, y=0, width=520, height=1040)
            MessageImagemapAction(
                text='hello',
                area=ImagemapArea(x=520, y=0, width=520, height=1040)
            )
    line_bot_api.reply_message(event.reply_token, message)
#######################################################################
if __name__ == "__main__":
    app.run()
    
