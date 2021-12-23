# client_put.py
import asyncio
import time 
from aiocoap import *


async def main():
    ipaddress = 'localhost'
    # send GET request
    protocol = await Context.create_client_context()
    request = Message(code=GET, uri=f'coap://{ipaddress}/sensors')

    try:
        response = await protocol.request(request).response
    except Exception as e:
        print('Failed to fetch resource:')
        print(e)
    else:
        print(f'\nResult: {response.code}\nResponse: {response.payload}')
 

if __name__ == "__main__":
    while(True):
        asyncio.run(main())
        time.sleep(5)