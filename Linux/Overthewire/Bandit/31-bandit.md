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
Command: `git clone ssh://bandit30-git@localhost/home/bandit30-git/repo`<br><br>
![image](https://user-images.githubusercontent.com/48288606/144731989-7f73105f-db01-4b3f-b5ee-f76e75e18a49.png)
- Use the current password for level 30 to authenticate.
- Move to **repo** folder. Read "README" file. But the file is empty.<br><br>
![image](https://user-images.githubusercontent.com/48288606/144732000-b0378b96-5a56-4fc4-ba6d-2ca918a8f544.png)
- Examining logs. <br><br>
![image](https://user-images.githubusercontent.com/48288606/144732050-938a018c-c597-4cf1-926f-538ddc756cef.png)<br>
It's just a normal commit when creating a new repo with README file<br>
Let's check information in **".git"** folder. **".git"** folder is created by `git init` (https://git-scm.com/docs/git-init). 
Files in **".git"** gives much information, configuration, ... about a repository. (See [What's in .git folder](https://stackoverflow.com/questions/29217859/what-is-the-git-folder)
- View all available branches <br><br>
![image](https://user-images.githubusercontent.com/48288606/144732782-984632d1-4987-4bf9-80f8-b2218584a04d.png)<br>
There's only 1 branch.<br>
- Move to **".git"** folder and have a look in **packed-refs**. We attempt to find more references in this file. <br><br>
![image](https://user-images.githubusercontent.com/4847e603bb428404d265f59c42920d81e58606/144732438-d4b79914-f2ec-466f-98f5-7bf84ef9f85d.png)
- View the secret: <br><br>
![image](https://user-images.githubusercontent.com/48288606/144732453-b6cbd66b-a0b2-41f3-85d3-6dc5079bc636.png)
Note: [Learn about packed-refs](https://git-scm.com/docs/git-pack-refs) 

#### Password for next level: 47e603bb428404d265f59c42920d81e5 



