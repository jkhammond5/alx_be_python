import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # Addition tests
    def test_addition_integers(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(1000, 2000), 3000)

    def test_addition_floats(self):
        self.assertAlmostEqual(self.calc.add(2.5, 1.2), 3.7)
        self.assertAlmostEqual(self.calc.add(-1.1, -2.2), -3.3)

    def test_addition_commutativity(self):
        self.assertEqual(self.calc.add(7, 4), self.calc.add(4, 7))

    # Subtraction tests
    def test_subtraction_integers(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(5, 10), -5)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_subtraction_floats(self):
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3)
        self.assertAlmostEqual(self.calc.subtract(-1.0, -2.5), 1.5)

    # Multiplication tests
    def test_multiplication_integers(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 5), -10)
        self.assertEqual(self.calc.multiply(0, 100), 0)

    def test_multiplication_floats(self):
        self.assertAlmostEqual(self.calc.multiply(2.5, 4.0), 10.0)
        self.assertAlmostEqual(self.calc.multiply(-1.5, -2), 3.0)

    def test_multiplication_commutativity(self):
        self.assertEqual(self.calc.multiply(6, 7), self.calc.multiply(7, 6))

    # Division tests
    def test_division_normal(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertAlmostEqual(self.calc.divide(7, 3), 7 / 3)

    def test_division_result_float(self):
        self.assertAlmostEqual(self.calc.divide(5, 2), 2.5)

    def test_division_negative(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(10, -2), -5)
        self.assertEqual(self.calc.divide(-10, -2), 5)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))  # by spec, dividing 0/0 returns None

    # Edge / robustness tests
    def test_large_numbers(self):
        self.assertEqual(self.calc.add(10**12, 10**12), 2 * 10**12)
        self.assertEqual(self.calc.multiply(10**6, 10**6), 10**12)
        self.assertAlmostEqual(self.calc.divide(10**12, 2), 5 * 10**11)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            _ = self.calc.add("a", 5)
        with self.assertRaises(TypeError):
            _ = self.calc.subtract(5, "b")
        with self.assertRaises(TypeError):
            _ = self.calc.multiply("x", 3)
        # divide with non-numeric should raise; behavior not defined in original class so we expect TypeError
        with self.assertRaises(TypeError):
            _ = self.calc.divide(10, "y")


if __name__ == "__main__":
    unittest.main()
