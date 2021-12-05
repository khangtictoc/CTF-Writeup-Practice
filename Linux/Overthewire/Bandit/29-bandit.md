# Level 29 - Level 30 ✔
- **Level Goal:**:<br>
There is a git repository at ssh://bandit29-git@localhost/home/bandit29-git/repo. The password for the user bandit28-git is the same as for the user bandit28.<br> 
Clone the repository and find the password for the next level.<br>
- **Commands you may need to solve this level:**<br>
git<br>
- **Login SSH:**<br>
User: bandit29<br>
Pass: bbc96594b4e001778eee9975372716b2<br>
## Write-up: 📝<br>
This level teach us about changing between branches.

### Solution:<br>
- Make a dir in **/tmp/{your_dir}**, then move to that path.<br>
Command: `git clone ssh://bandit29-git@localhost/home/bandit29-git/repo`<br><br>
![image](https://user-images.githubusercontent.com/48288606/144731740-a8edcbd6-2643-43bb-8b1f-161eff5ed8ec.png)
- Use the current password for level 29 to authenticate.
- Move to **repo** folder. Read "README" file. <br><br>
![image](https://user-images.githubusercontent.com/48288606/144731779-4c3ea26b-0fca-429c-bf94-d59a43eb2057.png)
- Type `git log`. <br><br>
![image](https://user-images.githubusercontent.com/48288606/144731827-839303e8-1f8a-4446-851f-4f0a5892141b.png)
- Each of these log is nothing special. View all the available branch `git branch -a`:<br><br>
![image](https://user-images.githubusercontent.com/48288606/144731849-3b1167cd-85a5-4097-a43b-b03dd7f35275.png)
- Move to **dev** branch. Command: `git checkout dev`
- View commit log. <br><br>
![image](https://user-images.githubusercontent.com/48288606/144731866-9979b035-2876-48f6-aaea-c430f431aabd.png)
- Examine the first commit. Command: `git show bc833286fca18a3948aec989f7025e23ffc16c07`<br><br>
![image](https://user-images.githubusercontent.com/48288606/144731881-3e545220-30ad-4b62-b578-29ab9fb1c063.png)

#### Password for next level: 5b90576bedb2cc04c86a9e924ce42faf 



