# Level 4 - Level 5 ✔
- **Level Goal:**:<br>
The password for the next level is stored in the only human-readable file in the inhere directory. Tip: if your terminal is messed up, try the “reset” command.<br>
- **Commands you may need to solve this level:**<br>
ls, cd, cat, file, du, find<br>
ssh<br>
- **Login SSH:**<br>
User: bandit3<br>
Pass: pIwrPrtPN36QITSp3EQaw936yaFoFgAB<br>
## Write-up: 📝<br>
In this chall, we need to list all the file (include hidden file) in the current location <br>
Use `man ls` and `man cd` for more details
### Solution:<br>
- List all hidden file<br>
Command: `ls -a`<br>
- Get into **"inhere"** directory
Command: `cd inhere`
- List all hidden file<br>
Command: `ls -a`<br>
- Cat **".hidden"** file
Command: `cat .hidden`

#### Password for next level: CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
