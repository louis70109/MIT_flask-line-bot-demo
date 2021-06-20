import os

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
    MessageEvent, TextMessage, TextSendMessage, QuickReply, QuickReplyButton, MessageAction,
    DatetimePickerAction, URIAction, CameraAction, CameraRollAction, LocationAction,
    PostbackAction,
)

app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET') or 'YOUR_SECRET'
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN') or 'YOUR_ACCESS_TOKEN'
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
    quick_reply = QuickReply(
        items=[
            QuickReplyButton(action=MessageAction(label="Hello", text="World")),
            QuickReplyButton(action=DatetimePickerAction(
                label="Time",
                data="storeId=12345",
                mode="datetime",)),
            QuickReplyButton(action=CameraAction(label="Camera")),
            QuickReplyButton(action=CameraRollAction(label="Camera Roll")),
            QuickReplyButton(action=LocationAction(label="Location✍️")),
            QuickReplyButton(action=PostbackAction(
                label="Postback",
                data="You can not see me",
                display_text="Hi"
            )),
            QuickReplyButton(
                action=URIAction(
                    label="Share",
                    uri='https://engineering.linecorp.com/zh-hant/blog/')
            )
        ])
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text, quick_reply=quick_reply)
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

