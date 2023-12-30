# Level 32 - Level 33 ✔
- **Level Goal:**:<br>
After all this git stuff its time for another escape. Good luck!<br> 

- **Commands you may need to solve this level:**<br>
sh, man<br>
- **Login SSH:**<br>
User: bandit32<br>
Pass: 56a9bf19c63d650ce78e6ec0354ee45e<br>
## Write-up: 📝<br>
When we log in to the system. We'll receive A UPPERCASE SHELL. THE UPPERCASE SHELL is converting every command into uppercase.

### Solution:<br>

- Type `$0`. <br><br>
![image](https://user-images.githubusercontent.com/48288606/144734738-d4996dd7-edfe-448c-98b1-1f44f48babea.png)
Note: `$0` receive the first argurment as a shell command. So this command will open a shell
- In the current path, we could see **uppershell** file. Run this file will open the UPPERCASE SHELL.<br><br>
![image](https://user-images.githubusercontent.com/48288606/144734805-33486fe8-abcc-45b5-a52d-5e2c4d430f27.png)
- Use `echo $SHELL` to view the current shell <br>
Note: [See and change the current shell](https://www.cyberciti.biz/tips/how-do-i-find-out-what-shell-im-using.html).<br>
As the output shown, we're using the shell in the path **/home/bandit32/uppershell**. 
Note: Being aware that changing shell methods in the reference above is not working cause it just takes effect when logging out and logging in again.
- With the current shell, we can read the password for next challenge<br>
Command: `cat /etc/bandit_pass/bandit33`

#### Password for next level:  c9c3199ddf4121b10cf581a98d51caee



