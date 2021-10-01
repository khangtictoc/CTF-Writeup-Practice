# Level 12 - Level 13 ✔
- **Level Goal:**:<br>
The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work using mkdir. For example: mkdir /tmp/myname123. Then copy the datafile using cp, and rename it using mv (read the manpages!)<br>
- **Commands you may need to solve this level:**<br>
grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd, mkdir, cp, mv, file<br>
- **Helpful Reading Material:** <br>
[Hex dump on Wikipedia](https://en.wikipedia.org/wiki/Hex_dump)
- **Login SSH:**<br>
User: bandit12<br>
Pass: 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu<br>
## Write-up: 📝<br>
In this chall, we have to decompress the file multiple times with various compress format.<br>
Use `man mkdir`, `man mv`, `man xxd`, `man gzip`, `man bzip2` and `man tar` for more details
### Solution:<br>
First, we have to create a directory under /tmp path as suggested for easily working with file `mkdir /tmp/darkhero101`  -- Change "darkhero101" into your filename<br>
And copy **data.txt** into there: `cp data.txt /tmp/darkhero101`<br>
Then, get into that path by `cd /tmp/darkhero101`.<br>
Now, we have to decompress the data, there are 3 main steps:<br>
- Step 1: Use `file {filename}` to figure out which types of that file **--gzip compressed data/bzip2 compressed data/ POSIX tar archive (GNU)--**.<br>
- Step 2: Rename the file to change the end **extension** suit to type in step above (The first time does not need): `mv {filename}.{extension}` (extension: gz, bzip2, tar)<br>
- Step 3: Use decompress command suitably with that types. Using:<br>
In the beginning, we are hinted that we will reverse hexdump the file: `xxd -r data.txt > {output}`
">": send the output data to file named {output}<br>
-r: reverse hexdump <br>
Other case:
`bzip2 -d {filename} > {outfile}` (Decompress **bzip2** file)<br> 
`gzip -d {filename} > {outfile}`(Decompress **gzip** file)<br>
`tar -xf {filename} > {outfile}`(Decompress **tar** file)<br>
-x: extract file<br>
-f: use the file ARCHIVE<br>
- Step 4: When we get a new file, start over with step 1. Stop until get the password. <br>
Note: After multiple-times decompression, we will get an ASCII text file. Then just read that file by `cat`

#### Password for next level: 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL

