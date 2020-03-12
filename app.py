from flask import Flask, request, abort



from linebot import (

    LineBotApi, WebhookHandler

)

from linebot.exceptions import (

    InvalidSignatureError

)

from linebot.models import *



import random







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

@handler.add(MessageEvent, message=TextMessage)

def handle_message(event):

    get = event.message.text

#event.gessage.text接收使用者文字訊息



#############################################

#回傳文字訊息

    if(get == '幹'):

        message = TextSendMessage(text = '怕.jpg')

    if(get == '啾'):

        message = TextSendMessage(text = '啾~❤')

    if(get == '誌誌帥嗎'):

        message = TextSendMessage(text = '好帥帥~ 幽默又可愛 喜歡❤')

    if(get == '祥育!' or get == '祥育！'):

        message = TextSendMessage(text = '帥帥帥帥')

    if(get == '不知道'):

        message = TextSendMessage(text = '我也不知道')

    if(get == 'ASUS-RT51U' or get == 'ASUS-RT51U_5G'):

        message = TextSendMessage(text = 'Password : D0645758')

    if(get == '飲料骰子'):

        result = random.randint(0, 5)

        if(result == 0):

            message = TextSendMessage(text = '超商飲料')

        if(result == 1):

            message = TextSendMessage(text = '你他媽不會喝水嘛?')

        if(result == 2):

            message = TextSendMessage(text = '迷迷迷客夏')

        if(result == 3):

            message = TextSendMessage(text = '喝清心好開心')

        if(result == 4):

            message = TextSendMessage(text = '來個五十杯五十嵐')

        if(result > 4):

            message = TextSendMessage(text = '圓石來電')

    if(get == '逢甲肚子餓'):

        result = random.randint(0, 22)

        if(result == 0):

            message = TextSendMessage(text = '超商食品')

        if(result == 1):

            message = TextSendMessage(text = '甲賽')

        if(result == 2):

            message = TextSendMessage(text = '好而大居酒屋')

        if(result == 3):

            message = TextSendMessage(text = '隨義煮')

        if(result == 4):

            message = TextSendMessage(text = '來來魯肉飯')

        if(result == 5):

            message = TextSendMessage(text = '職人牛排')

        if(result == 6):

            message = TextSendMessage(text = '六扇門')

        if(result == 7):

            message = TextSendMessage(text = '九湯屋')

        if(result == 8):

            message = TextSendMessage(text = '七味廚坊')

        if(result == 9):

            message = TextSendMessage(text = '豐成麵館')

        if(result == 10):

            message = TextSendMessage(text = '吉蜂蒸餃')

        if(result == 11):

            message = TextSendMessage(text = '八方雲集')

        if(result == 12):

            message = TextSendMessage(text = '大丁拉麵')

        if(result == 13):

            message = TextSendMessage(text = '九州拉麵')

        if(result == 14):

            message = TextSendMessage(text = '黑盒子')

        if(result == 15):

            message = TextSendMessage(text = '擄胃專家')

        if(result == 16):

            message = TextSendMessage(text = '吉野烤肉飯')

        if(result == 17):

            message = TextSendMessage(text = '紅辣椒')

        if(result == 18):

            message = TextSendMessage(text = '小辣椒')

        if(result == 19):

            message = TextSendMessage(text = '麥當勞')

        if(result == 20):

            message = TextSendMessage(text = '鴨樓鴨肉飯')

        if(result == 21):

            message = TextSendMessage(text = '泡麵')

        if(result > 21):

            message = TextSendMessage(text = '粥遊天下')



#############################################

#回傳圖片訊息

    if(get == '呱呱抽' or get == '呱呱呱'):

        get = '雨林抽'

    if(get == '庭庭抽'):

        message = ImageSendMessage(

            original_content_url='https://i.imgur.com/fTlDhKn.jpg',

            preview_image_url='https://i.imgur.com/fTlDhKn.jpg'

        )

    if(get == '庭婆抽'):

        message = ImageSendMessage(

            original_content_url='https://i.imgur.com/RyhdOXR.jpg',

            preview_image_url='https://i.imgur.com/RyhdOXR.jpg'

        )

    if(get == '嘿咻熊抽'):

        message = ImageSendMessage(

            original_content_url='https://i.imgur.com/mvfWWLw.jpg',

            preview_image_url='https://i.imgur.com/mvfWWLw.jpg'

        )

    if(get == '剛剛在Dcard看到一個可愛der女森'):

        message = ImageSendMessage(

            original_content_url='https://i.imgur.com/bc7Oig5.jpg',

            preview_image_url='https://i.imgur.com/bc7Oig5.jpg'

        )

    if(get == '黑人問號'):

        message = ImageSendMessage(

            original_content_url='https://i.imgur.com/zTOnfAi.jpg',

            preview_image_url='https://i.imgur.com/zTOnfAi.jpg'

        )

    if(get == '淳羽覺得很驚訝'):

        message = ImageSendMessage(

            original_content_url='https://i.imgur.com/KjfihNR.jpg',

            preview_image_url='https://i.imgur.com/KjfihNR.jpg'

        )

    if(get == '科學社社長抽' or get == '晴天抽'):

        message = ImageSendMessage(

            original_content_url='https://i.imgur.com/Cd2eUnx.jpg',

            preview_image_url='https://i.imgur.com/Cd2eUnx.jpg'

        )

    if(get == '劉德滑抽'):

        message = ImageSendMessage(

            original_content_url='https://i.imgur.com/sXXJq48.jpg',

            preview_image_url='https://i.imgur.com/sXXJq48.jpg'

        )

    if(get == '程程抽'):

        message = ImageSendMessage(

            original_content_url='https://i.imgur.com/dcO8RVL.jpg',

            preview_image_url='https://i.imgur.com/dcO8RVL.jpg'

        )

    if(get == '無疑王玉抽'):

        message = ImageSendMessage(

            original_content_url='https://i.imgur.com/KiodYrk.jpg',

            preview_image_url='https://i.imgur.com/KiodYrk.jpg'

        )

    if(get == '+淳抽'):

        message = ImageSendMessage(

            original_content_url='https://i.imgur.com/IksKVP1.jpg',

            preview_image_url='https://i.imgur.com/IksKVP1.jpg'

        )

    if(get == '阿祥抽'):

        message = ImageSendMessage(

            original_content_url='https://i.imgur.com/ZIjyjuI.jpg',

            preview_image_url='https://i.imgur.com/ZIjyjuI.jpg'

        )

    if(get == '癡漢二人組'):

        message = ImageSendMessage(

            original_content_url='https://i.imgur.com/FabmRZg.jpg',

            preview_image_url='https://i.imgur.com/FabmRZg.jpg'

        )

    if(get == '阿倩仔抽'):

        result = random.randint(0, 1)

        if(result == 0):

            message = ImageSendMessage(

                original_content_url='https://i.imgur.com/vi3VuEx.jpg',

                preview_image_url='https://i.imgur.com/vi3VuEx.jpg'

            )

        if(result > 0):

            message = ImageSendMessage(

                original_content_url='https://i.imgur.com/PTMT6fO.jpg',

                preview_image_url='https://i.imgur.com/PTMT6fO.jpg'

            )

    if(get == '雨林抽'):

        result = random.randint(0, 1)

        if(result == 0):

            message = ImageSendMessage(

                original_content_url='https://i.imgur.com/dsmxnc8.jpg',

                preview_image_url='https://i.imgur.com/dsmxnc8.jpg'

            )

        if(result > 0):

            message = ImageSendMessage(

                original_content_url='https://i.imgur.com/UN5J92A.jpg',

                preview_image_url='https://i.imgur.com/UN5J92A.jpg'

            )

    if(get == '誌誌抽'):

        message = ImageSendMessage(

            original_content_url='https://i.imgur.com/tslkGF3.jpg',

            preview_image_url='https://i.imgur.com/tslkGF3.jpg'

        )

    if(get == '唇語抽' or get == '脣語抽'):

        result = random.randint(0, 4)

        if(result == 0):

            message = ImageSendMessage(

                original_content_url='https://i.imgur.com/mDAHeVc.jpg',

                preview_image_url='https://i.imgur.com/mDAHeVc.jpg'

            )

        if(result == 1):

            message = ImageSendMessage(

                original_content_url='https://i.imgur.com/sEM6T0o.jpg',

                preview_image_url='https://i.imgur.com/sEM6T0o.jpg'

            )

        if(result == 2):

            message = ImageSendMessage(

                original_content_url='https://i.imgur.com/ntyCKwx.jpg',

                preview_image_url='https://i.imgur.com/ntyCKwx.jpg'

            )

        if(result == 3):

            message = ImageSendMessage(

                original_content_url='https://i.imgur.com/JIiCoNv.jpg',

                preview_image_url='https://i.imgur.com/JIiCoNv.jpg'

            )

        if(result > 3):

            message = ImageSendMessage(

                original_content_url='https://i.imgur.com/kTpBKD1.jpg',

                preview_image_url='https://i.imgur.com/kTpBKD1.jpg'

            )

    

#############################################

#回傳ButtonsTemplate訊息

    if(get == '汪'):

        message = TemplateSendMessage(

            alt_text = '用手機看好不好?',

            template = ButtonsTemplate(

                title = '測試用',

                text = '預祝各位期末ALL PASS',

                thumbnail_image_url = 'https://i.imgur.com/74HtSJK.jpg',

                actions = [

                    MessageTemplateAction(

                        label = '伯朗咖啡',

                        text = '好喝'

                    )

                ]

            )

        )

    if(get == '哈哈' or get == '哈哈哈'):

        get = '哈'

    if(get == '哈'):

        message = TemplateSendMessage(

            alt_text = '打開手機，許願池在你的手機裡?',

            template = ButtonsTemplate(

                title = '哈哈哈精靈許願池',

                text = '夢幻歌單，實現巨星之夢',

                thumbnail_image_url = 'https://i.imgur.com/jD1JAoH.jpg',

                actions = [

                    MessageTemplateAction(

                        label = '晶球',

                        text = '想出現在圖庫裡? 請將你的照片郵寄至ricky870921@gmail.com'

                    ),

                    URITemplateAction(

                        label = '你的女友對我打了槍',

                        uri = 'https://youtu.be/7EhVUpchE3A'

                    ),

                    URITemplateAction(

                        label = '呱風螫天 feat.韶洋',

                        uri = 'https://youtu.be/jyyq8UmJBh0'

                    )

                ]

            )

        )



#############################################

#回傳CarouselColumnTemplate訊息

#多個ButtonsTemplate

    if(get == '蝦米' or get == '當然'):

        get = '橘子'

    if(get == '橘子'):

        message = TemplateSendMessage(

            alt_text = '噹噹 小丁噹小丙噹小乙噹小甲噹',

            template = CarouselTemplate(

            columns=[

                CarouselColumn(

                    thumbnail_image_url='https://i.imgur.com/VQpvhMX.jpg',

                    title='在此提供香豔照',

                    text='請別攝取過量',

                    actions=[

                        MessageTemplateAction(

                            label='內克·脖子',

                            text='誌誌抽'

                        ),

                        MessageTemplateAction(

                            label='甩奶',

                            text='庭庭抽'

                        ),

                        MessageTemplateAction(

                            label='吉他社社長',

                            text='阿祥抽'

                        )

                    ]

                ),

                CarouselColumn(

                    thumbnail_image_url='https://i.imgur.com/f6aeyv4.jpg',

                    title='奉上真實寫真',

                    text='衝一點別太龜',

                    actions=[

                        MessageTemplateAction(

                            label='女神雙下巴',

                            text='唇語抽'

                        ),

                        MessageTemplateAction(

                            label='風保大姐頭',

                            text='程程抽'

                        ),

                        MessageTemplateAction(

                            label='橘子本人',

                            text='雨林抽'

                        )

                    ]

                ),

                CarouselColumn(

                    thumbnail_image_url='https://i.imgur.com/4gzv4mJ.png',

                    title='那些年，我們一起追的男孩',

                    text='結果還是被發卡',

                    actions=[

                        MessageTemplateAction(

                            label='2-021',

                            text='剛剛在Dcard看到一個可愛der女森'

                        ),

                        MessageTemplateAction(

                            label='劉·精益補習班',

                            text='劉德滑抽'

                        ),

                        MessageTemplateAction(

                            label='金正恩',

                            text='晴天抽'

                        )

                    ]

                ),

                CarouselColumn(

                    thumbnail_image_url='https://i.imgur.com/IbbQ1xo.jpg',

                    title='解剖結果出來了',

                    text='死因 - 解剖',

                    actions=[

                        MessageTemplateAction(

                            label='國軍弟兄',

                            text='無疑王玉抽'

                        ),

                        MessageTemplateAction(

                            label='智障',

                            text='+淳抽'

                        ),

                        MessageTemplateAction(

                            label='O777777',

                            text='阿倩仔抽'

                        )

                    ]

                ),

                CarouselColumn(

                    thumbnail_image_url='https://i.imgur.com/QD3Yikd.jpg',

                    title='I\'m still the same.',

                    text='小考分數還是沒有變',

                    actions=[

                        MessageTemplateAction(

                            label='我好興奮阿',

                            text='癡漢二人組'

                        ),

                        MessageTemplateAction(

                            label='(coming soon)',

                            text='梗圖欠缺中'

                        ),

                        MessageTemplateAction(

                            label='點歌許願池',

                            text='哈'

                        )

                    ]

                )

            ]

            )

        )    

    

    

    

#############################################

    if(get == '紹洋晴天破音'):

        message = AudioSendMessage(

            original_content_url='https://drive.google.com/file/d/1qsYbtwVQzrHVuiy3JPIFdwcF-vTr3l7j/view?usp=sharing',

            duration=240000

        )

    line_bot_api.reply_message(event.reply_token, message)



if __name__ == "__main__":

    app.run()
