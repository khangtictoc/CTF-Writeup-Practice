# ELF x86 - Stack buffer overflow basic 2
- Point: 10pts
- Author: [Lyes](https://www.root-me.org/Lyes?lang=en), 10 April 2015
- Level: Very Easy
- Statement
- Environment configuration <br>
```
  PIE	    Position Independent Executable	 ✘ 
  RelRO	    Read Only relocations	         ✘ 
  NX	    Non-Executable Stack	         ✔ 
  Heap exec Non-Executable Heap	                 ✔ 
  ASLR	    Address Space Layout Randomization	 ✘ 
  SF	    Source Fortification	         ✘ 
  SSP	    Stack-Smashing Protection            ✘
  SRC	    Source code access	                 ✔ 
```
## Write-up:
