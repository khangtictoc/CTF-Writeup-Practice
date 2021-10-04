# Level 22 - Level 23 ✔
- **Level Goal:**:<br>
A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.<br>
**NOTE:** Looking at shell scripts written by other people is a very useful skill. The script for this level is intentionally made easy to read. If you are having problems understanding what it does, try executing it to see the debug information it prints.<br>
- **Commands you may need to solve this level:**<br>
cron, crontab, crontab(5) (use “man 5 crontab” to access this)<br>                                        
- **Login SSH:**<br>
User: bandit22<br>
Pass: Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI<br>
## Write-up: 📝<br>
Like previous chall, we have to know what **cron** file do to understand more about it: `cat  /etc/cron.d/cronjob_bandit23`<br>
![image](https://user-images.githubusercontent.com/48288606/135883049-56cee474-c244-49d5-be66-559b3c15f2d2.png)
Again, we know we need to read **bash script** in the path **/usr/bin/cronjob_bandit23.sh**. But in this level, its difficult has been enhanced. We should find out the unfolded path of **/tmp/$mytarget**, which means we have to define **mytarget** variable<br>
### Solution:<br>
![image](https://user-images.githubusercontent.com/48288606/135879735-c450ef4c-7bbf-4f64-bb97-59c94cdbdfa9.png)
- Well, with bash script, the best way to handle it is using **DEBUG** each line and watch the result.<br>
- First, we copy and paste the first command: `myname=$(whoami)` then we print its value: `echo $myname`. We get **bandit22**. But in this chall, we need to reassign that value to "bandit23" for next level<br>
![image](https://user-images.githubusercontent.com/48288606/135881825-f3860352-dde7-4a27-98ae-62570a7edc38.png)
- Then, we copy and paste the second command. `mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)`. Examine the final value: **$mytarget**'s value:`echo $mytarget`. <br>
![image](https://user-images.githubusercontent.com/48288606/135882068-00dcd8fe-f8e1-4e1a-a9bd-7458de1575f5.png)
- Finally, we just read the fullpath file: `cat /tmp/8ca319486bfbbc3663ea0fbe81326349`
#### Password for next level: jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n 



