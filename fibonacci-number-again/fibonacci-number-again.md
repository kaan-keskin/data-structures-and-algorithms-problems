# Fibonacci Number Again

## Problem Introduction

In this problem, your goal is to compute πΉ(π) modulo π, where π may be really huge: up to 10^14.

For such values of π, an algorithm looping for π iterations will not fit into one second for sure. 

Therefore we need to avoid such a loop.

To get an idea how to solve this problem without going through all πΉ(π) for π from 0 to π, letβs see what happens when π is small β say, π = 2 or π = 3.

![Fibonacci Numbers Modulo Series Example](./fibonacci-mod-series.png)

Take a detailed look at this table. Do you see? Both these sequences are periodic! 

For π = 2, the period is 011 and has length 3, while for π = 3 the period is 01120221 and has length 8. 

Therefore, to compute, say, πΉ(2015) mod 3 we just need to find the remainder of 2015 when divided by 8. Since 2015 = 251 * 8 + 7, we
conclude that πΉ(2015) mod 3 = πΉ(7) mod 3 = 1.

This is true in general: for any integer π β₯ 2, the sequence πΉ(π) mod π is periodic. 

The period always starts with 01 and is known as Pisano period.

## Problem Description

**Task:** Given two integers π and π, output πΉ π mod π (that is, the remainder of πΉ π when divided by π).

**Input Format:** The input consists of two integers π and π given on the same line (separated by a space).

**Constraints:** 1 β€ π β€ 10^14, 2 β€ π β€ 10^3

**Output Format:** Output πΉ(π) mod π
