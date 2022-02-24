# Cmd1

**Description:**

Mommy! what is PATH environment in Linux?

ssh cmd1@pwnable.kr -p2222 (pw:guest)

## Source code:

```C
#include <stdio.h>
#include <string.h>

int filter(char* cmd){
        int r=0;
        r += strstr(cmd, "flag")!=0;
        r += strstr(cmd, "sh")!=0;
        r += strstr(cmd, "tmp")!=0;
        return r;
}
int main(int argc, char* argv[], char** envp){
        putenv("PATH=/thankyouverymuch");
        if(filter(argv[1])) return 0;
        system( argv[1] );
        return 0;
}
```

### Solution:

The program set the **$PATH** var into meaningless path "/thankyouverymuch". To execute command, we have to set **$PATH** to **/bin** (most common command here) and then execute the command we want. 

Notice that we must bypass the filter of our input ("flag", "sh", "tmp"). It's very easy to get through. In my case, I use "cat \*" to read all files in the current location.

Command: `./cmd1 "export PATH=/bin; cat *" `

Flag: **mommy now I get what PATH environment is for :)**
