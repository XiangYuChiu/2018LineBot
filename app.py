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

# 處理訊息
#@handler.add(MessageEvent, message=TextMessage)
#def handle_message(event):
    #if get message == ("測試")
 #   message = TextSendMessage(text=event.message.text)
  #  line_bot_api.reply_message(event.reply_token, message)

#if __name__ == "__main__":
 #   app.run()
    
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):                              #預設獲取使用者文字
    get = event.message.tex
#########################################################################################
if (get == '1)
    message = TextSendMessage(text='Hello, world')
    line_bot_api.reply_message(event.reply_token, message)  #回覆訊息
#########################################################################################
if __name__ == "__main__":                              #結束robot 
    #port = int(os.environ.get('PORT', 5000))
    app.run()#host='0.0.0.0', port=port)
