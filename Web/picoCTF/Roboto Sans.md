# Roboto Sans ❓

**Tags:** Web Exploitation

**Point:** 200 points

**Description:** 
The flag is somewhere on this web application not necessarily on the website. Find it.<br>
[Check this out.](http://saturn.picoctf.net:65442/)

### Solution: 💯

We have a website with nothing really special.

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/160036972-c9f99f9d-dc80-4149-925f-7d45a3d9e38b.png"></p>

The title of the challenge is **Roboto Sans**, this hinted to us that we'll need to inspect `robots.txt` file. [Find more information here!](https://developers.google.com/search/docs/advanced/robots/intro#:~:text=txt-,A%20robots.,or%20password%2Dprotect%20the%20page.). Move to that **file path**.

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/160037035-82ef8250-3f96-4202-a9a2-03ce61d28826.png"></p>

There's another hint telling us that we are near to the flag - "Think you have seen your flag or want to keep looking.". We notice that there's a base64-encoded string `anMvbXlmaWxlLnR4dA==`. We use [this tools](https://www.base64decode.org/) to decode. We get decoded string: `js/myfile.txt`. 

Move to that file path `http://saturn.picoctf.net:65442/js/myfile.txt`. Hurray ! We got the flag. 

#### The Flag (for reference): ✔️
```
picoCTF{Who_D03sN7_L1k5_90B0T5_a4f5cc70}
```
