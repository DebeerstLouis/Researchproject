import os
import json
import time
import random
import asyncio
from azure.iot.device import IoTHubDeviceClient

def main():
    # Fetch the connection string from an enviornment variable
    conn_str = "HostName=researchproject-Louis.azure-devices.net;DeviceId=PI_Louis;SharedAccessKey=rQ4F7Rs618hhhBXCCYit/nobTQqpA8gYkYrnmV8HiYk="
    # Create instance of the device client using the authentication provider
    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)
    # Connect the device client.
    device_client.connect()
    for i in range(10):
        print(i)
        # Send a single message
        print("Sending message...")
        device_client.send_message('{"number": 10}')
        print("Message successfully sent!")
    # finally, disconnect
    device_client.disconnect()
if __name__ == "__main__":
    main()