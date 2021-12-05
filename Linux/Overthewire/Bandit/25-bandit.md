# Level 25 - Level 26 ✔
- **Level Goal:**:<br>
Logging in to bandit26 from bandit25 should be fairly easy… The shell for user bandit26 is not /bin/bash, but something else. Find out what it is, how it works and how to break out of it.<br>               
- **Commands you may need to solve this level:**<br>
ssh, cat, more, vi, ls, id, pwd<br>
- **Login SSH:**<br>
User: bandit25<br>
Pass: uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG<br>
## Write-up: 📝<br>
In this chall, we log into the chall and find a ssh private key to the next level. But the interesting issue here is when ssh to **bandit26**, the system is closed. <br>
![image](https://user-images.githubusercontent.com/48288606/136666207-c15e8bd5-647c-4815-b798-f4bbaa9c9d6e.png)<br>
The description also gave clues about seeing the current **bandit26** user 's shell, we can reach this by read the **/etc/passwd** file: `cat /etc/passwd | grep bandit26`<br><br>
![image](https://user-images.githubusercontent.com/48288606/144730318-eb4e0ce5-7205-4aa2-99de-f322f1eccf49.png)

Then we take a look into the **/usr/bin/showtext** and see what inside it: <br>
![image](https://user-images.githubusercontent.com/48288606/136666316-6bd6d637-143e-427a-a3a2-98d9d914d103.png)<br>
This is a bash script which do the followings:<br>
- Assign a environment variable<br>
- Read ~/text.txt by `more` command<br>
- Then exit the system<br>
Yeah, the most important things in the code is when this shell is called. The script above will run and terminate the system by `exit 0` at the end.<br>
### Solution:<br>
The solution for this is in the `more` command.<br>
- Read the `more` command for more details<br>
- And we leverage its function with a unbelievable way, which `more` command it will terminate the program temporarily when the content is wrapped in a smaller-size view box. You can test it with a long-content file.<br>
- Rescaling the terminal before login the server. Then just ssh:<br>
![image](https://user-images.githubusercontent.com/48288606/136666710-bbd61c09-f9c6-4d07-b220-b0dc62c75840.png)<br>
- After that, we will use vim to read the password file from here. Why **"Vim"**? 'Cause it give a possibility to execute basic command when move to **command mode** to help us read the password in bandit26. Open vim: `vi`<br>
- Once get into vim workplace, make sure enter **command mode** by pressing **"Escape"** button. Then type: `:e /etc/bandit_pass/bandit26`. (:e means that the file that you're editing has been written to by another program.)<br>
Note 1: You can explore the official document about vim [here](https://vimhelp.org/cmdline.txt.html#Command-line) or [this](https://web.stanford.edu/class/archive/cs/cs107/cs107.1218/resources/vim.html) for more easily understanding and quick use. <br>
Note 2: You can't use the trick from Level 18-19 because this is non standard shell. Non-standard is defined as a shell not found in `/etc/shells.`<br>
- Enjoy the password !!!<br>
![image](https://user-images.githubusercontent.com/48288606/136666032-c4fac803-0d15-4ffe-9315-75d58586bd4c.png)<br>

#### Password for next level: 5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z 


