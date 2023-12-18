import requests
import json

PHONE_ID = "<whatsapp-phone-id>"
TOKEN = "<whatsapp-token>"
NUMBER = "<number>"
MESSAGE = "<message>"

URL = "https://graph.facebook.com/v13.0/"+PHONE_ID+"/messages"
headers = {
    "Authorization": "Bearer "+TOKEN, 
    "Content-Type": "application/json"
}
data = { 
    "messaging_product": "whatsapp", 
    "to": NUMBER, 
    "type": "text", 
    "text": json.dumps({ "preview_url": False, "body": MESSAGE}) 
}
response = requests.post(URL, headers=headers, data=data)
response_json = response.json()
print(response_json)