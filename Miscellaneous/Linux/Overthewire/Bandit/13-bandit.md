# Level 13 - Level 14 ✔
- **Level Goal:**:<br>
The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. Note: localhost is a hostname that refers to the machine you are working on<br>
- **Commands you may need to solve this level:**<br>
ssh, telnet, nc, openssl, s_client, nmap<br>
- **Helpful Reading Material:** <br>
[SSH/OpenSSH/Keys](https://help.ubuntu.com/community/SSH/OpenSSH/Keys)
- **Login SSH:**<br>
User: bandit13<br>
Pass: 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL<br>
## Write-up: 📝<br>
In this chall, we need to "ssh" to their server by using **private ssh key** (Not using password like normal)<br>
Use `man ssh` for more details
### Solution:<br>
- Get private ssh key from file: `cat sshkey.private` <br>
- Copy the all the output data and save it in a file and name it, for example sshkey.txt<br>
- Then "ssh" by next level user : `ssh -i bandit14_PrivateSSHKey.txt  bandit.labs.overthewire.org -l bandit14 -p 2220`
- Read the password for user bandit 14: `/etc/bandit_pass/bandit14`. So we don't need to ssh again by using private ssh key.
#### Password for next level: 4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e (After get into Level 14 - Level 15 and read the password)

