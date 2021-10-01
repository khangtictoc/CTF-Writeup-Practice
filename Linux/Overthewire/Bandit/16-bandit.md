# Level 16 - Level 17 ✔
- **Level Goal:**:<br>
There are 2 files in the homedirectory: passwords.old and passwords.new. The password for the next level is in passwords.new and is the only line that has been changed between passwords.old and passwords.new<br>
NOTE: if you have solved this level and see ‘Byebye!’ when trying to log into bandit18, this is related to the next level, bandit19<br>
- **Commands you may need to solve this level:**<br>
ssh, telnet, nc, openssl, s_client, nmap<br>
- **Helpful Reading Material:** <br>
[Secure Socket Layer/Transport Layer Security on Wikipedia](https://en.wikipedia.org/wiki/Secure_Socket_Layer)<br>
[OpenSSL Cookbook - Testing with OpenSSL](https://www.feistyduck.com/library/openssl-cookbook/online/ch-testing-with-openssl.html)<br>                                             
- **Login SSH:**<br>
User: bandit15<br>
Pass: BfMYroe26WYalil77FoDi9qh59eK5xNr<br>
## Write-up: 📝<br>
In this chall, we have to connect to port 30000 on localhost and we have to send a string containing the current password. <br>
Use `man nc` for more details
### Solution:<br>
- Connect securely (SSL encryption) to localhost:30001: `openssl s_client -connect localhost:30001`
#### Password for next level: cluFn7wTiGryunymYOu4RcffSxQluehd 

