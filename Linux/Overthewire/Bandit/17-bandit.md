# Level 17 - Level 18 ✔
- **Level Goal:**:<br>
There are 2 files in the homedirectory: passwords.old and passwords.new. The password for the next level is in passwords.new and is the only line that has been changed between passwords.old and passwords.new<br>
NOTE: if you have solved this level and see ‘Byebye!’ when trying to log into bandit18, this is related to the next level, bandit19<br>
- **Commands you may need to solve this level:**<br>
cat, grep, ls, diff<br>                                        
- **Login SSH:**<br>
User: bandit17<br>
Pass: xLYVMN9WE5zQ5vHacb0sZEVqbrp7nBTn<br>
## Write-up: 📝<br>
In this chall, we ought to differentiate the content between 2 files<br>
Use `man diff` for more details
### Solution:<br>
- Compare 2 files: `diff password.new passwords.old`<br>
#### Password for next level: kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd 

