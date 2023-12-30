# More Cookies ❓
**Tags:** Web Exploitation<br>
**Point:** 40  <br>
**Description:** Who doesn't love cookies? Try to figure out the best one. http://mercury.picoctf.net:54219/

Hint:
(None)

## Write-up: 📝

The website allow to search cookie with the name
Inspect the cookie with **Developer Tools**, we notice that there is a key `name` that store the id of the cookie, so we just bruteforce with this index, no need to brute force the name of the cookie

My [Python script](/Web/picoCTF/Cookies/solve.py) loop through increasing index (1000 loop times should be good enough), then check if the flag is returned

#### The Flag (for reference): ✔️
```
picoCTF{3v3ry1_l0v3s_c00k135_96cdadfd}
```