from simplecalculatorpaulit import Calculator
import unittest

class Test(unittest.TestCase):
    calculations = Calculator()
    
    def test_01_test_add(self):
        self.assertEqual(self.calculations.add(10.5), 10.5, 'Should be 10.5')
    
    def test_02_test_reset(self):
        self.assertEqual(self.calculations.reset(), 0.0, 'Should be 0.0')

    def test_03_test_subtract(self):
        self.assertEqual(self.calculations.subtract(5), -5.0, 'Should be 5.0')
    
    def test_04_test_multiply(self):
        self.assertEqual(self.calculations.multiply(-2), 10.0, 'Should be 10.0')

    def test_05_test_divide(self):
        self.assertEqual(self.calculations.divide(0.1), 100.0, 'Should be 100.0')
    
    def test_06_test_root(self):
        self.assertEqual(self.calculations.root(2), 10.0, 'Should be 10.0')
    

if __name__ == '__main__':
    unittest.main()