# ELF x86 - Format string bug basic 1
- Point: 15pts
- Author: [Lu33Y](https://www.root-me.org/Lu33Y?lang=en),  8 February 2012
- Level: Easy<br><br>
![image](https://user-images.githubusercontent.com/48288606/141501790-9851fa6d-9b74-44b1-9960-74e627795010.png)
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


