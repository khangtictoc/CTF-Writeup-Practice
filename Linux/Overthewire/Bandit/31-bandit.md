# Level 31 - Level 32 ✔
- **Level Goal:**:<br>
There is a git repository at ssh://bandit31-git@localhost/home/bandit31-git/repo. The password for the user bandit28-git is the same as for the user bandit31.<br> 
Clone the repository and find the password for the next level.<br>
- **Commands you may need to solve this level:**<br>
git<br>
- **Login SSH:**<br>
User: bandit31<br>
Pass: 47e603bb428404d265f59c42920d81e5<br>
## Write-up: 📝<br>
This level teach us about using git to view commit log.

### Solution:<br>
- Make a dir in **/tmp/{your_dir}**, then move to that path.<br>
Command: `git clone ssh://bandit31-git@localhost/home/bandit31-git/repo`<br><br>
![image](https://user-images.githubusercontent.com/48288606/144733105-6d078c82-834e-48db-a86e-100ad6e1f6d9.png)
- Use the current password for level 31 to authenticate.
- Move to **repo** folder. Read "README" file. But the file is empty.<br><br>
![image](https://user-images.githubusercontent.com/48288606/144733117-0ad109b3-623a-4476-a45b-e0f1c7c144b4.png)


#### Password for next level: 47e603bb428404d265f59c42920d81e5 



