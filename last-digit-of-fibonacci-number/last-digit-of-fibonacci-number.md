# Last Digit of a Large Fibonacci Number

## Problem Introduction

Your goal in this problem is to find the last digit of π-th Fibonacci number. 

Recall that Fibonacci numbers grow exponentially fast. For example,

πΉ(200) = 280 571 172 992 510 140 037 611 932 413 038 677 189 525

Therefore, a solution like

```
πΉ[0] β 0
πΉ[1] β 1
for π from 2 to π:
    πΉ[π] β πΉ[π β 1] + πΉ[π β 2]

print(πΉ[π] mod 10)
```

will turn out to be too slow, because as π grows the πth iteration of the loop computes the sum of longer and longer numbers. 

Also, for example, πΉ(1000) does not fit into the standard C++ int type. 

To overcome this difficulty, you may want to store in πΉ[π] not the πth Fibonacci number itself, but just its last digit (that
is, πΉ π mod 10).

Computing the last digit of πΉ π is easy: it is just the last digit of the sum of the last digits of πΉ(πβ1) and πΉ(πβ2):

```
πΉ[π] β (πΉ[π β 1] + πΉ[π β 2]) mod 10
```

This way, all πΉ [π]βs are just digits, so they fit perfectly into any standard integer type, and computing a sum of πΉ[π β 1] and πΉ[π β 2] is performed very quickly.

## Problem Description

**Task:** Given an integer π, find the last digit of the πth Fibonacci number πΉ(π) (that is, πΉ(π) mod 10).

**Input Format:** The input consists of a single integer π.

**Constraints:** 0 β€ π β€ 10^7

**Output Format:** Output the last digit of πΉ(π)
