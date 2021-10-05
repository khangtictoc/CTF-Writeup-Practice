# Level 23 - Level 24 ✔
- **Level Goal:**:<br>
A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.<br>
**NOTE 1:** This level requires you to create your own first shell-script. This is a very big step and you should be proud of yourself when you beat this level!<br>
**NOTE 2:** Keep in mind that your shell script is removed once executed, so you may want to keep a copy around…<br>
- **Commands you may need to solve this level:**<br>
cron, crontab, crontab(5) (use “man 5 crontab” to access this)<br>                                               
- **Login SSH:**<br>
User: bandit23<br>
Pass: jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n<br>
## Write-up: 📝<br>
Like many previous chall again, with this **"cron"**, we have to know what **cron** file do to understand more about it: `cat  /etc/cron.d/cronjob_bandit24`<br>
And then "cat" the relevant file:<br>
![image](https://user-images.githubusercontent.com/48288606/135885637-8b218ded-bbbe-42b9-987b-383d4e65ef6d.png)<br>
### Solution:<br>
Look carefully at the content above. This is what the "shell script" do:
1. Move to the path **/var/spool/$myname** , which the current user **whoami** 's assigned to $myname.
2. Do a "for" loop in the files with and without extension **\* .\*** 
#### Password for next level: BfMYroe26WYalil77FoDi9qh59eK5xNr 


