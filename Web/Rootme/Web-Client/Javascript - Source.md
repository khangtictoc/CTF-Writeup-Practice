# Javascript - Source

**Point:** 5 points 

**Description**: You know javascript ?

## Solution: 

<p align="center"> <img widht="400px" height="150px" src="https://user-images.githubusercontent.com/48288606/157894850-7e058340-2b2a-4c44-a6fb-3bc4996cd1d5.png" /> </p>

A prompt make us to enter the correct password. Open "Developer Tools" -> Source -> index: 

```javascript
<html>
    <head>
	<script type="text/javascript">
	/* <![CDATA[ */
	    function login(){
		pass=prompt("Entrez le mot de passe / Enter password");
		if ( pass == "123456azerty" ) {
		    alert("Mot de passe accepté, vous pouvez valider le challenge avec ce mot de passe.\nYou can validate the challenge using this password.");  }
		else {
		    alert("Mauvais mot de passe / wrong password !");
		}
	    }
	/* ]]> */
	</script>
    </head>
   <body onload="login();"><link rel='stylesheet' property='stylesheet' id='s' type='text/css' href='/template/s.css' media='all' /><iframe id='iframe' src='https://www.root-me.org/?page=externe_header'></iframe>

    </body>
</html>
```

The password is **123456azerty**. Submit it !!!

<p align="center"> <img widht="400px" height="150px" src="https://user-images.githubusercontent.com/48288606/157895195-f9677a26-9976-40a0-8548-9eeeec71bace.png" /> </p>

It tell us to submit the valid password above.

Flag: **123456azerty**




