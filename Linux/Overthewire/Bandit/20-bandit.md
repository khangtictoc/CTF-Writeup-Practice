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
In this chall, we ought to differentiate the content between 2 files<br>
Use `man diff` for more details
### Solution:<br>
- Compare 2 files: `diff password.new passwords.old`<br>
#### Password for next level: kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd 

