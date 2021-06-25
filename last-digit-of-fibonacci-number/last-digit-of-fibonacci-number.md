# Last Digit of a Large Fibonacci Number

## Problem Introduction

Your goal in this problem is to find the last digit of 𝑛-th Fibonacci number. 

Recall that Fibonacci numbers grow exponentially fast. For example,

𝐹(200) = 280 571 172 992 510 140 037 611 932 413 038 677 189 525

Therefore, a solution like

```
𝐹[0] ← 0
𝐹[1] ← 1
for 𝑖 from 2 to 𝑛:
    𝐹[𝑖] ← 𝐹[𝑖 − 1] + 𝐹[𝑖 − 2]

print(𝐹[𝑛] mod 10)
```

will turn out to be too slow, because as 𝑖 grows the 𝑖th iteration of the loop computes the sum of longer and longer numbers. 

Also, for example, 𝐹(1000) does not fit into the standard C++ int type. 

To overcome this difficulty, you may want to store in 𝐹[𝑖] not the 𝑖th Fibonacci number itself, but just its last digit (that
is, 𝐹 𝑖 mod 10).

Computing the last digit of 𝐹 𝑖 is easy: it is just the last digit of the sum of the last digits of 𝐹(𝑖−1) and 𝐹(𝑖−2):

```
𝐹[𝑖] ← (𝐹[𝑖 − 1] + 𝐹[𝑖 − 2]) mod 10
```

This way, all 𝐹 [𝑖]’s are just digits, so they fit perfectly into any standard integer type, and computing a sum of 𝐹[𝑖 − 1] and 𝐹[𝑖 − 2] is performed very quickly.

## Problem Description

**Task:** Given an integer 𝑛, find the last digit of the 𝑛th Fibonacci number 𝐹(𝑛) (that is, 𝐹(𝑛) mod 10).

**Input Format:** The input consists of a single integer 𝑛.

**Constraints:** 0 ≤ 𝑛 ≤ 10^7

**Output Format:** Output the last digit of 𝐹(𝑛)
