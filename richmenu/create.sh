curl -v -X POST https://api.line.me/v2/bot/richmenu \
-H 'Authorization: Bearer {channel access token}' \
-H 'Content-Type: application/json' \
-d \
'{
  "size":{
      "width":2500,
      "height":1686
  },
  "selected": false,
  "name": "LINE Developers Info",
  "chatBarText": "Tap to open",
  "areas": [
      {
          "bounds": {
              "x": 34,
              "y": 24,
              "width": 169,
              "height": 193
          },
          "action": {
              "type": "uri",
              "uri": "https://developers.line.biz/en/news/"
          }
      },
      {
          "bounds": {
              "x": 229,
              "y": 24,
              "width": 207,
              "height": 193
          },
          "action": {
              "type": "uri",
              "uri": "https://www.line-community.me/en/"
          }
      },
      {
          "bounds": {
              "x": 461,
              "y": 24,
              "width": 173,
              "height": 193
          },
          "action": {
              "type": "uri",
              "uri": "https://engineering.linecorp.com/en/blog/"
          }
      }
  ]
}'