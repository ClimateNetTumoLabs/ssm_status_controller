import paho.mqtt.client as mqtt
import json
import os
import requests
from datetime import datetime
from dotenv import load_dotenv
import time
from get_instance_id import get_instance_id

load_dotenv()

ENDPOINT = os.getenv("IOT_ENDPOINT")
CLIENT_ID = get_instance_id()
TOPIC_DEVICE = f"control/{CLIENT_ID}"
TOPIC_ALL = "control/all"

def log(msg):
    print(f"[{datetime.now()}] [{CLIENT_ID}] {msg}")

def on_connect(client, userdata, flags, rc):
    client.subscribe(TOPIC_DEVICE)
    client.subscribe(TOPIC_ALL)

def on_message(client, userdata, msg):
    
    try:
        payload = json.loads(msg.payload.decode())
        command = payload.get("message", "")
    except json.JSONDecodeError:
        command = msg.payload.decode()

    log(f"Received command: {command}")

    if command == "start-ssm":
        os.system('sudo systemctl daemon-reload')
        os.system('sudo systemctl restart amazon-ssm-agent')
        log("SSM Agent restarted.")
    elif command == "stop-ssm":
        os.system('sudo systemctl stop amazon-ssm-agent')
        log("SSM Agent stopped.")
    else:
        log("Unknown command received.")


client = mqtt.Client(client_id=CLIENT_ID)
client.tls_set(ca_certs="certificates/rootCA.pem",
               certfile="certificates/certificate.pem.crt",
               keyfile="certificates/private.pem.key")

client.on_connect = on_connect
client.on_message = on_message

client.connect(ENDPOINT, 8883)
client.loop_forever()
