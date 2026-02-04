#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample5 (self):
                self.assertEqual (1, calc(1,1))

        def test_sample6 (self):
                self.assertEqual (998001, calc(999,999))

        def test_sample56 (self):
                self.assertEqual (999, calc(1,999))

        def test_sample7 (self):
                self.assertEqual (-1, calc(0,5))

        def test_sample8 (self):
                self.assertEqual (-1, calc(1000,3))

        def test_sample9 (self):
                self.assertEqual (-1, calc(1.1,3))
        
        def test_sample10 (self):
                self.assertEqual (-1, calc("a",3))


