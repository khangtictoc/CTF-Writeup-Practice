
## ====================== SOLVED !!! ======================

import time

## ====================== DEFINED FUNCTION (FROM REVERSING SOURCE)======================

def check(input, s):
    return chec(input, s)

def check1(input, s):
    t = input
    t += 4950
    return chec(t, s)

def check2(input, s):
    t = input
    if s % 2 == 0:
        t += 499500
        return chec(t, s)
    t -= 499500
    return chec(t, s)

def check3(input, s):
    t = input
    t += 49995000
    return chec(t, s)

def chec(input, s):
    if s - 1 <= 0:
        result = input
    else:
        if 2 * s % 3 == 0:
            result = check1(input, s - 1)
        if 2 * s % 3 == 1:
            result = check2(input, s - 1)
        if 2 * s % 3 == 2:
            result = check3(input, s - 1) 
    return result

## ====================== MAIN FUNCTION (CRACKING PASSWORD) ======================

in_int = 236492000
start_time = time.time()

while (1):
    if check(in_int, 99) == 1835996258:
        print("The correct value is: " + str(in_int))
        stop_time = time.time()
        print("Execution time: " + str(stop_time - start_time))
        break
    else:
        print("Try: " + str(in_int))
        in_int += 1

## Correct number is 236492408
## ====================== CHECK FUNCTION ======================

print(check(236492408, 99) == 1835996258)


## Temp 

def check1(input, s):
    t = input
    t += 4950
    return chec(t, s)

def check2(input, s):
    t = input
    if s % 2 == 0:
        t += 499500
        return chec(t, s)
    t -= 499500
    return chec(t, s)

def check3(input, s):
    t = input
    t += 49995000
    return chec(t, s)