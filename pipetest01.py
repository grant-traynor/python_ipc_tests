#!/usr/bin/env python
'''
DOCSTRING
'''
import asyncio
from datetime import datetime

WORDS = "A big cat was here."
WORDS += "A big horse was here."
WORDS += "A big cat was here."

# Setup The Server
async def handle_echo(reader, writer):
    '''
    A Server
    '''
    msg_count = 0
    msg_measure = 50000
    t_now = datetime.now()

    while True:
        data = await reader.read(100)
        message = data.decode()
        addr = writer.get_extra_info('peername')
        writer.write(data)
        await writer.drain()
        msg_count += 1

        if msg_count % msg_measure == 0:
            t_delta = datetime.now() - t_now
            us_per_msg = 1000000.0 * t_delta.total_seconds()/msg_measure
            msg_sec = 1000000 / us_per_msg
            print("{} Messages took {} which is {} us per round trip or {} per second".format(msg_measure, 
                            t_delta, us_per_msg, msg_sec))
            t_now = datetime.now()

    # Never Happens
    print("Close the client socket")
    writer.close()


LOOP = asyncio.get_event_loop()
CORO = asyncio.start_server(handle_echo, '127.0.0.1', 8888, loop=LOOP)
SERVER = LOOP.run_until_complete(CORO)
print('Serving on {}'.format(SERVER.sockets[0].getsockname()))

# Setup the Client
async def tcp_echo_client(message, loop):
    '''
    A Client
    '''
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888,
                                                   loop=loop)

    while True:
        #print('Send: %r' % message)
        writer.write(message.encode())

        data = await reader.read(100)
        #print('Received: %r' % data.decode())

    print('Close the socket')
    writer.close()

CLIENT = LOOP.run_until_complete(tcp_echo_client("Send Me", LOOP))

# Run Until We Get Crtl-C
try:
    LOOP.run_forever()
except KeyboardInterrupt:
    pass

LOOP.run_until_complete(SERVER.wait_closed())
LOOP.close()
