import asyncio
import logging
import time

from asyncua import Client

_logger = logging.getLogger(__name__)

async def main():
    url = "opc.tcp://10.4.1.134:4840"
    async with Client(url=url) as client:
        uri = "http://monURI"
        idx = await client.get_namespace_index(uri)

        object = client.get_objects_node()
        objects = await object.get_child([f'{idx}:NX1021020_Boudineuse', f'{idx}:GlobalVars'])
        acquisitions = await objects.get_variables()

        while True :
            for acquisition in acquisitions:
                name = (await acquisition.read_display_name()).Text
                if "acquisition" in name :
                    print(await acquisition.read_value())
            print("---------------")
            time.sleep(1.5)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
