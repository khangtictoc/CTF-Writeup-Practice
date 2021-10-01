# Level 9 - Level 10 ✔
- **Level Goal:**:<br>
The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters.<br>
- **Commands you may need to solve this level:**<br>
grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd<br>
- **Login SSH:**<br>
User: bandit9<br>
Pass: UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR<br>
## Write-up: 📝<br>
In this chall,  the file contains both strings and binary data which can make it difficult to read. We have to filter the human-readable characters<br>
Use `man strings` for more details
### Solution:<br>
- Command: `cat data.txt | strings | grep ^=`<br>
"^=": a regular expression (regex). Reference here: [All about regex](https://regexr.com/)
#### Password for next level: truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk

