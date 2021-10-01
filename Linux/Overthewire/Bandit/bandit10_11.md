# Level 10 - Level 11 ✔
- **Level Goal:**:<br>
The password for the next level is stored in the file data.txt, which contains base64 encoded data<br>
- **Commands you may need to solve this level:**<br>
grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd<br>
- **Helpful Reading Material:** <br>
[Base64 on Wikipedia](https://en.wikipedia.org/wiki/Base64)
- **Login SSH:**<br>
User: bandit10<br>
Pass: truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk<br>
## Write-up: 📝<br>
In this chall, the data has been encoded with base64. We have to decode it<br>
Use `man decode` for more details
### Solution:<br>
- Command: `cat data.txt | base64 -d`<br>
#### Password for next level: IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
