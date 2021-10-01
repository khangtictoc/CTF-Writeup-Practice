# Level 6 - Level 7 ✔
- **Level Goal:**:<br>
The password for the next level is stored somewhere on the server and has all of the following properties:
owned by user bandit7<br>
owned by group bandit6<br>
33 bytes in size<br>
human-readable<br>
1033 bytes in size<br>
not executable<br>
- **Commands you may need to solve this level:**<br>
ls, cd, cat, file, du, find<br>
- **Login SSH:**<br>
User: bandit5<br>
Pass: koReBOKuIDDepwhWk7jZC0RTdopnAYKh<br>
## Write-up: 📝<br>
In this chall, we need to find the file which meets the given requirement in **inhere** Dir<br>
Use `man find` for more details
### Solution:<br>
- Find the file
Command: `find ./inhere -readable -size 1033c \! -executable`<br>
\!: negative flag
- Cat **".hidden"** file
Command: `cat ./inhere/maybehere07/.file2`
#### Password for next level: DXjZPULLxYr17uwoI01bNLQbtFemEgo7
