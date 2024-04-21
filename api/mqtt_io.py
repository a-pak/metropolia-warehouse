import os
from azure.iot.device import IoTHubDeviceClient


def send_mqtt_request(msg):
    # Fetch the connection string from an environment variable
    
    try:   
        #conn_str = os.environ['IOT_CONNECTION_STRING']
        conn_str = "HostName=warehouse.azure-devices.net;DeviceId=client-server;SharedAccessKey=wID6chypwyI4R2qHin2fyaPIICX7LcTBOAIoTNzraPI="
        # Create instance of the device client using the connection string
        device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)

        # Connect the device client.
        device_client.connect()

        # Send a single message
        print("Sending message...")
        device_client.send_message(msg)
        print("Message successfully sent!")

        # Finally, shut down the client
        device_client.shutdown()
    except:
        print('Can not send MQTT message: IOT_CONNECTION_STRING not found')