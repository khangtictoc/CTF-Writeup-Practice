# Level 6 - Level 7 ✔
- **Level Goal:**:<br>
The password for the next level is stored somewhere on the server and has all of the following properties:
owned by user bandit7<br>
owned by group bandit6<br>
33 bytes in size<br>
- **Commands you may need to solve this level:**<br>
ls, cd, cat, file, du, find<br>
- **Login SSH:**<br>
User: bandit6<br>
Pass: DXjZPULLxYr17uwoI01bNLQbtFemEgo7<br>
## Write-up: 📝<br>
In this chall, we need to find the file which meets the given requirement in entire systems <br>
Use `man find` for more details
### Solution:<br>
- Find the file: `find /  -group bandit6 -user bandit7 -size 33c`<br>
File with no permission is the right one. We can add `2> /dev/null` at the end of the command to fill out the error(permission denied files), it won't be output to the console<br>
"/": all the files in the system
- Read the file: `cat /var/lib/dpkg/info/bandit7.password`<br>
#### Password for next level: HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
