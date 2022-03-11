# Javascript - Obfuscation 1

**Point:** 10 Points

## Solution: 

A prompt require us to input password.

<p align="center"> <img widht="400px" height="150px" src="https://user-images.githubusercontent.com/48288606/157898912-69683f39-bd27-43c1-9491-4e9208b034fa.png" /></p>

Open "Developer Tools" -> Source -> ch4.html

```javascript
<html>
    <head>
        <title>Obfuscation JS</title>

          <script type="text/javascript">
              /* <![CDATA[ */

              pass = '%63%70%61%73%62%69%65%6e%64%75%72%70%61%73%73%77%6f%72%64';
              h = window.prompt('Entrez le mot de passe / Enter password');
              if(h == unescape(pass)) {
                  alert('Password accepté, vous pouvez valider le challenge avec ce mot de passe.\nYou an validate the challenge using this pass.');
              } else {
                  alert('Mauvais mot de passe / wrong password');
              }

              /* ]]> */
          </script>
    </head>
   <body><link rel='stylesheet' property='stylesheet' id='s' type='text/css' href='/template/s.css' media='all' /><iframe id='iframe' src='https://www.root-me.org/?page=externe_header'></iframe>
    </body>
</html>
```

Read the code. Our password is compare with a password `if(h == unescape(pass)) `. We can debug here, open "Console" tab in "Developers Tools":
- Set `var pass = '%63%70%61%73%62%69%65%6e%64%75%72%70%61%73%73%77%6f%72%64';`
- Set `var h = unescape(pass)`
- Print the value `console.log(h);`
The output value (cpasbiendurpassword) is the password we need. Submit the result !

<p align="center"><img widht="400px" height="150px" src="https://user-images.githubusercontent.com/48288606/157900007-83e29ecf-f9ee-42fc-83b8-298e4229eac5.png" /> </p>

The password is the flag, too!

Flag: **cpasbiendurpassword**
