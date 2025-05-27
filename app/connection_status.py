import requests
import time
import os
from dotenv import load_dotenv
import json
from get_instance_id import get_instance_id

def send_heartbeat():
    instance_id = get_instance_id()
    if not instance_id:
        print("Instance ID not found, skipping heartbeat.")
        return
    
    url = 'https://dev.climatenet.am/node/status/'  # Your Django API endpoint
    load_dotenv()

    data = {
        'instance_id': instance_id,  # Send instance ID dynamically
    }
    try:
        response = requests.post(url, json=data, timeout=5)
        print(response.status_code, response.text)
    except requests.exceptions.RequestException as e:
        print(f"Failed to send heartbeat: {e}")

while True:
    send_heartbeat()
    time.sleep(60)  # Wait 60 seconds before sending the next heartbeat
