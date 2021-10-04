# Level 21 - Level 22 ✔
- **Level Goal:**:<br>
A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.<br>
- **Commands you may need to solve this level:**<br>
cron, crontab, crontab(5) (use “man 5 crontab” to access this)<br>                                        
- **Login SSH:**<br>
User: bandit21<br>
Pass: gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr<br>
## Write-up: 📝<br>
In this chall, we have to read the content of the **cron** file to understand more about it.<br>
### Solution:<br>
- We take a look in cron workng path **/etc/cron.d/** and read the file for the bandit22
- Then, in the output, we know that system do something regularly with **/usr/bin/cronjob_bandit23.sh**. Try "Cat(ing)" it
![image](https://user-images.githubusercontent.com/48288606/135829002-32763a45-64b8-4fa1-bf71-c455506880ef.png)
- Now we see, they're doing the `chmod` command with **/tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv** file, then copy the password of bandit22 from **/etc/bandit_pass/bandit22** to there.
- So we just need to read the content in **/tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv**
#### Password for next level: Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI 


