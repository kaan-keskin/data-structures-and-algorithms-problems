#!/usr/bin/env python3
# fibonacci_sum_last_digit.py

import sys

# Naive Algorithm
def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


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


def fibonacci_sum_last_digit(n: int):
    period = get_pisano_period(10)
    length = len(period)
    last = 0
    if n > length:
        n = n % length
    for i in range(n + 1):
        last = (last + period[i]) % 10

    return last


# Matrix Solution
def pisano_fibonacci_sum_last_digit(n: int):
    KNOWN_VALUES = [0, 1, 2, 4, 7, 2, 0, 3, 4, 8,
                    3, 2, 6, 9, 6, 6, 3, 0, 4, 5,
                    0, 6, 7, 4, 2, 7, 0, 8, 9, 8,
                    8, 7, 6, 4, 1, 6, 8, 5, 4, 0,
                    5, 6, 2, 9, 2, 2, 5, 8, 4, 3,
                    8, 2, 1, 4, 6, 1, 8, 0, 9, 0]

    equivalent_n = n
    while equivalent_n > len(KNOWN_VALUES):
        equivalent_n = equivalent_n % len(KNOWN_VALUES)

    return KNOWN_VALUES[equivalent_n]


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_last_digit(n))
