# Level 7 - Level 8 ✔
- **Level Goal:**:<br>
The password for the next level is stored in the file data.txt next to the word millionth<br>
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
"(command A)| (command B)" : pipeline operator - send the output of command A to command B 
#### Password for next level: cvX2JJa4CFALtqS87jk27qwqGhBM9plV
