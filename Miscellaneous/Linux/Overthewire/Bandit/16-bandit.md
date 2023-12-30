# Level 16 - Level 17 ✔
- **Level Goal:**:<br>
The credentials for the next level can be retrieved by submitting the password of the current level to a port on localhost in the range 31000 to 32000. First find out which of these ports have a server listening on them. Then find out which of those speak SSL and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.<br>
- **Commands you may need to solve this level:**<br>
ssh, telnet, nc, openssl, s_client, nmap<br>
- **Helpful Reading Material:** <br>
[Port scanner on Wikipedia](https://en.wikipedia.org/wiki/Port_scanner)<br>                                     
- **Login SSH:**<br>
User: bandit16<br>
Pass: cluFn7wTiGryunymYOu4RcffSxQluehd<br>
## Write-up: 📝<br>
In this chall, we have to connect to  find out which of these ports have a server listening on them. Then find out which of those speak SSL <br>
Use `man nmap` for more details
### Solution:<br>
- Scan ports in given range: `nmap localhost -p 31000-32000`<br>
- Find right port with this command: `openssl s_client -connect localhost:{port}` with each scanned port.
- Only port: 31790 give back the private ssh key
#### Password for next level: xLYVMN9WE5zQ5vHacb0sZEVqbrp7nBTn (After login in Level 17 - Level 18 and read the password)

