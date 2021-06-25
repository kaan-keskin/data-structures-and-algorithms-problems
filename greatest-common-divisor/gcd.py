#!/usr/bin/env python3
# gcd.py

import sys


# Naive Algorithm
def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


# Faster Algorithm
def gcd_euclid(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a > b:
        a_modified = a % b
        return gcd_euclid(a_modified, b)
    else:
        b_modified = b % a
        return gcd_euclid(a, b_modified)


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_euclid(a, b))
