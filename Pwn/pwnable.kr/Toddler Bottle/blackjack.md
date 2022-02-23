# Blackjack

**Description:**

Hey! check out this C implementation of blackjack game!
I found it online
* http://cboard.cprogramming.com/c-programming/114023-simple-blackjack-program.html

I like to give my flags to millionares.
how much money you got?


Running at : nc pwnable.kr 9009

## Source code:

Source game: https://cboard.cprogramming.com/c-programming/114023-simple-blackjack-program.html

### Solution:
 
 We notice that the types of our **cash** and **bet** is int. So we can input the negative number so when `cash = cash - bet;` implemented, our cash would increase, input the bet with "-2000000000", try to get lose and our cash will increase. Ding dong ! We're billiionaires
 
 Flag: **YaY_I_AM_A_MILLIONARE_LOL**
 
