# ELF x86 - Format string bug basic 1
- Point: 15pts
- Author: [Lu33Y](https://www.root-me.org/Lu33Y?lang=en),  8 February 2012
- Level: Easy<br><br>
![image](https://user-images.githubusercontent.com/48288606/141501790-9851fa6d-9b74-44b1-9960-74e627795010.png)
## Write-up:

```
#include <stdio.h>
#include <unistd.h>
 
int main(int argc, char *argv[]){
        FILE *secret = fopen("/challenge/app-systeme/ch5/.passwd", "rt");
        char buffer[32];
        fgets(buffer, sizeof(buffer), secret);
        printf(argv[1]);
        fclose(secret);
        return 0;
}
```

### Solution:

Pass: 1w4ntm0r3pr0np1s


