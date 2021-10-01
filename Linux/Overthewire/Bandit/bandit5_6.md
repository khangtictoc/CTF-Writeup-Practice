# Level 5 - Level 6 ✔
- **Level Goal:**:<br>
The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:<br>
human-readable<br>
1033 bytes in size<br>
not executable<br>
- **Commands you may need to solve this level:**<br>
ls, cd, cat, file, du, find<br>
ssh<br>
- **Login SSH:**<br>
User: bandit5<br>
Pass: koReBOKuIDDepwhWk7jZC0RTdopnAYKh<br>
## Write-up: 📝<br>
In this chall, we need to find the file which meets the given requirement in **inhere** Dir<br>
Use `man find` for more details
### Solution:<br>
- Find the file
Command: `find ./inhere -readable -size 1033c \! -executable`<br>
- Cat **".hidden"** file
Command: `cat ./inhere/maybehere07/.file2`
#### Password for next level: DXjZPULLxYr17uwoI01bNLQbtFemEgo7
