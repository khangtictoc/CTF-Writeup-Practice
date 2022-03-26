# SQL injection - Numeric

**Point:** 35 Points

**Description:** Retrieve the administrator password.

## Solution:

Use check-payload `1'` in form: **Search**  and **Login** to see whether SQLi is possible or not. But it's not available.

Back to **Home** page. We notice that if we get into any **links**. Our URL look likes this `?action=news&news_id=3`, it contains 2 parameters `action` and `news_id`, check it with `'1` and we realize the SQLi point is in `news_id`

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/160247892-2628a705-59f1-4758-aab1-45cf22cfb1a2.png"> </p>

An error 's sent back. Now try to input:
```
123' or 1=1 --
```

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/160248089-b9f681d5-e785-41e4-88b1-9ca9d33ef814.png"> </p>

There's something error with backslash symbols `\`. How odd ? We didn't input any characters like that. The title of the challenge is `Numeric`, this make me think that maybe the server has a **sanitization** in our input and replace all `"` and `'` respectively with `\"` and `\'`. So we don't even need comment out symbols `--` to escape the string.

Try to input only number and append our command like: 

```
123 order by 1 
```

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/160248539-306078db-4b82-40a0-b26c-66bd8a193123.png"> </p>

No error. Determine the number of columns return by taking advantage of `UNION`. 

```
123 union select 1 
```

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/160248574-efcc3704-92ee-404c-82c6-51d935b01c5c.png"> </p>

Add 1 more columns for each testing until it's worked. The final checking payload is: 

```
123 union select 1, 2, 3 
```

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/160248000-cca3c1d3-61eb-449e-8c87-23ecd0b8b1cc.png"> </p>


OK. That's look good ! With this, try to get the information from **system database**. In SQLite, there's a system table with 5 columns `sqlite_master(type, name, tbl_name, rootpage, sql)`. We can choose 2 columns that we're interested in. Try:

``` 
123 union select type, name, sql from sqlite_master
```

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/160248613-8cc242ed-5ed1-4109-817b-6f10a60462dd.png"> </p>

Well, a `users` table. This gotta be interesting. Get information with 3 field `username`, `password` and `year` in `user` table. Payload:

```
123 union select username, password, year from users 
```

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/160248651-eb1df667-6128-4553-bc25-e5064c1a7632.png"> </p>

No **username** appears to identify the **admin**. With a such few result, try to submit each password (The first one is correct). Or we realize that only 2nd and 3rd columns are displayed. Final payload:

```
123 union select 1, username, password from users
```

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/160249017-e1b16dbb-2dc5-45ec-ab93-fc73ead3c606.png"> </p>


Flag: **aTlkJYLjcbLmue3**



