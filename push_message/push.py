import os

from linebot.models import TextSendMessage

if os.getenv('DEVELOPMENT') is not None:
    from dotenv import load_dotenv

    load_dotenv(dotenv_path='../.env')

import sys
from linebot import LineBotApi

channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN') or 'YOUR_ACCESS_TOKEN'

if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)

# Example: https://github.com/line/line-bot-sdk-python#push_messageself-to-messages-notification_disabledfalse-timeoutnone
# Document: https://developers.line.biz/en/reference/messaging-api/#send-push-message

to = ''  # Fill the USER_ID
line_bot_api.push_message(to, TextSendMessage(text='Hello this is push message test!'))
