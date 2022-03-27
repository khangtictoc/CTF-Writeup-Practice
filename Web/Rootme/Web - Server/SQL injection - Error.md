# SQL injection - Error

**Title**: Exploiting SQL error

**Point:** 40 Points

**Description:** Retrieve administrator’s password.

## Solution:

First, we have to find the SQLi point. Try `1'` in login form but it's not worked. Access **Contents**, we can see the URL `?action=contents&order=ASC` with 2 parameters `action` and `order`. The possible SQLi point is in `order`.



