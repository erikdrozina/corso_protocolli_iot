import json
import aiocoap.resource as resource
import aiocoap
import asyncio
import os, sys

from asyncio.protocols import DatagramProtocol
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(f'{dir_path}/../common')
from generate_data import get_sensors_data


class SensorsResource(resource.Resource):
    async def render_get(self, request):
        drone_id = 1
        # obtain data from sensors
        datajson = json.dumps(get_sensors_data(drone_id))
        # send CoAP message
        return aiocoap.Message(content_format=0,
                payload=datajson.encode('utf8'))
 
def main():
    ipaddress = 'localhost'
    port = 5683

    root = resource.Site()
    # declare routes
    root.add_resource(['sensors'], SensorsResource())
    asyncio.Task(aiocoap.Context.create_server_context(root, bind=(ipaddress, port)))
    print(f"\nServer CoAP started on {ipaddress}:{port}\n")
    # set to loop forever
    asyncio.get_event_loop().run_forever()
    
 
if __name__ == "__main__":
    
    main()