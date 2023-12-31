# Scavenger Hunt ❓

**Tags:** Web Exploitation

**Point:** 50 points

**Description:** 
There is some interesting information hidden around this site http://mercury.picoctf.net:5080/. Can you find it?

Hints:
- You should have enough hints to find the files, don't run a brute forcer.

### Solution: 💯

- Open source (Ctrl +U), search for "pico", this is the first part. Investigate other resources.
- Second part is in CSS file name `mycss.css`
- Investigate JS file name `myjs.js`. It hints "/* How can I keep Google from indexing my website? */". So it's `robots.txt`. Move to there, we've found the third part
- In there, it says " I think this is an apache server... can you Access the next flag?", so there is a sensitive config file in Apache server name `.htaccess`. That's the fourth part
- Then continue with hint "# I love making websites on my Mac, I can Store a lot of information there."; in MAC, there's a file name `.DS_Store`, access this file. That's the final part

#### The Flag (for reference): ✔️
```
picoCTF{th4ts_4_l0t_0f_pl4c3s_2_lO0k_35844447}
```
