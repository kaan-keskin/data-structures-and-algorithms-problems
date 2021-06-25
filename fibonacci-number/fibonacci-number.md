# Fibonacci Number

## Problem Introduction

Recall the definition of Fibonacci sequence: 𝐹(0) = 0, 𝐹(1) = 1, and 𝐹(𝑖) = 𝐹(𝑖−1) + 𝐹(𝑖−2) for 𝑖 ≥ 2.

Your goal in this problem is to implement an efficient algorithm for computing Fibonacci numbers. 

The starter files for this problem contain an implementation of the following naive recursive algorithm for computing Fibonacci numbers in Python3:

```Python
Fibonacci(n):
    if n ≤ 1:
        return n
    return Fibonacci(n − 1) + Fibonacci(n − 2)
```

Try compiling and running a starter solution on your machine. 
You will see that computing, say, 𝐹 40 already takes noticeable time.

Another way to appreciate the dramatic difference between an exponential time algorithm and a polynomial time algorithm is to use the following visualization by David Galles: http://www.cs.usfca.edu/~galles/visualization/DPFib.html.

Try computing 𝐹(20) by a recursive algorithm by entering “20” and pressing the “Fibonacci Recursive” button.

You will see an endless number of recursive calls.

Now, press “Skip Forward” to stop the current algorithm and call the iterative algorithm by pressing “Fibonacci Table”.

This will compute 𝐹(20) very quickly.

(Note that the visualization uses a slightly different definition of Fibonacci numbers: 𝐹(0) = 1 instead of 𝐹(0) = 0.

This of course has almost no influence on the running time.)

## Problem Description

**Task:** Given an integer 𝑛, find the 𝑛th Fibonacci number 𝐹(𝑛)

**Input Format:** The input consists of a single integer 𝑛

**Constraints:** 0 ≤ 𝑛 ≤ 45

**Output Format:** Output 𝐹(𝑛)
