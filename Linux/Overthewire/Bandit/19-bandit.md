# Level 19 - Level 20 ✔
- **Level Goal:**:<br>
To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.<br>
NOTE: if you have solved this level and see ‘Byebye!’ when trying to log into bandit18, this is related to the next level, bandit19<br>
- **Helpful Reading Material**<br>
[setuid on Wikipedia](https://en.wikipedia.org/wiki/Setuid)<br>                                   
- **Login SSH:**<br>
User: bandit19<br>
Pass: IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x<br>
## Write-up: 📝<br>
Setuid binary files specify the permission(read, write, execute) of some kind of user to a file. In this chall, we have to read the password for next challenge using a this kind of files<br>
### Solution:<br>
- Execute the file as challenge suggested : `./bandit20-do` <br>
Result: <br>
`Run a command as another user.<br>
  Example: ./bandit20-do id`
- So as a hint, then just combine with `cat` command to read the password: `./bandit20-do cat /etc/bandit_pass/bandit20`<br>
#### Password for next level: GbKksEFF4yrVs6il55v6gwY5aVje5f0j 


