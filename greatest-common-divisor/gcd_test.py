#!/usr/bin/env python3
# gcd_unit_tests.py


import sys
import random
import time
import unittest
import gcd

TIME_LIMIT_SECONDS = 5
implemented_functions = [gcd.gcd_naive,
                         gcd.gcd_euclid]


class GCDTest(unittest.TestCase):
    def test_trivial_case(self):
        for func in implemented_functions:
            self.assertEqual(func(18, 35), 1)
            self.assertEqual(func(1344, 217), 7)
            self.assertEqual(func(28851538, 1183019), 17657)

    def test_max_inputs(self):
        for func in implemented_functions:
            max_input = int(2e9)
            start_time = time.time()
            func(1, max_input)
            elapsed_time = time.time() - start_time
            print("---")
            print(f'Function: {func}({1,max_input})')
            print(f'Elapsed seconds: {elapsed_time} for input:{1,max_input}')
            self.assertTrue(elapsed_time < TIME_LIMIT_SECONDS)
            print("---")

    def test_stress(self):
        for _ in range(30):
            for func in implemented_functions:
                a = random.randint(1, 2e6)
                b = random.randint(1, 2e6)
                start_time = time.time()
                func(a,b)
                elapsed_time = time.time() - start_time
                print("---")
                print(f'Function: {func}({a,b})')
                print(f'Elapsed seconds: {elapsed_time} for input:{a,b}')
                self.assertTrue(elapsed_time < TIME_LIMIT_SECONDS)
                print("---")


if __name__ == "__main__":
    unittest.main()
