# Level 14 - Level 15 ✔
- **Level Goal:**:<br>
The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost.<br>
- **Commands you may need to solve this level:**<br>
ssh, telnet, nc, openssl, s_client, nmap<br>
- **Helpful Reading Material:** <br>
[How the Internet works in 5 minutes (YouTube) ](https://www.youtube.com/watch?v=7_LPdttKXPc&ab_channel=Aaron)(Not completely accurate, but good enough for beginners)<br>
[IP Addresses](https://computer.howstuffworks.com/web-server5.htm)<br>
[IP Address on Wikipedia](https://en.wikipedia.org/wiki/IP_address)<br>
[Localhost on Wikipedia](https://en.wikipedia.org/wiki/Localhost)<br>
[Ports](https://computer.howstuffworks.com/web-server8.htm)<br>
[Port (computer networking) on Wikipedia]([https://en.wikipedia.org/wiki/Port_(computer_networking))<br>                                                        
- **Login SSH:**<br>
User: bandit13<br>
Pass: 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL<br>
## Write-up: 📝<br>
In this chall, we have to connect to port 30000 on localhost and we have to send a string containing the current password. <br>
Use `man nc` for more details
### Solution:<br>
- Connect to localhost:30000: `nc localhost 30000`
- Type the current password: `4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e`
#### Password for next level: BfMYroe26WYalil77FoDi9qh59eK5xNr 

