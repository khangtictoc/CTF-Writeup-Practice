# picobrowser ❓

**Tags:** Web Exploitation

**Point:** 200 points

**Description:** 
This website can be rendered only by picobrowser, go and catch the flag! https://jupiter.challenges.picoctf.org/problem/50522/ (link) or http://jupiter.challenges.picoctf.org:50522

### Solution: 💯

Require user to access flag by `picobrowser`. Use Burp Suite to intercept the request and modify `User-Agent` header then send it

#### The Flag (for reference): ✔️
```
picoCTF{p1c0_s3cr3t_ag3nt_51414fa7}
```
