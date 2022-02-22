# Mistake

**Description:

We all make mistakes, let's move on.
(don't take this too seriously, no fancy hacking skill is required at all)

This task is based on real event
Thanks to dhmonkey

hint : operator priority

ssh mistake@pwnable.kr -p2222 (pw:guest)

## Source code:

```C
#include <stdio.h>
#include <fcntl.h>

#define PW_LEN 10
#define XORKEY 1

void xor(char* s, int len){
        int i;
        for(i=0; i<len; i++){
                s[i] ^= XORKEY;
        }
}

int main(int argc, char* argv[]){

        int fd;
        if(fd=open("/home/mistake/password",O_RDONLY,0400) < 0){
                printf("can't open password %d\n", fd);
                return 0;
        }

        printf("do not bruteforce...\n");
        sleep(time(0)%20);

        char pw_buf[PW_LEN+1];
        int len;
        if(!(len=read(fd,pw_buf,PW_LEN) > 0)){
                printf("read error\n");
                close(fd);
                return 0;
        }

        char pw_buf2[PW_LEN+1];
        printf("input password : ");
        scanf("%10s", pw_buf2);

        // xor your input
        xor(pw_buf2, 10);

        if(!strncmp(pw_buf, pw_buf2, PW_LEN)){
                printf("Password OK\n");
                system("/bin/cat flag\n");
        }
        else{
                printf("Wrong Password\n");
        }

        close(fd);
        return 0;
}
```

### Solution:

As the hint proposed, there is a unintentional vulnerability in this line: `if(fd=open("/home/mistake/password",O_RDONLY,0400) < 0)`

Some compiler will alert errors, some would parse the code above into this : `if(fd = (open("/home/mistake/password",O_RDONLY,0400) < 0))`. The comparison with '0' will happen before assignment. Reference here: [Priority operator](https://en.cppreference.com/w/c/language/operator_precedence)

And the password has the "Read" permission so it will return a non-negative integer; therefore, the **result > 0** and **fd = 0**. So in this line, `len=read(fd,pw_buf,PW_LEN)`, we could construct our password from input (STDIN(0))

This first password `pw_buf`, which we can input whatever we want, would be compared with the second password `pw_buf2`. `pw_buf2` is take the value from `pw_buf` and **XOR** with '1'. 

This python code could solve the problem: `chr(int('0b' + str(int(format(ord('{character_you_want_to_xor}'), 'b')) ^ 1), 2))`

For example: 
```python
>>> chr(int('0b' + str(int(format(ord('A'), 'b')) ^ 1), 2))
'@'
```
If the characters in password is "A", the second must be "@". Make sure our input have both 10 characters in length. 

Flag: **Mommy, the operator priority always confuses me :(**



