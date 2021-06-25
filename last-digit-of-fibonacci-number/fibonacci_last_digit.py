#!/usr/bin/env python3
# fibonacci_last_digit.py

import sys


# Naive Algorithm
def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n
    previous = 0
    current = 1
    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


# Faster Algorithm
def get_fibonacci_last_digit_2(n):
    if n <= 1:
        return n
    previous = 0
    current = 1
    for _ in range(n - 1):
        previous, current = (current % 10), (previous % 10 + current % 10)

    return current % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_2(n))
