import requests
import os
import base64
import urllib.parse
from decouple import config
from requests.exceptions import ConnectionError
API_TOKEN = config('API_TOKEN')
WHATSAPP_ID = config('WHATSAPP_ID')
INSTANCE = config('INSTANCE')

path_file = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.csv') or f.endswith('.pdf') or f.endswith('.xlsx')]


for path_file in path_file:
    file_complete = os.path.splitext(path_file)
    file_name = ''
    for file in file_complete:
        file_name += file
    print(file_name)
    with open(path_file, "rb") as fileInDirectory:
        encoded_string = base64.b64encode(fileInDirectory.read())
    img_bas64 = urllib.parse.quote_plus(encoded_string)
    url = f"https://api.ultramsg.com/{INSTANCE}/messages/document"

    payload = f"token={API_TOKEN}&to={WHATSAPP_ID}&filename={file_name}&document={img_bas64}&referenceId=&nocache="
    headers = {'content-type': 'application/x-www-form-urlencoded'}

    try:
        response = requests.request("POST", url, data=payload, headers=headers)
    except ConnectionError as e:
        print(e)
        print("---------------network freezing -----------error ---------")
