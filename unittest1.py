import unittest

from flight_calculator import calculate_flight_time


class TestCalculateFlightTime(unittest.TestCase):
    def test_zero_weight_returns_baseline_flight_time(self):
        self.assertEqual(calculate_flight_time(0), 180.0)

    def test_positive_weight_reduces_flight_time(self):
        self.assertEqual(calculate_flight_time(500), 130.0)

    def test_fractional_weight_returns_expected_flight_time(self):
        self.assertAlmostEqual(calculate_flight_time(125.5), 167.45)

    def test_large_weight_is_clamped_to_zero(self):
        self.assertEqual(calculate_flight_time(1800), 0.0)

    def test_negative_weight_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "Weight cannot be negative."):
            calculate_flight_time(-1)


if __name__ == "__main__":
    unittest.main()