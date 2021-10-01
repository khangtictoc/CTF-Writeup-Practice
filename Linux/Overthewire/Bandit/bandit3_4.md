# Level 3 - Level 4 ✔
- **Level Goal:**:<br>
The password for the next level is stored in a hidden file in the inhere directory.<br>
- **Commands you may need to solve this level:**<br>
ls, cd, cat, file, du, find<br>
ssh<br>
- **Login SSH:**<br>
User: bandit3<br>
Pass: UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK<br>
## Write-up: 📝<br>
In this chall, we need to list all the file (include hidden file) in the current location <br>
Use `man ls` and `man cd` for more details
### Solution:<br>
- List all hidden file<br>: `ls -a`<br>
- Get into **"inhere"** directory: `cd inhere`
- List all hidden file: `ls -a`<br>
- Cat **".hidden"** file: `cat .hidden`

#### Password for next level: pIwrPrtPN36QITSp3EQaw936yaFoFgAB
