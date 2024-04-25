from azure.iot.device import IoTHubDeviceClient, Message
import os
import threading
import traceback
import time

class IoTHubCommunication:
    def __init__(self, connection_string, device_id):
        self.connection_string = connection_string
        self.device_id = device_id
        self.client = IoTHubDeviceClient.create_from_connection_string(self.connection_string)
        self.is_running = False
        self.client.connect()
        print("connected")



    def send_message(self, message):
        try:
            message = Message(message)
            self.client.send_message(message)
            print("Message sent to Azure IoT Hub. Waiting for response...")
            
            self.is_running = True
            while (self.is_running):
                message = self.client.receive_message()
                if(message):
                    print(message)
                    self.is_running = False

        except Exception as e:
            print("An error occurred while sending a message to Azure IoT Hub:")
            print(e)
            traceback.print_exc()