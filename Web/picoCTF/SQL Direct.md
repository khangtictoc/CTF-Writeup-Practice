# SQL Direct ❓

**Tags:** Web Exploitation

**Point:** 200 points

**Description:** 
Connect to this PostgreSQL server and find the flag!<br>
psql -h saturn.picoctf.net -p 58674 -U postgres pico <br>
Password is postgres

### Solution: 💯

Install postgresql in https://www.postgresql.org/. Then connect to `psql -h saturn.picoctf.net -p 58674 -U postgres pico`. 

Use `\l` to list all databases

<p align="center"> <img width=600px height=200px src="https://user-images.githubusercontent.com/48288606/159285211-1a6efdbc-be6f-4d90-af44-d145390ea028.png"></p>

Use `\c pico` to connect to **pico** database. Then use `\dt` to list all available tables.

<p align="center"> <img width=300px height=100px  src="https://user-images.githubusercontent.com/48288606/159285686-a4319f35-9f8a-4bcb-91da-4911c538887d.png"> </p>

Print all data in **flag** table by `select * from flags;`

<p align="center"> <img width=700px height=200px  src="https://user-images.githubusercontent.com/48288606/159286010-1d4dd7b1-bdea-488f-8bad-4866d5b768b0.png"> </p>

#### The Flag (for reference): ✔️
```
picoCTF{L3arN_S0m3_5qL_t0d4Y_0414477f}
```
