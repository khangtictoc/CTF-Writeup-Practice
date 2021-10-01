# Level 9 - Level 10 ✔
- **Level Goal:**:<br>
The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters.<br>
- **Commands you may need to solve this level:**<br>
grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd<br>
- **Login SSH:**<br>
User: bandit9<br>
Pass: UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR<br>
## Write-up: 📝<br>
In this chall, we need to find the file which meets the given requirement in current Dir<br>
Use `man sort` and `man uniq` for more details
### Solution:<br>
- Sort the file, then output the unique line: `sort data.txt | uniq -u`<br>
#### Password for next level: UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR

