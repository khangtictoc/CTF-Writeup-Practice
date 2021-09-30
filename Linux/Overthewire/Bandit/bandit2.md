# Level 1 - Level 2 ✔
- **Level Goal:**:<br>
The password for the next level is stored in a file called - located in the home directory<br>
- **Commands you may need to solve this level:**<br>
ssh<br>
- **Helpful Reading Material:**<br>
[Google Search for “dashed filename”](https://www.google.com/search?q=dashed+filename)<br>
[Advanced Bash-scripting Guide - Chapter 3 - Special Characters](https://tldp.org/LDP/abs/html/special-chars.html)<br>
- **Login SSH:**<br>
User: bandit1<br>
Pass: boJ9jbbUNNfktd78OOpsqOltutMc3MY1<br>
## Write-up: 📝<br>
In this chall, we just connect remotely to their server by using "ssh" with user:bandit0 & password:bandit0 <br>
Use `man ssh` for more details<br>
### Solution:<br>
Command: `ssh   bandit.labs.overthewire.org -l bandit0 -p 2220`<br>
With<br>
-l: choose user to login<br>
-p: port to connect<br>
### Other Solution:<br>
For shorter, we can use:<br>
Syntax: `ssh user@host -l port`<br>
Command: `ssh   bandit0@bandit.labs.overthewire.org -p 2220`<br>
#### Password for next level: boJ9jbbUNNfktd78OOpsqOltutMc3MY1
