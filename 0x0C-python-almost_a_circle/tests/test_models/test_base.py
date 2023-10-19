#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle

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

    def test_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary, '[{"id": 2, "width": 10, "height": 7, "x": 2, "y": 8}]')

        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, '[]')

        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, '[]')




if __name__ == '__main__':
    unittest.main()
