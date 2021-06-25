#!/usr/bin/env python3
# fibonacci_test.py

import random
import time
import unittest
import fibonacci

TIME_LIMIT_SECONDS = 5
implemented_functions = [fibonacci.calc_fib,
                         fibonacci.calc_fib_2,
                         fibonacci.calc_fib_3]


class FibonacciTest(unittest.TestCase):
    def test_trivial_case(self):
        for func in implemented_functions:
            self.assertEqual(0, func(0))
            self.assertEqual(1, func(1))
            self.assertEqual(1, func(2))
            self.assertEqual(2, func(3))
            self.assertEqual(5, func(5))
            self.assertEqual(55, func(10))

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
