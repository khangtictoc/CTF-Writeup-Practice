# Level 16 - Level 17 ✔
- **Level Goal:**:<br>
The credentials for the next level can be retrieved by submitting the password of the current level to a port on localhost in the range 31000 to 32000. First find out which of these ports have a server listening on them. Then find out which of those speak SSL and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.<br>
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

