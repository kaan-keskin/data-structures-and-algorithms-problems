#!/usr/bin/env python3
# lcm_test.py


import sys
import random
import time
import unittest
import lcm

TIME_LIMIT_SECONDS = 5
implemented_functions = [lcm.lcm_naive,
                         lcm.lcm_faster]


class LCMTest(unittest.TestCase):

    def test_trivial_case(self):
        for func in implemented_functions:
            self.assertEqual(func(6, 8), 24)
            self.assertEqual(func(28851538, 1183019), 1933053046)
            self.assertEqual(func(761457, 614573), 467970912861)

    def test_stress(self):
        for _ in range(30):
            for func in implemented_functions:
                a = random.randint(1, 1e3)
                b = random.randint(1, 1e3)
                start_time = time.time()
                func(a, b)
                elapsed_time = time.time() - start_time
                print("---")
                print(f'Function: {func}({a, b})')
                print(f'Elapsed seconds: {elapsed_time} for input:{a, b}')
                self.assertTrue(elapsed_time < TIME_LIMIT_SECONDS)
                print("---")


if __name__ == '__main__':
    unittest.main()
