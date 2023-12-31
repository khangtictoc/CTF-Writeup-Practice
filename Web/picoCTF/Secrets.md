# Secrets ❓

**Tags:** Web Exploitation

**Point:** 200 points

**Description:** 
We have several pages hidden. Can you find the one with the flag?<br>
[The website is running here.](http://saturn.picoctf.net:54925/)

### Solution: 💯

Nothing but a normal site. 

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/160038507-3f1a027a-9a39-4ae1-8871-28bd3409a966.png"></p>

Inspect the **source** (Ctrl + U). We can see a `secret` path 

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/160038676-23c5a418-c63d-4bd0-962c-0e8c22895318.png"></p>

Move to `/secret/` path : `http://saturn.picoctf.net:54925/secret/`

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/160038767-b772cf52-bbaf-47e6-876b-e790c83df625.png"></p>

Inspect the **source** again. We can see a `hidden` path in current `/secret/` 

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/160038900-1ac594d6-7bcf-4fef-9d89-605832aadd52.png"></p>

Move to `/secret/hidden/` path: `http://saturn.picoctf.net:54925/secret/hidden/`. 

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/160039103-4ccf79a7-7095-44b2-b94c-cdf86d49e14a.png"></p>

Inspect again more (~ _ ~). There's a `/superhidden/` path in current `/secret/hidden/`

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/160039368-c24e2bb7-8ffb-499c-b3d7-263bffebc499.png"></p>

Move to `/secret/hidden/superhidden/` path: `http://saturn.picoctf.net:54925/secret/hidden/superhidden/`. 

A site with message "Finally. You found me. But can you see me" shows up. Inspect the **source** one more to get the flag.

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/160039660-2a8ca3e8-f003-4e57-b6fb-0c5d3d6deba0.png"></p>

#### The Flag (for reference): ✔️
```
picoCTF{succ3ss_@h3n1c@10n_34327aaf}
```
