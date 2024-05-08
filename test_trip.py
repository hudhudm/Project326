import unittest
import trip

class TestTrip(unittest.TestCase):
    """ 
    Test cases for the Trip class and related functions
    """
    def setUp(self):
        """
        Initializes test data for Trip class
        """
        self.test_trip_data = [
            trip.Trip("California", "Hiking", 3, "Sunny"),
            trip.Trip("New York", "Sightseeing", 2, "Rainy"),
            trip.Trip("Florida", "Beach", 4, "Sunny")
        ]

    def test_trip_initialization(self):
        """
        Test the initialization of the Trip class
        """
        test_trip = trip.Trip("California", "Hiking", 3, "Sunny")
        self.assertEqual(test_trip.state, "California")
        self.assertEqual(test_trip.activity, "Hiking")
        self.assertEqual(test_trip.cost_rating, 3)
        self.assertEqual(test_trip.weather, "Sunny")

    def test_load_states_data(self):
        """
        Test loading data for states
        """
        trips = trip.load_states_data('TripData.csv')
        self.assertEqual(len(trips), 50)
        self.assertEqual(trips[0].state, "Alabama")
        self.assertEqual(trips[0].activity, "Golfing")
        self.assertEqual(trips[0].cost_rating, 3)
        self.assertEqual(trips[0].weather, "Warm")

    def test_get_unique_values(self):
        """
        Test getting unique values from trip data csv
        """
        unique_activities = trip.get_unique_values(self.test_trip_data, 'activity')
        self.assertEqual(sorted(unique_activities), sorted(["Hiking", "Sightseeing", "Beach"]))


        unique_weather = trip.get_unique_values(self.test_trip_data, 'weather')
        self.assertEqual(sorted(unique_weather), sorted(["Sunny", "Rainy"]))

class TestTraveler(unittest.TestCase):
    """
    Test cases for the Traveler class and related functions
    """
    def test_traveler_initialization(self):
        """
        Test the initializations of the Traveler class
        """
        test_traveler = trip.Traveler("John", "password123", 1000)
        self.assertEqual(test_traveler.name, "John")
        self.assertEqual(test_traveler.password, "password123")
        self.assertEqual(test_traveler.budget, 1000)
        self.assertEqual(test_traveler.trips, [])
        self.assertIsNone(test_traveler.activity)
        self.assertIsNone(test_traveler.weather)

    def test_add_trip_to_traveler(self):
        """
        Test adding a trip for a Traveler
        """
        test_traveler = trip.Traveler("John", "password123", 1000)
        test_trip = trip.Trip("California", "Hiking", 3, "Sunny")
        test_traveler.add_trip("California", 3, ["Hiking"], "Sunny")
        self.assertEqual(len(test_traveler.trips), 1)
        self.assertEqual(test_traveler.trips[0].state, "California")
        self.assertEqual(test_traveler.trips[0].activity[0], "Hiking")
        self.assertEqual(test_traveler.trips[0].cost_rating, 3)
        self.assertEqual(test_traveler.trips[0].weather, "Sunny")

class TestTripFunctions(unittest.TestCase):
    """
    Test cases for utility functions related to trips
    """
    def setUp(self):
        """
        Initialize test data for utility functions
        """
        self.test_trips = [
            trip.Trip("California", "Hiking", 3, "Sunny"),
            trip.Trip("New York", "Sightseeing", 2, "Rainy"),
            trip.Trip("Florida", "Beach", 4, "Sunny")
        ]

    def test_recommend_trip(self):
        """
        Test recommending a trip for a traveler or group 
        """
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
        """
        Test getting a random trip
        """
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
