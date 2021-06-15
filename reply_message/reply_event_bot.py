import os

from linebot.models.events import VideoPlayCompleteEvent

if os.getenv('DEVELOPMENT') is not None:
    from dotenv import load_dotenv

    load_dotenv(dotenv_path='../.env')

import sys
from argparse import ArgumentParser

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FlexSendMessage, TemplateSendMessage,
    ImageCarouselTemplate, ImageCarouselColumn, PostbackAction, LocationSendMessage,
    VideoSendMessage, ImageSendMessage, StickerSendMessage,
)

app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = 'YOUR_SECRET' or os.getenv('LINE_CHANNEL_SECRET')
channel_access_token = 'YOUR_ACCESS_TOKEN' or os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)


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


@handler.add(MessageEvent, message=TextMessage)
def message_text(event):
    message = event.message.text
    if message == 'emoji':
        emoji = [
            {
                "index": 0,
                "productId": "5ac1bfd5040ab15980c9b435",
                "emojiId": "001"
            },
            {
                "index": 13,
                "productId": "5ac1bfd5040ab15980c9b435",
                "emojiId": "002"
            }
        ]
        output = TextSendMessage(text='$ LINE emoji $', emojis=[emoji])
    elif message == 'sticker':
        # https://github.com/line/line-bot-sdk-python#stickersendmessage
        output = StickerSendMessage(
            package_id='1',
            sticker_id='1'
        )
    elif message == 'image':
        # https://github.com/line/line-bot-sdk-python#imagesendmessage
        output = ImageSendMessage(
            original_content_url='https://engineering.linecorp.com/wp-content/uploads/2021/06/linebot001-1024x571.jpg',
            preview_image_url='https://engineering.linecorp.com/wp-content/uploads/2021/06/linebot001-1024x571.jpg'
        )
    elif message == 'video':
        # https://github.com/line/line-bot-sdk-python#videosendmessage
        output = VideoSendMessage(
            original_content_url='https://example.com/original.mp4',
            preview_image_url='https://engineering.linecorp.com/wp-content/uploads/2021/04/%E6%88%AA%E5%9C%96-2021-04-23-%E4%B8%8B%E5%8D%883.00.15.png',
            tracking_id='test video'
        )
    elif message == 'location':
        # https://github.com/line/line-bot-sdk-python#locationsendmessage
        output = LocationSendMessage(
            title='my location',
            address='Tokyo',
            latitude=35.65910807942215,
            longitude=139.70372892916203
        )
    elif message == 'flex':
        # https://github.com/line/line-bot-sdk-python#flexsendmessage
        output = FlexSendMessage(
            alt_text='hello',
            contents={
                'type': 'bubble',
                'direction': 'ltr',
                'hero': {
                    'type': 'image',
                    'url': 'https://example.com/cafe.jpg',
                    'size': 'full',
                    'aspectRatio': '20:13',
                    'aspectMode': 'cover',
                    'action': {'type': 'uri', 'uri': 'http://example.com', 'label': 'label'}
                }
            }
        )
    else:
        output = TextSendMessage(text="Just echo echo~~~")
    line_bot_api.reply_message(
        event.reply_token,
        output
    )


@handler.add(VideoPlayCompleteEvent)
def handle_follow(event):
    event_name = event.video_play_complete.tracking_id
    output = 'Video fail'
    if event_name == 'video':
        output = 'Complete'
    line_bot_api.reply_message(
        event.reply_token,
        messages=[TextSendMessage(text=output)]
    )


if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', default=8000, help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()

    app.run(host='0.0.0.0', debug=options.debug, port=options.port)
