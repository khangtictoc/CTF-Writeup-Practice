# dont-use-client-side ❓

**Tags:** Web Exploitation

**Point:** 100 points

**Description:** 
Can you break into this super secure portal? https://jupiter.challenges.picoctf.org/problem/29835/ (link) or http://jupiter.challenges.picoctf.org:29835

### Solution: 💯

The website authenticate user from client side. Inspect the source.

The authenticating JS file check each part of user input whether it matches with some string. Combing all part we will have a valid login credential: `picoCTF{no_clients_plz_7723ce}`. That's the flag.

#### The Flag (for reference): ✔️
```
picoCTF{no_clients_plz_7723ce}
```
