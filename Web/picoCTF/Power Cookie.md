# Power Cookie ❓

**Tags:** Web Exploitation

**Point:** 200 points

**Description:** 
Can you get the flag?<br>
Go to [this](http://saturn.picoctf.net:64271/) website and see what you can discover.

### Solution: 💯

Click the button "Continue as guest". The page will be directed and shows up message "We apologize, but we have no guest services at the moment.". Here, open "Developer Tools" -> Application -> Storage -> Cookie -> "saturn.picoctf.net", edit "value" of "isAdmin" to 1. After that, reload pages



#### The Flag (for reference): ✔️
```
picoCTF{gr4d3_A_c00k13_dcb9f091}
```
