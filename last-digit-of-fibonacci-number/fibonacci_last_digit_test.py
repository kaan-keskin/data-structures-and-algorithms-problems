#!/usr/bin/env python3
# fibonacci_last_digit_unit_tests.py

import random
import time
import unittest
import fibonacci_last_digit

TIME_LIMIT_SECONDS = 5
implemented_functions = [fibonacci_last_digit.get_fibonacci_last_digit_naive,
                         fibonacci_last_digit.get_fibonacci_last_digit_2]


class FibonacciLastDigitTest(unittest.TestCase):
    def test_trivial_case(self):
        for func in implemented_functions:
            self.assertEqual(0, func(0))
            self.assertEqual(1, func(1))
            self.assertEqual(1, func(2))
            self.assertEqual(2, func(3))
            self.assertEqual(5, func(5))
            self.assertEqual(5, func(10))

    def test_stress(self):
        for n in range(30):
            for func in implemented_functions:
                start_time = time.time()
                fib_num = func(n)
                elapsed_time = time.time() - start_time
                print("---")
                print(f'Function: {func}({n})')
                print(f'Elapsed seconds: {elapsed_time} for input:{n}')
                self.assertTrue(elapsed_time < TIME_LIMIT_SECONDS)
                print("---")


if __name__ == '__main__':
    unittest.main()
