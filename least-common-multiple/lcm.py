#!/usr/bin/env python3
# lcm.py

import sys


# Naive Algorithm
def lcm_naive(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a * b


# Faster GCD Algorithm
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


# Faster LCM ALgorithm
def lcm_faster(a, b):
    prod = a * b
    gcd_val = gcd_euclid(a, b)
    lcm = prod // gcd_val

    return int(lcm)


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_faster(a, b))
