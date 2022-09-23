import requests
from requests.exceptions import ConnectionError
from decouple import config
API_TOKEN = config('API_TOKEN')
WHATSAPP_ID = config('WHATSAPP_ID')
INSTANCE = config('INSTANCE')


def receive_message_sent():
    url = f"https://api.ultramsg.com/{INSTANCE}/chats/messages"

    querystring = {"token": f"{API_TOKEN}", "chatId": f"{WHATSAPP_ID}", "limit": "1000 "}

    headers = {'content-type': 'application/x-www-form-urlencoded'}

    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        new_data = response.json()
        return new_data
    except ConnectionError as e:
        print(e)
        return False
