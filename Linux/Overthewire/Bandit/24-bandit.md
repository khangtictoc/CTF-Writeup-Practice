# Level 24 - Level 25 ✔
- **Level Goal:**:<br>
A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing.<br>                                            
- **Login SSH:**<br>
User: bandit24<br>
Pass: UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ<br>
## Write-up: 📝<br>
In this chall, we learn how to bruteforce. You can reference here: [BruteForce from OWASP](https://owasp.org/www-community/attacks/Brute_force_attack) <br>
### Solution:<br>
- We have no command suggested here. It means we have to write a **bash script** again. With the description above, i just need to pass a string which combines of current 
password and a **PIN** code (which have to bruteforce). So here is my script:
`#! /bin/bash`
`for i in {0000..9999}`
`do`
`    echo "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $i"`
`done | nc localhost 30002`
**Note**: Remember to put the `| nc localhost 30002` command after looping. Let the loop output **pipeline** through into netcat.  
#### Password for next level: uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG 


