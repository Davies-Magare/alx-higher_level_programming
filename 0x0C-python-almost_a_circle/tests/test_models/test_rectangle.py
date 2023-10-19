import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_args(self):
        second = Rectangle(10, 2, 0, 0)
        self.assertEqual(second.id, 3)
        self.assertEqual(second.width, 10)
        self.assertEqual(second.height, 2)
        self.assertEqual(second.x, 0)
        self.assertEqual(second.y, 0)

        first = Rectangle(10, 2, 0, 0, 79)
        self.assertEqual(first.id, 79)

    def test_exception(self):
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle((4, ))
        with self.assertRaises(TypeError):
            Rectangle({4: 'davies'})
        with self.assertRaises(TypeError):
            Rectangle([])
        with self.assertRaises(ValueError):
            Rectangle(-4, 3)
        with self.assertRaises(ValueError):
            Rectangle(4, -3)
        with self.assertRaises(TypeError):
            Rectangle(4, [], 1, 1, 0)
        with self.assertRaises(TypeError):
            Rectangle(4, (1,), 1, 1, 0)
        with self.assertRaises(TypeError):
            Rectangle(4, "1", 1, 1, 0)
        with self.assertRaises(TypeError):
            Rectangle(4, {1: "st"}, 1, 1, 0)
        with self.assertRaises(ValueError):
            Rectangle(4, 3, -2, 1, 0)
        with self.assertRaises(ValueError):
            Rectangle(4, 3, 2, -1, 0)
        with self.assertRaises(ValueError):
            Rectangle(0, 3, 2, 1, 0)
        with self.assertRaises(ValueError):
            Rectangle(3, 0, 2, 1, 0)
        with self.assertRaises(TypeError):
            Rectangle(4.5, 0, 2, 1, 0)
        with self.assertRaises(TypeError):
            Rectangle(4, 1.5, 0, 1, 0)
        with self.assertRaises(TypeError):
            Rectangle(4, 1, 1.5, 1, 0)
        with self.assertRaises(TypeError):
            Rectangle(4, 1, 1, 1.5, 0)
        with self.assertRaises(TypeError):
            Rectangle(4, 1, [], 1, 0)
        with self.assertRaises(TypeError):
            Rectangle(4, 1, {4: 'cat'}, 1, 0)
        with self.assertRaises(TypeError):
            Rectangle(4, 1, (2,), 1, 0)
        with self.assertRaises(TypeError):
            Rectangle(4, 1, 1, [], 0)
        with self.assertRaises(TypeError):
            Rectangle(4, 1, 1, {4: 'dav'}, 0)
        with self.assertRaises(TypeError):
            Rectangle(4, 1, 1, "1", 0)
        with self.assertRaises(TypeError):
            Rectangle(4, 1, "2", 1, 0)

    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
    


    if __name__ == '__main__':
        unittest.main()

