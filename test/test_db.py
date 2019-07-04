#!/usr/bin/env python

import os
import unittest

from db.db import DB

class TestDB(unittest.TestCase):
    def setUp(self):
        self.actual_output = []
        self.db = DB()

        self.longMessage=True
        self.test_data_dir='{}/data/'.format(os.path.dirname(__file__))

    def read_lines(self, filename):
        with open(filename, 'r') as f:
            result = [line.strip() for line in f if line.strip() != None]
            return result

    def test_basic_commands_1(self):
        self.worker('basic-1')

    def test_basic_commands_2(self):
        self.worker('basic-2')

    def test_transactional_commands_1(self):
        self.worker('transactional-1')

    def test_transactional_commands_2(self):
        self.worker('transactional-2')

    def test_transactional_commands_3(self):
        self.worker('transactional-3')

    def test_transactional_commands_4(self):
        self.worker('transactional-4')

    def worker(self, title):
        out_file = '{}{}-out.txt'.format(self.test_data_dir, title)
        expected_output = self.read_lines(out_file)

        queries =self.read_lines('{}{}-in.txt'.format(self.test_data_dir, title))
        self.run_queries(queries)
        
        self.assertEqual(len(self.actual_output),len(expected_output),
            'Query result differ in length from {}'.format(out_file))

        for i, actual in enumerate(self.actual_output):
            self.assertEqual(str(actual), expected_output[i],
            'query result line {} does not match {}'.format(i+1, out_file))

    def run_queries(self, queries):
        for query in queries:
            try:
                result = self.db.run(query)
                if result != None:
                    self.actual_output.append(result)
            except:
                break

def test():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDB)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    test()
