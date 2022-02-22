# Random

**Description**: 

Daddy, teach me how to use random value in programming!

ssh random@pwnable.kr -p2222 (pw:guest)

## Source code: 

```C
#include <stdio.h>

int main(){
        unsigned int random;
        random = rand();        // random value!

        unsigned int key=0;
        scanf("%d", &key);

        if( (key ^ random) == 0xdeadbeef ){
                printf("Good!\n");
                system("/bin/cat flag");
                return 0;
        }

        printf("Wrong, maybe you should try 2^32 cases.\n");
        return 0;
}
```

### Solution:

The **rand()** function with no seed is always returning the same values. We can copy the code and run similarly to examine the value of random. 

By default, the code above is seed with "1", like calling this function **srand(1)**. Reference: [Rand() function in C)](https://en.cppreference.com/w/cpp/numeric/random/rand)

The random value we figure out is **1804289383**. Then **XOR** with **0xdeadbeef** to find the result. 

![image](https://user-images.githubusercontent.com/48288606/155062819-c532e413-4e68-4165-ac8c-e5ab883c4614.png)

Flag: **Mommy, I thought libc random is unpredictable...**

