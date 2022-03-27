# SQL injection - Authentication - GBK

**Title**: Do you speak chinese ?

**Point**: 30 Points 

**Description:** Get an administrator access.

## Solution:

Enter site. There's a login form.

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/160287236-efb8d3f9-4e61-4d13-9401-393aee4035d2.png"></p>

Move to "Liste des membres" (List of members) . This shows only 1 account and this is **admin** user as well. So login form need to be bypassed:

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/160287421-b19261b3-6ec7-4317-babf-24839e5abcd7.png"></p>

**NOTE: In this chall, we only attack on "first input box". The second is not vulnerable.**

Try simple payload:

```
admin' or 1=1 -- 
``` 

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/160287699-06189e43-edca-42ab-8cb1-24a7c1c5cf84.png"></p>

A message Erreur d'identification (Misidentification). Remember the **title** "Do you speak chinese ?" and the challenge's name somehow relate to **GBK**. After "googling" a lot, we know that this things a character encoding for Chinese. 

[Main reference](https://en.wikipedia.org/wiki/GBK_(character_encoding)#cite_note-gb18030-2005-7). And this also relates to a tip called "Bypassing the addslash()". Now, everything is clear! Our input with any characters like double quotes `"`, single quotes `'` or backslashes `\` will be added with 1 more backslashes `\` before them, which will escape the characters and make our query wrong.

Our main mission is bypass it ! Luckily, they hint us we use a method call **multibyte character set**, some of these is `Shift-jis`, `jis`, `euc-jp`, `euc-kr`, ... And our popular type which the challenge recommend us to use is **GBK**. Our main idea is we add a **character** have a url-encoded form like `%xx` and add our single quote `'` (%27) to escape string. And when the server add backslashes `\`(%5C), which will construct a multi-byte string that we call "GBK character". It means we indirectly delete backslashes `\` base on **Constructing GBK characters**.

Our payload will has a form of:

`%xx%27 or 1=1 -- ` -> Equivalent to `%xx' or 1=1 -- `

When server add **backslash** `\` (**%5C**):

`(%xx%5C)%27 or 1=1 -- ` -> Equivalent to `%xx\' or 1=1 --`

And **%xx%5C** will create a **GBK character**. So server will take our payload as: `{character}' or 1=1 -- ` 

So which's the character should we add ? Follow the table how **GDB characters** are encoded from the reference link above.

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/160288832-7abb3605-26ea-4e41-9bc3-f53381031107.png"></p>

**%5C** `\` with add before **%27** `'` and will be the second byte. Our first byte is optional, as long as it's in satisfied range. 

For example, I choose **%AB** for our payload. We can check it if it's a valid **Chinese** characterby convert **%AB%5C** -> `«\` (Unicode char). Use BurpSuite to decode). 

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/160289127-c5323ebe-a522-48f6-984e-72d5e942f048.png"></p>

Use [This site](https://www.njstar.com/cms/cjk-code-to-unicode-conversion) to convert:

We will see `«\` is convert to `玕`. So our paylod in server side is like: `玕' or 1=1 -- `. This will bypass the form.

We use "Burp Suite" to send our encoded payload. Use directly normal browser may "hard" to send right encoded character like "%AB" or "%27". Besides, the form use "POST" method so we could easily change our payload in **POST Request.**. Turn on **Intercept**, enter:

Login: `123`

Password: `123`

Then submit form. In **captured request**, change `login`'s value to `%ab%27 or 1=1 -- `  like below:

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/160289576-91b1a06b-b882-4f3a-9dfe-ef2a98f5d135.png"></p>

Then forward request:

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/160289619-fc214eb3-8ab0-4b77-a027-bbec890ee38e.png"></p>

Final payload: 

```
%ab%27 or 1=1 -- 
```

**NOTE: If anyone find better way to check our 2-bytes GBK character is valid. I'm pleased to learn with you**

Flag: **iMDaFlag1337!**
