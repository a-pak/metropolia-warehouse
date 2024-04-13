import os
import asyncio
from azure.iot.device.aio import IoTHubDeviceClient


async def main(msg):
    # Fetch the connection string from an environment variable
    conn_str = "HostName=warehouse.azure-devices.net;DeviceId=client-server;SharedAccessKey=wID6chypwyI4R2qHin2fyaPIICX7LcTBOAIoTNzraPI="
    
    # Create instance of the device client using the connection string
    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)

    # Connect the device client.
    await device_client.connect()

    # Send a single message
    print("Sending message...")
    await device_client.send_message(msg)
    print("Message successfully sent!")

    # Finally, shut down the client
    await device_client.shutdown()


def send_mqtt_request(msg):
    asyncio.run(main(msg))