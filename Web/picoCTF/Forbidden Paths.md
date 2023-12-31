# Forbidden Paths ❓

**Tags:** Web Exploitation

**Point:** 200 points

**Description:** 
Can you get the flag? <br>
[Here's the website.](http://saturn.picoctf.net:53295/)<br>
We know that the website files live in /usr/share/nginx/html/ and the flag is at /flag.txt but the website is filtering absolute file paths. Can you get past the filter to read the flag?

### Solution: 💯

This challenge require us to input the file path to read that file content. But they filtered the `absolute path` out. We can use `relative path` because "the flag is at /flag.txt". It means `flag.txt` is in **root** `/` path. 

With that in mind, we don't need to know current location, just "step back" to the **parent** path until we can reach that `flag.txt` file.

Final path: `../../../../flag.txt`

#### The Flag (for reference): ✔️
```
picoCTF{7h3_p47h_70_5ucc355_26b22ab3}
```
