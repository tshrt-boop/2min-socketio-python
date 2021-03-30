import asyncio

from sanic import Sanic
from sanic.response import html

import socketio
import json

sio = socketio.AsyncServer(async_mode='sanic', cors_allowed_origins=['https://hoppscotch.io'])
app = Sanic(name='sio')
app.config['CORS_SUPPORTS_CREDENTIALS'] = True
sio.attach(app)


@sio.event
def connect(sid, environ, auth):
    print('connect ', sid)

@sio.event
def my_event(sid, data):
    print('my event ', sid, data)
    return json.dumps({'data': data})

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    app.run()