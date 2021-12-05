# Level 28 - Level 29 ✔
- **Level Goal:**:<br>
There is a git repository at ssh://bandit28-git@localhost/home/bandit28-git/repo. The password for the user bandit28-git is the same as for the user bandit28.<br> 
Clone the repository and find the password for the next level.<br>
- **Commands you may need to solve this level:**<br>
git<br>
- **Login SSH:**<br>
User: bandit28<br>
Pass: 0ef186ac70e04ea33b4c1853d2526fa2<br>
## Write-up: 📝<br>
This level teach us about using git to view commit log.

### Solution:<br>
- Make a dir in **/tmp/{your_dir}**, then move to that path.<br>
Command: `git clone ssh://bandit28-git@localhost/home/bandit28-git/repo`<br><br>
![image](https://user-images.githubusercontent.com/48288606/144731381-a22ae87c-8dc0-4716-af24-4d8a51b2c561.png)
- Use the current password for level 28 to authenticate.
- Move to **repo** folder. Read "README" file. But the file has been changes.<br><br>
![image](https://user-images.githubusercontent.com/48288606/144731457-829a7316-c1c4-4021-a03f-ca52eae7f4ad.png)
- Type `git log`. <br><br>
![image](https://user-images.githubusercontent.com/48288606/144731400-1733124d-07dd-4e49-9251-864d175afe7b.png)
- View each commit by using `git show edd935d60906b33f0619605abd1689808ccdd5ee` (Here I exam the first commit)
Note: The syntax is `git show {hash}`. <br><br>
![image](https://user-images.githubusercontent.com/48288606/144731438-570c6d47-d9ec-4435-a24b-0bb35ead1ccf.png)

#### Password for next level: 0ef186ac70e04ea33b4c1853d2526fa2 



