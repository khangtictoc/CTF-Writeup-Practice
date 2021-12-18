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
Compared to first **Web Gauntlet". This challenge only have 1 round but more difficult.

## Solution: 💯

Filter: `or and true false union like = > < ; -- /* */ admin`

In this chall, we try to create an injection in **username** which should cover and ignore the **password**. We use concatenation `||` to create string `admin` in **username**
. We try to combine with password to generate the character in `admin` string. 

Our payload look like this: `SELECT username, password FROM users where username='admi'||{n}`

We get the `'n'` character by `CHAR()` function and specify the exact number we need in [Ascii Table](https://www.asciitable.com/) (n=110 in decimal). We take an advantage of `LENGTH()` function to control the value. And now we will calculate: The must-have string is ` AND password=` has 14 characters. We need 110 so it ought to be multiplied by 7 and add by 12. 

The actual query string is below: `SELECT * FROM users where username='admi'||(CHAR(12+LENGTH(' AND password=')*7))||'' `

**Note:** This chall requires the sum of length of username and password < 35. In some case if our payload's size is too large, we should  decrease it by omitting redundant characters in **password** or instead of string, we should move to calculate with number. 
**Note:** May be  using **division operator** (In this case is `1540/LENGTH(' AND password=')` for more easy calculations.

#### The Flag (for reference): ✔️
```
picoCTF{0n3_m0r3_t1m3_fc0f841ee8e0d3e1f479f1a01a617ebb}
```

