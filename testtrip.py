import unittest
from unittest.mock import patch
from io import StringIO
from trip import main, recommended_trip

class TestMain(unittest.TestCase):

    @patch('builtins.input', side_effect=['yes'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_add_trip_yes(self, mock_stdout, mock_input):
        budget = 1000
        main(budget)
        self.assertEqual(mock_stdout.getvalue().strip(), 
                         f"We think you would enjoy a trip to {recommended_trip.state}. It is within your budget of ${budget} with a cost rating of {'$' * recommended_trip.cost_rating}. It is nice and {recommended_trip.weather} and you would be able to try {recommended_trip.activity}!\nTrip to {recommended_trip.state} added to your list of trips.")

    @patch('builtins.input', side_effect=['no'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_add_trip_no(self, mock_stdout, mock_input):
        budget = 1000
        main(budget)
        self.assertEqual(mock_stdout.getvalue().strip(), 
                         f"We think you would enjoy a trip to {recommended_trip.state}. It is within your budget of ${budget} with a cost rating of {'$' * recommended_trip.cost_rating}. It is nice and {recommended_trip.weather} and you would be able to try {recommended_trip.activity}!\nNo trip added.")

    @patch('builtins.input', side_effect=['yes'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_add_trip_budget_exceeded(self, mock_stdout, mock_input):
        budget = 500
        main(budget)
        self.assertEqual(mock_stdout.getvalue().strip(), 
                         f"We think you would enjoy a trip to {recommended_trip.state}. It is within your budget of ${budget} with a cost rating of {'$' * recommended_trip.cost_rating}. It is nice and {recommended_trip.weather} and you would be able to try {recommended_trip.activity}!\nNo trip added.")

    @patch('builtins.input', side_effect=['yes'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_add_trip_wrong_input(self, mock_stdout, mock_input):
        budget = 1000
        main(budget)
        self.assertNotEqual(mock_stdout.getvalue().strip(), "Invalid input")

    @patch('builtins.input', side_effect=['yes', 'no'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_add_trip_multiple_trips(self, mock_stdout, mock_input):
        budget = 1000
        main(budget)
        self.assertIn("Trip to", mock_stdout.getvalue().strip())
        self.assertIn("added to your list of trips.", mock_stdout.getvalue().strip())

if __name__ == '__main__':
    unittest.main()