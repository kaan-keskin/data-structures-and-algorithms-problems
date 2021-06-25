#!/usr/bin/env python3
# fibonacci_huge.py

import sys


# Naive Algorithm
def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


# Faster Algorithm - Pisano Period
def get_pisano_period_length(m):
    prev, curr = 0, 1
    for i in range(2, m * m + 1):
        prev, curr = curr, (prev + curr) % m
        # A Pisano Period starts with 01
        if prev == 0 and curr == 1:
            return i - 1
    return 0


def get_pisano_period(m):
    length = get_pisano_period_length(m)
    period = [0] * length
    period[0] = 0
    period[1] = 1
    for i in range(2, length):
        period[i] = (period[i - 1] + period[i - 2]) % m

    return period


# Calculate Fn mod m
def fibonacci_modulo(n, m):
    # Getting the period
    pisano_period_len = get_pisano_period_length(m)
    pisano_period = get_pisano_period(m)
    if n > pisano_period_len:
        # Taking mod of N with period length
        n = n % pisano_period_len

    return pisano_period[n]


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(fibonacci_modulo(n, m))
