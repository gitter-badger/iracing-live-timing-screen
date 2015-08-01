import logging
import asyncio
import websockets
import irsdk
import json

logger = logging.getLogger('websockets')
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

@asyncio.coroutine
def hello(websocket, path):
    message = yield from websocket.recv()
    #message = json.loads(message)['data']
    print("< {}".format(message), path)
    yield from websocket.send(message)
    print("> {}".format(message))

start_server = websockets.server.serve(hello, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()