# SQL injection - Authentication

**Point**: 30 Points

**Description**: Retrieve the administrator password

## Solution:

We have a login form that needs to be bypassed. 

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/160244563-57aad69c-5e8d-4aa7-a016-23179a921c4f.png" > </p>

Try simple payload: 

Username: `' or 1=1 -- `

Password: `123`

Another form appears and wait us provide with information to connect

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/160244806-b413b29b-faec-4eb6-a221-b99f79b5b7f9.png" > </p>

We notice that we've bypassed the first login form. And our first value input username: `' or 1=1 -- ` and password: `123` made the query statement get all rows and there's 1 row return to the website. That's why we see an user info displayed, this is return value.

We try similar payload but with `admin` value to try to get his password as the **description** said.

Username: `admin' or 1=1 -- `

Password: `123`

Query's sent. Nothing happen, this's usually filter and they filter `or` with only username: `admin`. (We can check to verify this). Use payload without `or`:

Username: `admin' or 1=1 -- `

Password: `123`

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/160245159-465e8e36-1539-4526-b50c-115deda0aae4.png" > </p>

We can see the password by **viewing source**.

Flag: **t0_W34k!$**
