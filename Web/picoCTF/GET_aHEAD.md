# GET aHEAD ❓
**Tags:** Web Exploitation<br>
**Point:** 20 <br>
**Description:** Find the flag being held on this server to get ahead of the competition http://mercury.picoctf.net:53554/
Hint:
- Maybe you have more than 2 choices
- Check out tools like Burpsuite to modify your requests and look at the responses

## Write-up: 📝

- Use Burpsuite to intercept the request and examine the response.
- "Choose red" use **GET** method, "Choose blue" use **POST** method
- As the title of challenge and hints suggested, we modify our request and change to **HEAD** method.

![image](https://user-images.githubusercontent.com/48288606/147682699-0acdb7ab-7e5a-4a01-ad28-d7c2a2a191d6.png)

- Forward request and view the response.

#### The Flag (for reference): ✔️
```
picoCTF{r3j3ct_th3_du4l1ty_2e5ba39f}
```
