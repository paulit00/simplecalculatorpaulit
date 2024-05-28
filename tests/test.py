import math
from simplecalculatorpaulit import Calculator, ScientificCalculator,StatisticsCalculator

import unittest

class Test(unittest.TestCase):
    calculations = Calculator()
    scientific_calculations = ScientificCalculator()
    statistics_calculations = StatisticsCalculator([1, 3, 3, 4, 5])
    
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
    
    def test_07_test_sine(self):
        self.scientific_calculations.add(30)
        self.assertAlmostEqual(self.scientific_calculations.sine(), 0.5, places=1, msg='Should be 0.5')

    def test_08_test_cosine(self):
        self.scientific_calculations.reset()
        self.scientific_calculations.add(60)
        self.assertAlmostEqual(self.scientific_calculations.cosine(), 0.5, places=1, msg='Should be 0.5')

    def test_09_test_tangent(self):
        self.scientific_calculations.reset()
        self.scientific_calculations.add(45)
        self.assertAlmostEqual(self.scientific_calculations.tangent(), 1, places=1, msg='Should be 1')

    def test_10_test_log(self):
        self.scientific_calculations.reset()
        self.scientific_calculations.add(100)
        self.assertAlmostEqual(self.scientific_calculations.log(), 2, places=1, msg='Should be 2')

    def test_11_test_ln(self):
        self.scientific_calculations.reset()
        self.scientific_calculations.add(math.e)
        self.assertAlmostEqual(self.scientific_calculations.ln(), 1, places=1, msg='Should be 1')

    def test_12_test_power(self):
        self.scientific_calculations.reset()
        self.scientific_calculations.add(2)
        self.assertEqual(self.scientific_calculations.power(3), 8, 'Should be 8')

    def test_14_test_mean(self):
        self.assertEqual(self.statistics_calculations.mean(), 3.2)

    def test_15_test_median(self):
        self.assertEqual(self.statistics_calculations.median(), 3.0)

    def test_16_test_standard_deviation(self):
        self.assertAlmostEqual(self.statistics_calculations.standard_deviation(), 1.3266, places=4)

    def test_17_test_variance(self):
        self.assertAlmostEqual(self.statistics_calculations.variance(), 1.76, places=2)

if __name__ == '__main__':
    unittest.main()