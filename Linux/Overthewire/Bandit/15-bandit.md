# Level 15 - Level 16 ✔
- **Level Goal:**:<br>
The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL encryption.

Helpful note: Getting “HEARTBEATING” and “Read R BLOCK”? Use -ign_eof and read the “CONNECTED COMMANDS” section in the manpage. Next to ‘R’ and ‘Q’, the ‘B’ command also works in this version of that command…<br>
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

