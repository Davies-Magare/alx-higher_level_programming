#!/usr/bin/python3

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_base(self):
        first = Base()
        self.assertEqual(first.id, 1)

        second = Base(4)
        self.assertEqual(second.id, 4)

        first = Base([1,2])
        self.assertEqual(first.id, [1,2])

    def test_base_Typevalue(self):
        with self.assertRaises(TypeError):
            Base(4, 5)

if __name__ == '__main__':
    unittest.main()
