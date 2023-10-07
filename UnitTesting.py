import unittest
import calc


class TestCalc(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-100, 34), -66)
        self.assertEqual(calc.add(-1, 100), 99)
        
    def test_subtract(self):
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-100, 34), -134)
        self.assertEqual(calc.subtract(-1, 100), -101)
        
    def test_multiply(self):
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-100, 34), -3400)
        self.assertEqual(calc.multiply(-1, 100), -100)
        
    def test_divide(self):
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-100, 20), -5)
        self.assertEqual(calc.divide(-1, -1), 1)
        
        with self.assertRaises(ValueError):
            calc.divide(10, 0)
        
        
if __name__ == "__main__":
    unittest.main()