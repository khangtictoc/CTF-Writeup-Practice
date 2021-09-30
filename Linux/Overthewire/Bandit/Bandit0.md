# Level 0 ✔
- **Level Goal:**:<br>
The goal of this level is for you to log into the game using SSH. The host to which you need to connect is bandit.labs.overthewire.org, on port 2220. The username is bandit0 and the password is bandit0. Once logged in, go to the Level 1 page to find out how to beat Level 1.<br>
- **Commands you may need to solve this level:**<br>
ssh<br>
- **Helpful Reading Material:**<br>
[Secure Shell (SSH) on Wikipedia](https://en.wikipedia.org/wiki/Secure_Shell)<br>
[How to use SSH on wikiHow](https://www.wikihow.com/Use-SSH)<br>
## Write-up: 📝<br>
In this chall, we just connect remotely to their server by using "ssh" <br>
`ssh   bandit.labs.overthewire.org -l bandit0 -p 2220`<br>
With -l: choose user to login<br>
     -p: port to connect<br>
