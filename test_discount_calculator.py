import unittest
from discount_calculator import DiscountCalculator

class DiscountCalculatorTests(unittest.TestCase):
    def test_twenty_percent_discount(self):
        discount_calculator = DiscountCalculator()
        result = discount_calculator.calculate(100, 20, 'percent')
        self.assertEqual(20.0, result)
        
        