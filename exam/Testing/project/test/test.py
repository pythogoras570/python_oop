import unittest
from collections import deque
from project.railway_station import RailwayStation


class TestRailwayStation(unittest.TestCase):
    def setUp(self):
        self.station = RailwayStation("Test Station")

    def test_constructor(self):
        self.assertEqual(self.station.name, "Test Station")
        self.assertIsInstance(self.station.arrival_trains, deque)
        self.assertIsInstance(self.station.departure_trains, deque)

    def test_name_property(self):
        with self.assertRaises(ValueError):
            self.station.name = "ab"  # Name should be more than 3 symbols
        self.assertEqual(self.station.name, "Test Station")

    def test_new_arrival_on_board(self):
        self.station.new_arrival_on_board("Train A")
        self.assertEqual(self.station.arrival_trains, deque(["Train A"]))

    def test_train_has_arrived(self):
        self.station.new_arrival_on_board("Train A")
        self.station.new_arrival_on_board("Train B")

        result = self.station.train_has_arrived("Train B")
        self.assertEqual(result, "There are other trains to arrive before Train B.")
        self.assertEqual(self.station.departure_trains, deque([]))  # No train should depart yet

        result = self.station.train_has_arrived("Train A")
        self.assertEqual(result, "Train A is on the platform and will leave in 5 minutes.")
        self.assertEqual(self.station.departure_trains, deque(["Train A"]))

    def test_train_has_left(self):
        self.station.new_arrival_on_board("Train A")
        self.station.train_has_arrived("Train A")

        result = self.station.train_has_left("Train A")
        self.assertTrue(result)
        self.assertEqual(self.station.departure_trains, deque())

        result = self.station.train_has_left("Train B")
        self.assertFalse(result)
        result = self.station.train_has_left("Nonexistent Train")
        self.assertFalse(result)

    def test_multiple_arrivals_and_departures(self):
        self.station.new_arrival_on_board("Train A")
        self.station.new_arrival_on_board("Train B")
        self.station.train_has_arrived("Train A")
        self.station.train_has_arrived("Train B")

        self.assertEqual(self.station.departure_trains, deque(["Train A", "Train B"]))

        result = self.station.train_has_left("Train A")
        self.assertTrue(result)
        self.assertEqual(self.station.departure_trains, deque(["Train B"]))

        result = self.station.train_has_left("Train B")
        self.assertTrue(result)
        self.assertEqual(self.station.departure_trains, deque())

    def test_train_has_left_nonexistent_train(self):
        result = self.station.train_has_left("Nonexistent Train")
        self.assertFalse(result)

    def test_getters_and_setters(self):
        # Test setter for name
        with self.assertRaises(ValueError):
            self.station.name = "ab"
        self.assertEqual(self.station.name, "Test Station")

        # Test setter for arrival_trains
        self.station.arrival_trains = deque(["Train X", "Train Y"])
        self.assertEqual(self.station.arrival_trains, deque(["Train X", "Train Y"]))

        # Test setter for departure_trains
        self.station.departure_trains = deque(["Train Z"])
        self.assertEqual(self.station.departure_trains, deque(["Train Z"]))

        # Test getters
        self.assertEqual(self.station.get_name(), "Test Station")
        self.assertEqual(self.station.get_arrival_trains(), deque(["Train X", "Train Y"]))
        self.assertEqual(self.station.get_departure_trains(), deque(["Train Z"]))


if __name__ == '__main__':
    unittest.main()
