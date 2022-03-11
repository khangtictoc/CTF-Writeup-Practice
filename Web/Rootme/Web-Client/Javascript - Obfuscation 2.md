# Javascript - Obfuscation 2

**Point:** 10 Points

**Description:** Going down 3 floors.....

## Solution:

Just an empty page. Open "Developer Tools" -> Source -> ch12.html

```html
<html>

<head>
	<title>Obfuscation JS</title>
<!-- 
Obfuscation 
.Niveau : Facile 
.By Hel0ck
.The mission : 
	Retrouver le password contenu dans la var pass.
	You need my help ? IRC : irc.root-me.org #root-me
-->
<script type="text/javascript">
	var pass = unescape("unescape%28%22String.fromCharCode%2528104%252C68%252C117%252C102%252C106%252C100%252C107%252C105%252C49%252C53%252C54%2529%22%29");
</script>
</head>

</html>
```
Look at the source code. We know that the password is also the flag and the var **pass** contain it. Let's figure it out by 'unescaping' from outside , take the following onto console:
- `unescape("unescape%28%22String.fromCharCode%2528104%252C68%252C117%252C102%252C106%252C100%252C107%252C105%252C49%252C53%252C54%2529%22%29");` . The result still has '%' and **unescape** function.
- `'unescape("String.fromCharCode%28104%2C68%2C117%2C102%2C106%2C100%2C107%2C105%2C49%2C53%2C54%29")'`. Now the result is out of "%".
- `String.fromCharCode(104,68,117,102,106,100,107,105,49,53,54)`. Now it returns **hDufjdki156** - this is the flag

Flag: **hDufjdki156**
