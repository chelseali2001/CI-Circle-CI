import unittest
import calculator

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(calculator.add(1, 2), 3)

    def test0(self):
        self.assertEqual(calculator.sub(3, 2), 1)
    
    def test1(self):
        self.assertEqual(calculator.mul(2, 2), 4)

    def test2(self):
        self.assertEqual(calculator.div(4, 2), 2.0)

if __name__ == '__main__':
    unittest.main()