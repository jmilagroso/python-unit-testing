import unittest
from add import Add

class TestAdd(unittest.TestCase):
    def test_add_equal(self):
        expected = 30

        sum = Add.perform(10, 20)
        
        self.assertEqual(sum, expected)

    def test_add_failed(self):
        expected = 50

        sum = Add.perform(10, 20)
        
        self.assertNotEqual(sum, expected)

if __name__ == '__main__':
    unittest.main()
