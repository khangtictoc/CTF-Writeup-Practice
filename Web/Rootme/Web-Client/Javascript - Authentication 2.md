# Javascript - Authentication 2

**Point:** 10 Points

**Description:** Yes folks, Javascript is damn easy :)

## Solution:

There's a login button. Click it !!! Two prompt appear require username & password:

<p align="center"><img width="400px" height="150px" src="https://user-images.githubusercontent.com/48288606/157896207-0a05061d-3e02-48fc-81ad-b5a22d8783fb.png" /> </p>

<p align="center"><img width="400px" height="150px" src="https://user-images.githubusercontent.com/48288606/157896215-f7ca1b17-df85-4bcc-b6b7-a91779fbcda2.png" /> </p>

Open "Developer Tools" -> Source -> login.js: 

```javascript
function connexion(){
    var username = prompt("Username :", "");
    var password = prompt("Password :", "");
    var TheLists = ["GOD:HIDDEN"];
    for (i = 0; i < TheLists.length; i++)
    {
        if (TheLists[i].indexOf(username) == 0)
        {
            var TheSplit = TheLists[i].split(":");
            var TheUsername = TheSplit[0];
            var ThePassword = TheSplit[1];
            if (username == TheUsername && password == ThePassword)
            {
                alert("Vous pouvez utiliser ce mot de passe pour valider ce challenge (en majuscules) / You can use this password to validate this challenge (uppercase)");
            }
        }
        else
        {
            alert("Nope, you're a naughty hacker.")
        }
    }
}
```
Let's look at this code. Its functionalities do the following steps:
- Declare a list with 1 item ** ["GOD:HIDDEN"]**
- If the **username** (our input) appear in the first place (0th index) of **TheLists**, move to next. It means the first character must contain 'G'.
- The var **TheSplit**  splits item from the list above, return 2 items ['GOD','HIDDEN'], assign these to **TheUsername** and **ThePassword**
So as we found out, the username is **GOD** and password is **HIDDEN**. Submit the value !

<p align="center"><img width="400px" height="150px" src="https://user-images.githubusercontent.com/48288606/157898000-2de3d884-ffff-46ce-8494-97e33c9dab1d.png"></p>

It tell us to submit the valid password above.

Flag: **HIDDEN**
