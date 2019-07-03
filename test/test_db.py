#!/usr/bin/env python

import os
import unittest

from db.db import DB

class TestDB(unitest.TestCase):
    def setUp(self):
        self.actual_output = []
        self.db = DB()

    def test_get(self):
        pass

def test():
    suit = unitest.TestLoader().loadTestsFromTestCase(TestDB)
    unitest.TextTestRunner(verbosity=2).run(suite)

if __name__ = '__main__':
    test()
