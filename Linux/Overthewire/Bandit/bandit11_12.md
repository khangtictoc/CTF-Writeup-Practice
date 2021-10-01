# Level 11 - Level 12 ✔
- **Level Goal:**:<br>
The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions<br>
- **Commands you may need to solve this level:**<br>
grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd<br>
- **Helpful Reading Material:** <br>
[Rot13 on Wikipedia](https://en.wikipedia.org/wiki/ROT13)
- **Login SSH:**<br>
User: bandit11<br>
Pass: IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR<br>
## Write-up: 📝<br>
In this chall, the data has been encoded with ROT13. We need to decode it<br>
Use `man tr` for more details
### Solution:<br>
- Use online tool: [ROT13](https://rot13.com/)<br>
### Other solution:<br>
- Need to know regex.<br>
Command: `cat data.txt | tr '[A-Za-z]' '[N-ZA-Mn-za-m]'` <br>
Explain: Rotate 13 position means (a->n, z->m and the same goes with uppercase)
#### Password for next level: 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
