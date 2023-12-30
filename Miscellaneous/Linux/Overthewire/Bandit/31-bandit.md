# Level 31 - Level 32 ✔
- **Level Goal:**:<br>
There is a git repository at ssh://bandit31-git@localhost/home/bandit31-git/repo. The password for the user bandit31-git is the same as for the user bandit31.<br> 
Clone the repository and find the password for the next level.<br>
- **Commands you may need to solve this level:**<br>
git<br>
- **Login SSH:**<br>
User: bandit31<br>
Pass: 47e603bb428404d265f59c42920d81e5<br>
## Write-up: 📝<br>
This level teach us about pushing a file to remote repo.

### Solution:<br>
- Make a dir in **/tmp/{your_dir}**, then move to that path.<br>
Command: `git clone ssh://bandit31-git@localhost/home/bandit31-git/repo`<br><br>
![image](https://user-images.githubusercontent.com/48288606/144733105-6d078c82-834e-48db-a86e-100ad6e1f6d9.png)
- Use the current password for level 31 to authenticate.
- Move to **repo** folder. Read "README" file. But the file is empty.<br><br>
![image](https://user-images.githubusercontent.com/48288606/144733117-0ad109b3-623a-4476-a45b-e0f1c7c144b4.png)<br>
We have to push a file with above information to remote repository. Check branch, tag and remote path: <br><br>
![image](https://user-images.githubusercontent.com/48288606/144733505-f62b57f4-3426-41a6-8b3f-96d162cf987d.png)<br>
Overview of Github workflow:<br><br>
![image](https://user-images.githubusercontent.com/48288606/144733449-9310a9f6-78da-4713-bced-c1223e4a50dd.png)
- Create a new file that meets the requirements. <br>
Command: `echo "May I come in?" > key.txt`
- Add file to staging area.<br><br>
![image](https://user-images.githubusercontent.com/48288606/144733347-2509c63d-4c47-4dea-bf00-888a813b8c71.png)<br>
Add "-f" flag. Command: `git add -f  key.txt `
- Commit file to local repo <br>
Command :`git commit -m "New commit"`<br>
- Push the file to remote repo <br>
Command: `git push -u origin master`

#### Password for next level: 56a9bf19c63d650ce78e6ec0354ee45e 



