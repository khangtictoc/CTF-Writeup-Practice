# Logon ❓
**Tags:** Web Exploitation<br>
**Point:** 100<br>
**Description:** The factory is hiding things from all of its users. Can you login as logon and find what they've been looking at?
https://jupiter.challenges.picoctf.org/problem/15796/ or http://jupiter.challenges.picoctf.org:15796

## Write-up: 📝
This is one of my first favorite CTF challenges to explore more in ```Inspect 🔍``` tools. The challenge also provide a hint which is essentially login as logon, means we need to login as administrator.<br>
And by default , we can just login to the website as a normal user and it doesn't check any passwords . With common login, as you can see, there is no flag. So we have to set our "Access authority" as "Administrator". Fortunately, we can manipulate our login data by set cookie values.

### Solution: 💯
```
1. Just login as a end user.
2. Inspect the Website by F12 or Right Click -> Choose Inspect .
3. Choose Application Tab , then choose "Cookies" in Storage section . 
4. Change the value of admin which is "False" by default into "True" to gain administrative access.
5. Reload the webpage  and here comes a flag. 
```

#### The Flag (for reference): ✔️
```
picoCTF{th3_c0nsp1r4cy_l1v3s_6edb3f5f}
```
