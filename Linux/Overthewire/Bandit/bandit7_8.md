# Level 7 - Level 8 ✔
- **Level Goal:**:<br>
The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:<br>
human-readable<br>
1033 bytes in size<br>
not executable<br>
- **Commands you may need to solve this level:**<br>
grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd<br>
- **Login SSH:**<br>
User: bandit7<br>
Pass: HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs<br>
## Write-up: 📝<br>
In this chall, we need to manipulate the data in data.txt file<br>
Use `man grep` for more details
### Solution:<br>
Command: `cat data.txt | grep millionth`<br>
#### Password for next level: cvX2JJa4CFALtqS87jk27qwqGhBM9plV
