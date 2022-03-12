# Javascript - Obfuscation 3

**Point:** 30 Points

## Solution:

A pop-up requires password.

<p align="center"><img width="400px" height="150px" src="https://user-images.githubusercontent.com/48288606/158011946-b05d566e-d83e-42a5-88c1-1d5e22ea7ab9.png" /> </p>

Whatever we input, the same result returns:

<p align="center"><img width="450px" height="150px" src="https://user-images.githubusercontent.com/48288606/158011980-e7dee0e1-7d51-43e7-b05f-33a2e90226e6.png" /> </p>

Open "Developer Tools" -> Source -> ch13.html :

```html
<html>
<head>
    <title>Obfuscation JS</title>
    <script type="text/javascript">
    function dechiffre(pass_enc){
        var pass = "70,65,85,88,32,80,65,83,83,87,79,82,68,32,72,65,72,65";
        var tab  = pass_enc.split(',');
                var tab2 = pass.split(',');var i,j,k,l=0,m,n,o,p = "";i = 0;j = tab.length;
                        k = j + (l) + (n=0);
                        n = tab2.length;
                        for(i = (o=0); i < (k = j = n); i++ ){o = tab[i-l];p += String.fromCharCode((o = tab2[i]));
                                if(i == 5)break;}
                        for(i = (o=0); i < (k = j = n); i++ ){
                        o = tab[i-l]; 
                                if(i > 5 && i < k-1)
                                        p += String.fromCharCode((o = tab2[i]));
                        }
        p += String.fromCharCode(tab2[17]);
        pass = p;return pass;
    }
    String["fromCharCode"](dechiffre("\x35\x35\x2c\x35\x36\x2c\x35\x34\x2c\x37\x39\x2c\x31\x31\x35\x2c\x36\x39\x2c\x31\x31\x34\x2c\x31\x31\x36\x2c\x31\x30\x37\x2c\x34\x39\x2c\x35\x30"));
    
    h = window.prompt('Entrez le mot de passe / Enter password');
    alert( dechiffre(h) );
    
</script>
</head>

</html>
```
The code above is little "messy". It do obfuscation on our password , return a "faux password"; therefore, a false password pop-up. Well, I really don't know exactly the target of the challenge but this line may be contains password 

```html
 String["fromCharCode"](dechiffre("\x35\x35\x2c\x35\x36\x2c\x35\x34\x2c\x37\x39\x2c\x31\x31\x35\x2c\x36\x39\x2c\x31\x31\x34\x2c\x31\x31\x36\x2c\x31\x30\x37\x2c\x34\x39\x2c\x35\x30"));
```
So i **unescape** and convert to ascii char: 

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/158012242-02c874b4-a43e-4eb1-afe2-8e9f5ebd2925.png" /></p> 

There's no way to confirm the password cuz there's no clue. Just submit it and bang, that's the password !

Flag: **786OsErtk12**
 

