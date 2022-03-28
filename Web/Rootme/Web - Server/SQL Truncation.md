# SQL Truncation

**Title:** SQL limits

**Point:** 35 Points

**Description: **Retrieve an access to the administration’s zone.

## Solution:

This challenge do nothing with any thing like `truncate()` function or `truncate` keyword. This's all about **Truncate Error** . [Reference Document](https://en.dirceuresende.com/blog/sql-server-string-or-binary-data-would-be-truncated-o-que-e-como-identificar-a-causa-raiz-e-como-corrigir/#:~:text=What%20is%20%E2%80%9CString%20or%20binary,than%20the%20maximum%20field%20size.)

We cannot penetrate this form, also cannot create `admin` user because this user is already in database.

Basically, **Truncate Error** happens when we declare a variable with size of (for example) `10`. And then user input more characters to that field `20`. Then user's input will be truncated to the max size declared before when handling with database (in this case is creating information). And if value in that field is not unique, we totally create a new user with the same name `admin` and our arbitrary password.

**NOTE: Message `User already in DB` is from back-end server, nothing relates to "Database Side". In database, we even create many rows which has the same value in a field (Ex: `Pseudo`), you could check this and testing on your own DB.**

Go to source code (Ctrl + U) in "Register" , you will get a surprise. 

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/160291900-98940ab9-96dd-47e7-ab77-f222f5aedd8c.png"> </p>

Now we know the length of `Pseudo` is **12**. Try to create a new user:

Pseudo : 

```
admin                        hackerisnothere
```

Password: (We can choose freely as long as having a length be greater or equal to **8**)

```
khangtictoc123
```

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/160292269-563b3fcc-f8a2-45b4-a58a-3526f67fa741.png"> </p>

Easy, pieces !


Flag: **J41m3Qu4nD54Tr0nc**
