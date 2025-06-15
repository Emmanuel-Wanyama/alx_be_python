import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Create an instance of SimpleCalculator for testing."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5) # Test positive numbers
        self.assertEqual(self.calc.add(-1, 1), 0) # Test negative and positive numbers
        self.assertEqual(self.calc.add(-1, -1), -2) #test negative numbers
        self.assertEqual(self.calc.add(0, 0), 0) #test zero addition
        self.assertEqual(self.calc.add(0, 5), 5) #test zero addition with positive number

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2) # Test positive numbers
        self.assertEqual(self.calc.subtract(3, 5), -2) #test negative result
        self.assertEqual(self.calc.subtract(-1, -1), 0) #test negative numbers
        self.assertEqual(self.calc.subtract(0, 0), 0) #test zero subtraction
        self.assertEqual(self.calc.subtract(5, 0), 5) #test zero subtraction with positive number   

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6) # Test positive numbers
        self.assertEqual(self.calc.multiply(-1, 1), -1) #test negative and positive numbers
        self.assertEqual(self.calc.multiply(-1, -1), 1) #test negative numbers
        self.assertEqual(self.calc.multiply(0, 5), 0) #test zero multiplication
        self.assertEqual(self.calc.multiply(-1, 5), -5) #test negative multiplication with positive number
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0) #test float multiplication

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(5, 0), None)  # Division by zero should return None
        self.assertEqual(self.calc.divide(-6, 3), -2)  # Negative dividend
    
    def test_divide_by_zero(self):
        """
        Tests the divide method with a zero denominator.
        Asserts that a ValueError is raised as expected.
        """
        with self.assertRaises(ValueError):
            self.calculator.divide(10, 0)
        with self.assertRaises(ValueError):
            self.calculator.divide(-5, 0)

if __name__ == '__main__':
    # Runs all tests in the TestSimpleCalculator class when the script is executed.
    unittest.main()
