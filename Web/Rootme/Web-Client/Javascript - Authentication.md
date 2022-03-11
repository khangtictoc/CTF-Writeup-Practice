# Javascript - Authentication

**Point:** 5 points

## Solution:

<p align="center"> <img  src="https://user-images.githubusercontent.com/48288606/157893271-45c2ae29-ccb6-4817-a9ff-e373ad8aebfd.png" alt="123" /> </p>

We have username and password input field. Open "Developer Tools" -> Source -> login.js :

```javascript
function Login(){
	var pseudo=document.login.pseudo.value;
	var username=pseudo.toLowerCase();
	var password=document.login.password.value;
	password=password.toLowerCase();
	if (pseudo=="4dm1n" && password=="sh.org") {
	    alert("Password accepté, vous pouvez valider le challenge avec ce mot de passe.\nYou an validate the challenge using this password.");
	} else { 
	    alert("Mauvais mot de passe / wrong password"); 
	}
```

**pseudo** gets value of username input, **password** gets value of password input. Then they're both set to lowercase.
So we have username and password to pass the challenge. (4dm1n && sh.org)

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/157893906-d9fe103a-6d72-4be9-bab5-e242b4143382.png" /> </p>

It tell us to submit with the valid password above. 

Flag: **sh.org**
