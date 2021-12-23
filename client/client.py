# client_put.py
import asyncio
import random
 
from aiocoap import *
from aiocoap import resource
 
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
    asyncio.get_event_loop().run_until_complete(main())