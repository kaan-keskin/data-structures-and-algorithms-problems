# Fibonacci Number

## Problem Introduction

Recall the definition of Fibonacci sequence: ๐น(0) = 0, ๐น(1) = 1, and ๐น(๐) = ๐น(๐โ1) + ๐น(๐โ2) for ๐ โฅ 2.

Your goal in this problem is to implement an efficient algorithm for computing Fibonacci numbers. 

The starter files for this problem contain an implementation of the following naive recursive algorithm for computing Fibonacci numbers in Python3:

```Python
Fibonacci(n):
    if n โค 1:
        return n
    return Fibonacci(n โ 1) + Fibonacci(n โ 2)
```

Try compiling and running a starter solution on your machine. 
You will see that computing, say, ๐น 40 already takes noticeable time.

Another way to appreciate the dramatic difference between an exponential time algorithm and a polynomial time algorithm is to use the following visualization by David Galles: http://www.cs.usfca.edu/~galles/visualization/DPFib.html.

Try computing ๐น(20) by a recursive algorithm by entering โ20โ and pressing the โFibonacci Recursiveโ button.

You will see an endless number of recursive calls.

Now, press โSkip Forwardโ to stop the current algorithm and call the iterative algorithm by pressing โFibonacci Tableโ.

This will compute ๐น(20) very quickly.

(Note that the visualization uses a slightly different definition of Fibonacci numbers: ๐น(0) = 1 instead of ๐น(0) = 0.

This of course has almost no influence on the running time.)

## Problem Description

**Task:** Given an integer ๐, find the ๐th Fibonacci number ๐น(๐)

**Input Format:** The input consists of a single integer ๐

**Constraints:** 0 โค ๐ โค 45

**Output Format:** Output ๐น(๐)
