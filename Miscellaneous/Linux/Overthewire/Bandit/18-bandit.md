# Level 18 - Level 19 ✔
- **Level Goal:**:<br>
The password for the next level is stored in a file readme in the homedirectory. Unfortunately, someone has modified .bashrc to log you out when you log in with SSH.<br>
**NOTE:** if you have solved this level and see ‘Byebye!’ when trying to log into bandit18, this is related to the next level, bandit19<br>
- **Commands you may need to solve this level:**<br>
ssh, ls, cat<br>                                        
- **Login SSH:**<br>
User: bandit18<br>
Pass: kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd<br>
## Write-up: 📝<br>
In this chall, we are kicked out when we login by "ssh". We can solve this chall by force another type of terminal to be allocated<br>
Use `man ssh` for more details
### Solution:<br>
- We **ssh** and use special flag "-t" to **force the pseudo-terminal allocation(PTY)**: `ssh -t bandit.labs.overthewire.org -l bandit18 -p 2220 /bin/sh`<br>
Here, i use the "TTY" terminal, its path is **/bin/sh**<br>
- Then `cat` **readme** file
### Other solution:<br>
We can use "-T" flag to disable the PTY allocation and communicate with shell, then the rest is similar. 
#### Password for next level: IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x 


