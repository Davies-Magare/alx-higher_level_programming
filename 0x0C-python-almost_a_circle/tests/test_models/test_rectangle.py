import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_args(self):
        first = Rectangle(4, 5)
        self.assertEqual(first.id, 2)

        second = Rectangle(4, [2, 3])
        self.assertEqual(second.id, 3)

        second = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(second.id, 12)

        second = Rectangle(10, 2, 0, 0)
        self.assertEqual(second.id, 4)

    def test_exception(self):
        with self.assertRaises(TypeError):
            Rectangle()
        
        with self.assertRaises(TypeError):
            Rectangle(4)

    if __name__ == '__main__':
        unittest.main()

