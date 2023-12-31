# SQLiLite ❓

**Tags:** Web Exploitation

**Point:** 300 points

**Description:** 
Can you login to this website?
Try to login [here](http://saturn.picoctf.net:62733/).

**Hint:** admin is the user you want to login as.

### Solution: 💯

This is a basic SQLi vulnerability with the hint is "admin is the user you want to login as".

Username: **admin' --**

Password: **123** (optional string)

We redirect to another page with message "Logged in! But can you see the flag, it is in plainsight." . Open "Developer Tool" -> Element. Flag's there !

#### The Flag (for reference): ✔️
```
picoCTF{L00k5_l1k3_y0u_solv3d_it_33d32a56}
```
