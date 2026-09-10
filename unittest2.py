import unittest

from flight_calculator import flight_time_table


class TestFlightTimeTable(unittest.TestCase):
    def test_zero_max_weight_returns_zero_entry(self):
        self.assertEqual(
            flight_time_table(0, 100),
            [(0, 180.0)],
        )

    def test_exact_step_divisions_include_max_weight(self):
        self.assertEqual(
            flight_time_table(1000, 250),
            [
                (0, 180.0),
                (250, 155.0),
                (500, 130.0),
                (750, 105.0),
                (1000, 80.0),
            ],
        )

    def test_non_divisible_max_weight_stops_before_exceeding_maximum(self):
        table = flight_time_table(1000, 300)

        self.assertEqual(
            table,
            [
                (0, 180.0),
                (300, 150.0),
                (600, 120.0),
                (900, 90.0),
            ],
        )
        self.assertLessEqual(table[-1][0], 1000)

    def test_max_weight_below_zero_returns_empty_table(self):
        self.assertEqual(flight_time_table(-1, 100), [])

    def test_step_larger_than_max_weight_returns_only_zero_entry(self):
        self.assertEqual(
            flight_time_table(100, 250),
            [(0, 180.0)],
        )

    def test_table_contains_weight_and_flight_time_tuples(self):
        table = flight_time_table(400, 200)

        self.assertTrue(all(isinstance(entry, tuple) for entry in table))
        self.assertTrue(all(len(entry) == 2 for entry in table))
        self.assertEqual([entry[0] for entry in table], [0, 200, 400])

    def test_flight_times_are_calculated_for_each_weight(self):
        table = flight_time_table(600, 200)

        expected_flight_times = [180.0, 160.0, 140.0]
        actual_flight_times = [flight_time for _, flight_time in table]

        self.assertEqual(actual_flight_times, expected_flight_times)

    def test_weights_are_in_ascending_step_order(self):
        table = flight_time_table(1000, 250)
        weights = [weight for weight, _ in table]

        self.assertEqual(weights, sorted(weights))
        self.assertEqual(
            [later - earlier for earlier, later in zip(weights, weights[1:])],
            [250, 250, 250, 250],
        )


if __name__ == "__main__":
    unittest.main()