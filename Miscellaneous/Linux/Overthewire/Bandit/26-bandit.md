# Level 26 - Level 27 ✔
- **Level Goal:**:<br>
Good job getting a shell! Now hurry and grab the password for bandit27!<br>               
- **Commands you may need to solve this level:**<br>
ls<br>
- **Login SSH:**<br>
User: bandit26<br>
Pass: 5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z<br>
## Write-up: 📝<br>


### Solution:<br>

In this chall, when ssh to bandit26, the system is closed. Accourding to described hints, we should open the shell while in vim like in level 25.

Just like the previous challenge, we examined that the system is shut down when we try to log in. So we try to open a shell through vim while being "in" `more` command.
- Minimize the window as small as possible.
- Press "v" to enter **Vim**
- In command mode, input `:shell` to open a shell. But nothing happens so we have to set the shell by `:set shell=/bin/bash` (we can also use **/bin/sh** shell)
- Now we type `:shell`, it works. List all file in current path. <br><br>
![image](https://user-images.githubusercontent.com/48288606/144730722-3a7af5dc-fbe3-41d0-a9ab-32d96adebb11.png)
- With **bandit27-do**, we can read the password the next challenge. <br> 
Command `./bandit27-do cat /etc/bandit_pass/bandit27`

#### Password for next level: 3ba3118a22e93127a4ed485be72ef5ea 



