# Javascript - Obfuscation 4

**Point:** 50 Points

**Description**:Find the password.

**NB**: You will have to enable popups in order to solve this challenge!

## Solution:

References: [ChineseProPlayer](https://github.com/lyy289065406/CTF-Solving-Reports/tree/master/rootme/Web-Client/%5B14%5D%20%5B50P%5D%20Javascript%20-%20Obfuscation%204)

This challenge is really "big deal" to me. It makes me focus on this "hardcore" helps me forget my Ex. I've read up some write-ups to realize the suitable method to solve it. Any way, enter the site. Password input requirement: 

<p align="center"> <img width="400px" height="150px" src="https://user-images.githubusercontent.com/48288606/158101277-6cc1dc90-4612-436e-85bb-2e993586e7df.png"> </p>

Just check the source code as usual. Open "Developer Tools" -> Source -> ch17.html

```html
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<!-- 
But du jeu: trouver le bon mdp ! Il vous faudra de la patience et de l'intuition!
Si vous avez des problèmes, contactez aaSSfxxx sur #root-me
-->

<script>
var ð= "\x71\x11\x24\x59\x8d\x6d\x71\x11\x35\x16\x8c\x6d\x71\x0d\x39\x47\x1f\x36\xf1\x2f\x39\x36\x8e\x3c\x4b\x39\x35\x12\x87\x7c\xa3\x10\x74\x58\x16\xc7\x71\x56\x68\x51\x2c\x8c\x73\x45\x32\x5b\x8c\x2a\xf1\x2f\x3f\x57\x6e\x04\x3d\x16\x75\x67\x16\x4f\x6d\x1c\x6e\x40\x01\x36\x93\x59\x33\x56\x04\x3e\x7b\x3a\x70\x50\x16\x04\x3d\x18\x73\x37\xac\x24\xe1\x56\x62\x5b\x8c\x2a\xf1\x45\x7f\x86\x07\x3e\x63\x47";function _(x,y){return x^y;}function __(y){var z = 0;for(var i=0;i<y;i++){z += Math.pow(2,i);}return z;}function ___(y){var z = 0;for(var i=8-y;i<8;i++){z += Math.pow(2,i);}return z} function ____(x,y){y = y % 8;Ï = __(y);Ï = (x & Ï) << (8-y);return (Ï) + (x >> y);}function _____(x,y){y = y % 8;Ï = ___(y);Ï = (x & Ï) >> (8-y);return ((Ï) + (x << y)) & 0x00ff;}function ______(x,y){return _____(x,y)}function _______(_________,key){________ = "";________2 = "";for(var i=0;i<_________.length;i++){c = _________.charCodeAt(i);if(i != 0){t = ________.charCodeAt(i-1)%2;switch(t){case 0:cr = _(c, key.charCodeAt(i % key.length));break;case 1:cr = ______(c, key.charCodeAt(i % key.length));break;}}else{cr = _(c, key.charCodeAt(i % key.length));}________ += String.fromCharCode(cr);}return ________;}function __________(þ){var ŋ=0;for(var i=0;i<þ.length;i++){ŋ+=þ["charCodeAt"](i)}if(ŋ==8932){var ç=window.open("","","\x77\x69\x64\x74\x68\x3d\x33\x30\x30\x2c\x68\x65\x69\x67\x68\x74\x3d\x32\x20\x30");ç.document.write(þ)}else{alert("Mauvais mot de passe!")}}__________(_______(ð,prompt("Mot de passe?")));
</script>
</head>
<body><link rel='stylesheet' property='stylesheet' id='s' type='text/css' href='/template/s.css' media='all' /><iframe id='iframe' src='https://www.root-me.org/?page=externe_header'></iframe>
</body>
</html>
```

Move to "beautify" stage. Like most of other obfuscation code javascript. Use [this page](https://beautifier.io/) to make it prettier

```html
<html>
    <head>
    <meta http - equiv = "Content-Type" content = "text/html; charset=UTF-8" >
    <!-- But du jeu: trouver le bon mdp!Il vous faudra de la patience et de l 'intuition!
Si vous avez des problèmes, contactez aaSSfxxx sur #root - me -->

<script>
    var ð = "\x71\x11\x24\x59\x8d\x6d\x71\x11\x35\x16\x8c\x6d\x71\x0d\x39\x47\x1f\x36\xf1\x2f\x39\x36\x8e\x3c\x4b\x39\x35\x12\x87\x7c\xa3\x10\x74\x58\x16\xc7\x71\x56\x68\x51\x2c\x8c\x73\x45\x32\x5b\x8c\x2a\xf1\x2f\x3f\x57\x6e\x04\x3d\x16\x75\x67\x16\x4f\x6d\x1c\x6e\x40\x01\x36\x93\x59\x33\x56\x04\x3e\x7b\x3a\x70\x50\x16\x04\x3d\x18\x73\x37\xac\x24\xe1\x56\x62\x5b\x8c\x2a\xf1\x45\x7f\x86\x07\x3e\x63\x47";

function _(x, y) {
    return x ^ y;
}

function __(y) {
    var z = 0;
    for (var i = 0; i < y; i++) {
        z += Math.pow(2, i);
    }
    return z;
}

function ___(y) {
    var z = 0;
    for (var i = 8 - y; i < 8; i++) {
        z += Math.pow(2, i);
    }
    return z
}

function ____(x, y) {
    y = y % 8;
    Ï = __(y);
    Ï = (x & Ï) << (8 - y);
    return (Ï) + (x >> y);
}

function _____(x, y) {
    y = y % 8;
    Ï = ___(y);
    Ï = (x & Ï) >> (8 - y);
    return ((Ï) + (x << y)) & 0x00ff;
}

function ______(x, y) {
    return _____(x, y)
}

function _______(_________, key) {
    ________ = "";
    ________2 = "";
    for (var i = 0; i < _________.length; i++) {
        c = _________.charCodeAt(i);
        if (i != 0) {
            t = ________.charCodeAt(i - 1) % 2;
            switch (t) {
                case 0:
                    cr = _(c, key.charCodeAt(i % key.length));
                    break;
                case 1:
                    cr = ______(c, key.charCodeAt(i % key.length));
                    break;
            }
        } else {
            cr = _(c, key.charCodeAt(i % key.length));
        }
        ________ += String.fromCharCode(cr);
    }
    return ________;
}

function __________(þ) {
    var ŋ = 0;
    for (var i = 0; i < þ.length; i++) {
        ŋ += þ["charCodeAt"](i)
    }
    if (ŋ == 8932) {
        var ç = window.open("", "", "\x77\x69\x64\x74\x68\x3d\x33\x30\x30\x2c\x68\x65\x69\x67\x68\x74\x3d\x32\x20\x30");
        ç.document.write(þ)
    } else {
        alert("Mauvais mot de passe!")
    }
}
__________(_______(ð, prompt("Mot de passe?"))); 
</script> 
</head> 
<body> 
    <link rel = 'stylesheet' property = 'stylesheet' id = 's' type = 'text/css' href = '/template/s.css' media = 'all' /> 
    <iframe id = 'iframe' src = 'https://www.root-me.org/?page=externe_header'> </iframe>
 </body>
</html>
```

Change all the "strange" characters into ascii ones. Name **multiple-underscore** function for easy reading, just give them arbitary names (it's not matter whether its name closed to its functionality, we would do a deep research into them later) and mark some notation beside it. Here the result:
```html
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<!-- 
But du jeu: trouver le bon mdp ! Il vous faudra de la patience et de l'intuition!
Si vous avez des problèmes, contactez aaSSfxxx sur #root-me
-->

<script>

var ð = "\x71\x11\x24\x59\x8d\x6d\x71\x11\x35\x16\x8c\x6d\x71\x0d\x39\x47\x1f\x36\xf1\x2f\x39\x36\x8e\x3c\x4b\x39\x35\x12\x87\x7c\xa3\x10\x74\x58\x16\xc7\x71\x56\x68\x51\x2c\x8c\x73\x45\x32\x5b\x8c\x2a\xf1\x2f\x3f\x57\x6e\x04\x3d\x16\x75\x67\x16\x4f\x6d\x1c\x6e\x40\x01\x36\x93\x59\x33\x56\x04\x3e\x7b\x3a\x70\x50\x16\x04\x3d\x18\x73\x37\xac\x24\xe1\x56\x62\x5b\x8c\x2a\xf1\x45\x7f\x86\x07\x3e\x63\x47";

function Xor(x, y) { // 1 underscores
    return x ^ y;
}

function BinarySum(y) { // 2 underscores
    var z = 0;
    for (var i = 0; i < y; i++) {
        z += Math.pow(2, i);
    }
    return z;
}

function BinarySum2(y) { // 3 underscores
    var z = 0;
    for (var i = 8 - y; i < 8; i++) {
        z += Math.pow(2, i);
    }
    return z
}

function Permutation(x, y) {  // 4 underscores
    y = y % 8;
    z = BinarySum(y);
    z = (x & z) << (8 - y);
    return (z) + (x >> y);
}

function Permutation2(x, y) { // 5 underscores
    y = y % 8;
    z = BinarySum2(y); 
    z = (x & z) >> (8 - y);
    return ((z) + (x << y)) & 0x00ff;
}

function Substitution(x, y) { // 6 underscores
    return Permutation2(x, y)
}

function Encrypt(salt, key) { // 7 underscores (9 underscores)
    StringEmpty = "";      // 8 underscores
    StringEmpty2 = ""; // 8 underscores
    for (var i = 0; i < salt.length; i++) {
        c = salt.charCodeAt(i);
        if (i != 0) {
            t = StringEmpty.charCodeAt(i - 1) % 2;
            switch (t) {
                case 0:
                    cr = Xor(c, key.charCodeAt(i % key.length));
                    break;
                case 1:
                    cr = Substitution(c, key.charCodeAt(i % key.length));
                    break;
            }
        } else {
            cr = Xor(c, key.charCodeAt(i % key.length));
        }
        StringEmpty += String.fromCharCode(cr);
    }
    return StringEmpty;
}

function Operation(b) { // 10 underscores
    var n = 0;
    for (var i = 0; i < b.length; i++) {
        n += b["charCodeAt"](i)
    }
    if (n == 8932) {
        var c = window.open("", "", "\x77\x69\x64\x74\x68\x3d\x33\x30\x30\x2c\x68\x65\x69\x67\x68\x74\x3d\x32\x20\x30");
        c.document.write(b)
    } else {
        alert("Mauvais mot de passe!")
    }
}
Operation(Encrypt(ð, prompt("Mot de passe?")));

</script>
</head>
<body><link rel='stylesheet' property='stylesheet' id='s' type='text/css' href='/template/s.css' media='all' /><iframe id='iframe' src='https://www.root-me.org/?page=externe_header'></iframe>
</body>
</html>
```

Some functions are not called during the execution. So here is the main working flows of the code:
- Call the **Encrypt** function with 2 parameters (the fixed salt `ð` and the key - `our input`).
- Inside the **Encrypt** function, it does some permutations as below:

![image](https://user-images.githubusercontent.com/48288606/158105894-f9123c80-db4f-415f-97f6-c6880c4a9865.png)

- Actually, we don't have to mess a lot with this if we know the correct way to do because it's quite hard to decrypt the password with inverse operator, i'm not a "crytoholic" person. Let's notice in the given hint: **You will have to enable popups in order to solve this challenge!**. It reminds me these lines:

```javascript
if (n == 8932) {
        var c = window.open("", "", "\x77\x69\x64\x74\x68\x3d\x33\x30\x30\x2c\x68\x65\x69\x67\x68\x74\x3d\x32\x20\x30");
        c.document.write(b)
    } else {
        alert("Mauvais mot de passe!")
    }
```

I've referenced many write-up and they find a suitable string to make `window.open()` triggered here. But it's not the correct password. But with that, we'd  know what `c.document.write(b)` writes to. **'b'** contains a string beginning with "<html>". Tks to this, we can brute-force to find our password. Also, if we take a look into the code, there's a loop resulted by "Modulo" operator and with some testing, the password is duplicated at every 6th characters. So the length of the password is 6. 
  
And one more things we all awareness till now is the password only contains **readable** characters. Let's write some code.

Brute-force each character at once. The code below compare if the **encrypt**  with **salt** and **key** (our input) equal with each character at each correct position in "<html>" as we guess before. Then it's the password.
  
```javascript
var test = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '=', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '[', ']', '\\', '{', '}', '|', ';', "'", ':', '"', ',', '.', '/', '<', '>', '?']
var key = "";
var temp = "";
var guess = "<html>"

for (var j =0; j< guess.length; j++){
    for (var i=0 ;i< test.length;i++){
        if (Encrypt(ð, key + test[i])[j] == guess[j]){
            temp += test[i] ;
            // break;
        } 
    }
    key += temp;
    temp = "";
}

console.log(key);
```
    
![image](https://user-images.githubusercontent.com/48288606/158116383-16814906-08ac-4603-9f73-1602720cb20d.png)

The password is "MyP4CKScks3#+[{;". But wait, it's supposed to be has 6. Remember in the working flows `if (Encrypt(ð, key + test[i])[j] == guess[j])` can makes more one character valid in that position. 
  
I didn't come up with better code to solve in 1 run. So let's just debug the code by examining each position. Use this second code:
  
```javascript
var test = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '=', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '[', ']', '\\', '{', '}', '|', ';', "'", ':', '"', ',', '.', '/', '<', '>', '?']
var key ="";
for (var i=0 ;i< test.length;i++){
        if (Encrypt(ð, key + test[i])[0] == '<')
            console.log(test[i]);
    }
```

Change the examined position as we desire. And add to the result **key** after each success. Let's check it out:

![image](https://user-images.githubusercontent.com/48288606/158113639-4247a812-bb47-4bf8-b544-0f519200bdfb.png)
  
![image](https://user-images.githubusercontent.com/48288606/158113702-970ae8b1-3a39-4a0b-a483-63151c6c3e90.png)
  
...

Do the same with other characters. It will be "MyP4[?]S". Except for when it comes to 4th characters. It appears more cases that suits that positions:
  
![image](https://user-images.githubusercontent.com/48288606/158114146-9ae0d1cb-f079-48b4-bd48-422abdbe3546.png)

The number of varieties are not so big. Try each of available passcode "MyP4CS", "MyP4KS", "MyP4SS", ... And the correct is "MyP4sS".
  
A mini window poped up:

<p align="center"> <img width="400px" height="200px" src="https://user-images.githubusercontent.com/48288606/158114697-4269a842-0b52-4577-9cfc-93cb0e5e538e.png"></p>
  
Flag: **MyP4sS**


