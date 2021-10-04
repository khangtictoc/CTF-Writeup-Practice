# Level 20 - Level 21 ✔
- **Level Goal:**:<br>
There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument.
It then reads a line of text from the connection and compares it to the password in the previous level (bandit20).
If the password is correct, it will transmit the password for the next level (bandit21).<br>
NOTE: Try connecting to your own network daemon to see if it works as you think<br>
- **Commands you may need to solve this level:**<br>
ssh, nc, cat, bash, screen, tmux, Unix ‘job control’ (bg, fg, jobs, &, CTRL-Z, …)<br>                                        
- **Login SSH:**<br>
User: bandit20<br>
Pass: GbKksEFF4yrVs6il55v6gwY5aVje5f0j<br>
## Write-up: 📝<br>
In this chall, we have a different **Setuid binary** file with different function.<br>
- Execute **Setuid** file: `./suconnect`
- ![image](https://user-images.githubusercontent.com/48288606/135811838-7a0902bd-cb58-4c7d-a71b-65ca4cbe6c9b.png)
As we can see, that files act exactly like what the challenge describes above.<br>
So in this challenge, we have to create 2 sessions: A listening terminal used to open the port and put the current password in there; and a terminal that we'll use this **suconnect** file to connect to that port to check the password<br>
### Solution:<br>
- First, we create two terminal. We can use the short cut `Ctrl + Alt + T`. Then, connect both to challenge by **ssh** like normal.<br> 
- Second, we gonna let a arbitary terminal assume listening task and send the **{current password}** into local host and optional **{port}** (here i choose "4444"): `echo "GbKksEFF4yrVs6il55v6gwY5aVje5f0j" |nc -l localhost -p 4444`<br>
- Finally, the other port responsible for connecting task by using: `./suconnect 4444` <br>
The password for next chall display in listening terminal
#### Password for next level: gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr 

