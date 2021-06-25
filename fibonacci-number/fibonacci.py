#!/usr/bin/env python3
# fibonacci.py

# Naive Algorithm
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


# Faster Algorithm
def calc_fib_2(n):
    fib_list = [0, 1]
    if n > 1:
        for i in range(2, n + 1):
            fib_list.insert(i, fib_list[i - 1] + fib_list[i - 2])

    return fib_list[n]


# Faster Algorithm
def calc_fib_3(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current


if __name__ == '__main__':
    n = int(input())
    print(calc_fib_2(n))
