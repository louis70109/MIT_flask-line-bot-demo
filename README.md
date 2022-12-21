# LINE Bot workshop exsample

- Reply Message
    - Echo bot
    - Icon Switch
    - Quick Reply
    - Reply event demo
- Push Message
    - Push to specific user demonstration
- Rich Menu
    - Create a menu
    - Set default menu to all user
    - Upload image to be a menu

## LINE Bot 設定

1. 先前往 LINE Developers 網站 (https://developers.line.biz/) 註冊帳號，並建立一個新的 Bot。
2. 安裝 Python 和 pip，並使用 pip 安裝 line-bot-sdk 套件。
3. 在程式碼中引用 line-bot-sdk 套件，並設定您的 Channel access token 和 Channel secret。
4. 建立一個 HTTP 伺服器，用於接收 LINE 服務器發送過來的請求。您可以使用 Python 內建的 BaseHTTPServer 模組，或是使用第三方套件如 Flask 或 Django。
5. 在接收到請求時，使用 line-bot-sdk 套件的方法處理請求並回應使用者的訊息。
6. 在 LINE Developers 網站中設定您的 Bot 的 Webhook URL，並啟用 Webhook 功能。
7. 在您的 Bot 中加入自己的功能，並使用 line-bot-sdk 套件的方法將訊息發送回 LINE。

## License

MIT
