# Level 2 - Level 3 ✔
- **Level Goal:**:<br>
The password for the next level is stored in a file called spaces in this filename located in the home directory<br>
- **Commands you may need to solve this level:**<br>
ls, cd, cat, file, du, find<br>
ssh<br>
- **Helpful Reading Material:**<br>
[Google Search for “spaces in filename”](https://www.google.com/search?q=spaces+in+filename)<br>
- **Login SSH:**<br>
User: bandit2<br>
Pass: CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9<br>
## Write-up: 📝<br>
In this chall, we need to read a filename contain "space". Normally, when we use command (for example: cat) with " " in file name, they will split into 2 file , seperated by that space. So in this case, we have a special syntax to tell that this is one file with space contained<br>
Syntax: `cat '{file name with space}' `<br>
Alternative:<br>
`cat "{file name with space}" `<br>
`cat {file\ name\ with\ space} `<br>
### Solution:<br>
Command: `cat "spaces in this filename"`<br>
#### Password for next level: UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
