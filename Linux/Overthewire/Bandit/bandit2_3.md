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
In this chall, we need to read a so-called "dashed" filename.Normally, the "-" sign specify the parameter in the command. So we have to use a special syntax to differentiate between this.  <br>
Syntax: `cat ./{(-)filename}` or `cat <(-)filename`<br>
### Solution:<br>
Command: `cat ./-`<br>
#### Password for next level: CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
