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
Look carefully at the content above. This is what the "shell script" do:<br>
1. Move to the path **/var/spool/$myname** , which the current user **whoami** 's assigned to $myname.<br>
2. Do a "for" loop in the files with and without extension (**\* .\***):<br>
`for i in * .*;`<br>
Remember the syntax: "* .*"<br>
3. With each loop, it'll consider the special case whether that files is "." or ".." , it'll skip<br>
`f [ "$i" != "." -a "$i" != ".." ];`<br> 
4. At last, it check one more condition, if it's a file owned by user "bandit23" then it will execute and remove it every 60 seconds
`owner="$(stat --format "%U" ./$i)"`<br>
`    if [ "${owner}" = "bandit23" ]; then`<br>
`        timeout -s 9 60 ./$i`<br>
`    fi`<br>
`    rm -f ./$i`<br>
### Solution:<br>
In this chall, we have to think a little bit to solve. The easiest way I can come up with is write a file read the password from next level and i will let that cron file do that for me.<br>
- First, we should create a working dir in /tmp/{yourfolder}: `mkdir /tmp/khang123` and move to there `cd /tmp/khang123`<br>
- Then, the **NOTE** said, we need to write your own bash script here, in this case, i use **Vim** to create and edit : `vim solve.sh`<br>
- Write the following script:<br>
`#! /bin/bash`<br>
`cat /etc/bandit_password/bandit24 > /tmp/khang123/passwd.txt`<br>
▸ #! /bin/bash specify this is a bash script<br>
▸ Next line means we get the password and put it in file **/tmp/khang123/passwd.txt** once this file is executed<br>
- Then save it by `Esc` to escape mode and type `:x` (in **Vim**)<br>
- One more important thing we have to do is change the mode of the file so that other users can execute it (here is **cron**) <br>
`chmod 777 solve.sh` and `chmod 777 passwd.txt` <br>
- In the end, copy that script to the destination where files're handled: <br>
`cp solve.sh /var/spool/bandit24`<br>
- Wait at most 60 seconds for the cron do its work.<br>
- Check the passwd.txt <br>
✌: According to the chall said, I should be proud of myself. And I did !!! 😎
#### Password for next level: UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 
