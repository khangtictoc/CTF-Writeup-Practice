# Level 0 ✔
- **Level Goal:**:<br>
The goal of this level is for you to log into the game using SSH. The host to which you need to connect is bandit.labs.overthewire.org, on port 2220. The username is bandit0 and the password is bandit0. Once logged in, go to the Level 1 page to find out how to beat Level 1.<br>
- **Commands you may need to solve this level:**<br>
ssh<br>
- **Helpful Reading Material:**<br>
[Secure Shell (SSH) on Wikipedia](https://en.wikipedia.org/wiki/Secure_Shell)<br>
[How to use SSH on wikiHow](https://www.wikihow.com/Use-SSH)<br>
- **Login SSH:**<br>
User: bandit0<br>
Pass: bandit0<br>
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

