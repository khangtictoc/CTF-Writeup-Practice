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
In this chall, we have to connect to port 30000 on localhost and we have to send a string containing the current password. <br>
Like many previous chall again, with this **"cron"**, we have to know what **cron** file do to understand more about it: `cat  /etc/cron.d/cronjob_bandit24`<br>
![image](https://user-images.githubusercontent.com/48288606/135883049-56cee474-c244-49d5-be66-559b3c15f2d2.png)<br>
path of **/tmp/$mytarget**, which means we have to define **mytarget** variable<br>
### Solution:<br>
Cron content:<br>
![image](https://user-images.githubusercontent.com/48288606/135879735-c450ef4c-7bbf-4f64-bb97-59c94cdbdfa9.png)

#### Password for next level: BfMYroe26WYalil77FoDi9qh59eK5xNr 


