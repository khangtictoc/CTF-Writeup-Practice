# Level 4 - Level 5 ✔
- **Level Goal:**:<br>
The password for the next level is stored in the only human-readable file in the inhere directory. Tip: if your terminal is messed up, try the “reset” command.<br>
- **Commands you may need to solve this level:**<br>
ls, cd, cat, file, du, find<br>
ssh<br>
- **Login SSH:**<br>
User: bandit4<br>
Pass: pIwrPrtPN36QITSp3EQaw936yaFoFgAB<br>
## Write-up: 📝<br>
In this chall, we need to find the **human-readable** file in **inhere** dir<br>
Use `man file` for more details
### Solution:<br>
- List all hidden file<br>
Command: `ls -a`<br>
- Get into **"inhere"** directory
Command: `cd inhere`
- Find the **human-readable** file
Command: `file ./*`
File with "ASCII text" is the right one.
"./*" : means all the files in the current Dir
- Read that file
Command: `cat ./-file07 `
#### Password for next level: koReBOKuIDDepwhWk7jZC0RTdopnAYKh
