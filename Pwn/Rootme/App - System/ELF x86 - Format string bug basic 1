# ELF x86 - Format string bug basic 1
- Point: 15pts
- Author: [Lu33Y](https://www.root-me.org/Lu33Y?lang=en),  8 February 2012
- Level: Very Easy
- Statement
- Environment configuration <br>
```
  PIE	    Position Independent Executable	 ✘ 
  RelRO	    Read Only relocations	         ✘ 
  NX	    Non-Executable Stack	         ✘ 
  Heap exec Non-Executable Heap	                 ✘ 
  ASLR	    Address Space Layout Randomization	 ✘ 
  SF	    Source Fortification	         ✘ 
  SRC	    Source code access	                 ✔ 
```
## Write-up:

```
#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>
#include <stdio.h>
 
int main()
{
 
  int var;
  int check = 0x04030201;
  char buf[40];
 
  fgets(buf,45,stdin);
 
  printf("\n[buf]: %s\n", buf);
  printf("[check] %p\n", check);
 
  if ((check != 0x04030201) && (check != 0xdeadbeef))
    printf ("\nYou are on the right way!\n");
 
  if (check == 0xdeadbeef)
   {
     printf("Yeah dude! You win!\nOpening your shell...\n");
     setreuid(geteuid(), geteuid());
     system("/bin/bash");
     printf("Shell closed! Bye.\n");
   }
   return 0;
}
```

### Solution:

 Pass: 1w4ntm0r3pr0np1s


