# Level 27 - Level 28 ✔
- **Level Goal:**:<br>
There is a git repository at ssh://bandit27-git@localhost/home/bandit27-git/repo. The password for the user bandit27-git is the same as for the user bandit27<br> 
Clone the repository and find the password for the next level.<br>
- **Commands you may need to solve this level:**<br>
git<br>
- **Login SSH:**<br>
User: bandit27<br>
Pass: 3ba3118a22e93127a4ed485be72ef5ea<br>
## Write-up: 📝<br>
This level teach us about using git to clone a repository from github.

### Solution:<br>
- Make a dir in **/tmp/{your_dir}**, then move to that path.
Command: `git clone ssh://bandit27-git@localhost/home/bandit27-git/repo`<br>
![image](https://user-images.githubusercontent.com/48288606/144731242-939fa7ef-a7e7-4779-8079-c973da52a483.png)
- Use the current password for level 27 to authenticate.
- Move to **repo** folder.
- Read "README"

#### Password for next level: 0ef186ac70e04ea33b4c1853d2526fa2 



