import logging
import asyncio
import json

import websockets
import irsdk

import session

logger = logging.getLogger('websockets')
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

ir = irsdk.IRSDK()
ir.startup(test_file='data.bin')
Session = session.Session(ir)
Session.update_classification()

@asyncio.coroutine
def hello(websocket, path):
    message = yield from websocket.recv()
    print("< {}".format(message), path)
    yield from websocket.send(json.dumps(Session.classification))
    print("> {}".format(json.dumps(Session.classification)))

start_server = websockets.server.serve(hello, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()