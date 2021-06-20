
import sys
from linebot import LineBotApi

channel_access_token = 'YOUR_TOKEN'

if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)

# Example: https://github.com/line/line-bot-sdk-python#set_default_rich_menuself-rich_menu_id-timeoutnone
# Document: https://developers.line.biz/en/reference/messaging-api/#set-default-rich-menu
rich_menu_id = 'RICH_MENU_ID'
line_bot_api.set_default_rich_menu(rich_menu_id)
