import json

REGISTRATION_FILE = "/var/lib/amazon/ssm/registration"

def get_instance_id():
    try:
        with open(REGISTRATION_FILE, "r") as f:
            data = json.load(f)  # Load JSON data from the file
            return data.get("ManagedInstanceID")  # Extract instance ID
    except Exception as e:
        print(f"Error reading instance ID: {e}")
        return None
