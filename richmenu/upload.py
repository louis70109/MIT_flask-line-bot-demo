import os

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

# Example: https://github.com/line/line-bot-sdk-python#set_rich_menu_imageself-rich_menu_id-content_type-content-timeoutnone
# Document https://developers.line.biz/en/reference/messaging-api/#upload-rich-menu-image

content_type = 'image/png'  # Just support JPEG or PNG, check your image type

try:
    with open('template.png', 'rb') as f:
        line_bot_api.set_rich_menu_image('RICH_EMNU_ID', content_type, f)
except Exception as e:
    print(e)

print('Set default success.')
