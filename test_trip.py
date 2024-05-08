import unittest
import trip

class TestTrip(unittest.TestCase):

    def setUp(self):
        # Initialize test data
        self.test_trip_data = [
            trip.Trip("California", "Hiking", 3, "Sunny"),
            trip.Trip("New York", "Sightseeing", 2, "Rainy"),
            trip.Trip("Florida", "Beach", 4, "Sunny")
        ]

    def test_trip_initialization(self):
        # Test Trip initialization
        test_trip = trip.Trip("California", "Hiking", 3, "Sunny")
        self.assertEqual(test_trip.state, "California")
        self.assertEqual(test_trip.activity, "Hiking")
        self.assertEqual(test_trip.cost_rating, 3)
        self.assertEqual(test_trip.weather, "Sunny")

    def test_load_states_data(self):
        # Test loading data from CSV
        trips = trip.load_states_data('TripData.csv')
        self.assertEqual(len(trips), len(self.test_trip_data))
        for i in range(len(trips)):
            self.assertEqual(trips[i].state, self.test_trip_data[i].state)
            self.assertEqual(trips[i].activity, self.test_trip_data[i].activity)
            self.assertEqual(trips[i].cost_rating, self.test_trip_data[i].cost_rating)
            self.assertEqual(trips[i].weather, self.test_trip_data[i].weather)

    def test_get_unique_values(self):
        # Test getting unique values
        unique_activities = trip.get_unique_values(self.test_trip_data, 'activity')
        self.assertEqual(sorted(unique_activities), sorted(["Hiking", "Sightseeing", "Beach"]))


        unique_weather = trip.get_unique_values(self.test_trip_data, 'weather')
        self.assertEqual(sorted(unique_weather), sorted(["Sunny", "Rainy"]))


    # Add more test methods for other functions like poll_user_preferences, recommend_trip, etc.

class TestTraveler(unittest.TestCase):

    def test_traveler_initialization(self):
        # Test Traveler initialization
        test_traveler = trip.Traveler("John", "password123", 1000)
        self.assertEqual(test_traveler.name, "John")
        self.assertEqual(test_traveler.password, "password123")
        self.assertEqual(test_traveler.budget, 1000)
        self.assertEqual(test_traveler.trips, [])
        self.assertIsNone(test_traveler.activity)
        self.assertIsNone(test_traveler.weather)

    def test_add_trip_to_traveler(self):
        # Test adding trip to Traveler
        test_traveler = trip.Traveler("John", "password123", 1000)
        test_trip = trip.Trip("California", "Hiking", 3, "Sunny")
        test_traveler.add_trip("California", 3, ["Hiking"], "Sunny")
        self.assertEqual(len(test_traveler.trips), 1)
        self.assertEqual(test_traveler.trips[0].state, "California")
        self.assertEqual(test_traveler.trips[0].activity, "Hiking")
        self.assertEqual(test_traveler.trips[0].cost_rating, 3)
        self.assertEqual(test_traveler.trips[0].weather, "Sunny")

    # Add more test methods for other functionalities in the Traveler class

class TestTripFunctions(unittest.TestCase):

    def setUp(self):
        self.test_trips = [
            trip.Trip("California", "Hiking", 3, "Sunny"),
            trip.Trip("New York", "Sightseeing", 2, "Rainy"),
            trip.Trip("Florida", "Beach", 4, "Sunny")
        ]

    def test_recommend_trip(self):
        recommended_trip = trip.recommend_trip(self.test_trips, 1000, "Hiking", "Sunny")
        self.assertIsNotNone(recommended_trip)
        self.assertEqual(recommended_trip.state, "California")

        recommended_trip = trip.recommend_trip(self.test_trips, 700, "Beach", "Sunny")
        self.assertIsNotNone(recommended_trip)
        self.assertEqual(recommended_trip.state, "Florida")

        recommended_trip = trip.recommend_trip(self.test_trips, 2000, "Sightseeing", "Rainy")
        self.assertIsNotNone(recommended_trip)
        self.assertEqual(recommended_trip.state, "New York")

    def test_get_random_trip(self):
        random_trip = trip.get_random_trip(self.test_trips, "Hiking")
        self.assertIsNotNone(random_trip)
        self.assertEqual(random_trip.activity, "Hiking")

        random_trip = trip.get_random_trip(self.test_trips, "Camping")
        self.assertIsNone(random_trip)

        random_trip = trip.get_random_trip([], "Hiking")
        self.assertIsNone(random_trip)

    # Add more test methods for other utility functions in trip.py

if __name__ == '__main__':
    unittest.main()
