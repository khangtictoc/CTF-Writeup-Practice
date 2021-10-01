# Level 8 - Level 9 ✔
- **Level Goal:**:<br>
The password for the next level is stored in the file data.txt and is the only line of text that occurs only once<br>
- **Commands you may need to solve this level:**<br>
grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd<br>
- **Helpful Reading Material:**
[Piping and Redirection](https://ryanstutorials.net/linuxtutorial/piping.php)
- **Login SSH:**<br>
User: bandit8<br>
Pass: cvX2JJa4CFALtqS87jk27qwqGhBM9plV<br>
## Write-up: 📝<br>
In this chall, we need to find the file which meets the given requirement in current Dir<br>
Use `man find` for more details
### Solution:<br>
- Sort the file, then output the unique line `sort data.txt | uniq -u`<br>
#### Password for next level: UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
