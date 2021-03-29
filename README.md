# 2min-socketio-python

## 環境構築

```sh
pipenv sync --dev
pipenv shell
```


## Socket.IOでサーバーを立ててHoppscotchで接続

```sh
python server.py
```

Hoppscotchを起動、URLに`ws://localhost:8000`を入力して接続。



## 気になる

- Hoppscotchで切断すると例外がでているっぽい

