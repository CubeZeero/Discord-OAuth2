# Discord-OAuth2
Discord OAuth2 Example
PythonのFlaskを利用したDiscordのOAuth2のサンプルプログラム

## Run
Flaskをインストール

```
pip install flask
```

client_idとclient_secretを指定し、portを変更します
callbackURIは http://localhost:(ここにポート番号)/callback/ を設定してください

テストとして取得されたトークンなどは、responce.txt としてまとめて出力されます
認証完了時は認証が完了したことを示すhtmlを表示するようにしています
