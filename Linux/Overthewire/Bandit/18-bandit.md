# Level 17 - Level 18 ✔
- **Level Goal:**:<br>
The password for the next level is stored in a file readme in the homedirectory. Unfortunately, someone has modified .bashrc to log you out when you log in with SSH.<br>
**NOTE:** if you have solved this level and see ‘Byebye!’ when trying to log into bandit18, this is related to the next level, bandit19<br>
- **Commands you may need to solve this level:**<br>
ssh, ls, cat<br>                                        
- **Login SSH:**<br>
User: bandit17<br>
Pass: xLYVMN9WE5zQ5vHacb0sZEVqbrp7nBTn<br>
## Write-up: 📝<br>
In this chall, we ought to differentiate the content between 2 files<br>
Use `man diff` for more details
### Solution:<br>
- Compare 2 files: `diff password.new passwords.old`<br>
#### Password for next level: kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd 


