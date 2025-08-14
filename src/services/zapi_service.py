import requests
from src.config import settings

def send_message(message_text, phone_number):
    url = f"https://api.z-api.io/instances/{settings.ZAPI_INSTANCE_ID}/token/{settings.ZAPI_INSTANCE_TOKEN}/send-text"

    headers = {
        "Content-Type": "application/json",
        "Client-Token": settings.ZAPI_CLIENT_TOKEN
    }
    
    payload = {
        "phone": phone_number,
        "message": message_text
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        print("enviooou msg! => {" + message_text + "}")
        print(response.json())
    else:
        print(f"erro na msg: {response.status_code} ==> {response.text}")

    return response
    

if __name__ == "__main__":
    send_message("testando novo", "5511915529263")
