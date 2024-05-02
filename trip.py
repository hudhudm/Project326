"Trip Planner Project"

class Trip:
    def __init__(self, state, activity, cost_rating, weather):
        """
        Initializes a Trip object.
        Args:
        state (str): the name of the destination state
        activity (str): the activity available at the destination
        cost_rating (int): the average cost rating on a scale of 1-5
        weather (str): the average weather conditions
        """
        self.state = state
        self.activity = activity
        self.cost_rating = cost_rating
        self.weather = weather

class Traveler:
    def __init__(self, name, budget):
        """
        Initializes a Traveler object.
        Args:
        name (str): the name of the traveler
        budget (float): the budget of the individual traveler
        """
        self.name = name
        self.budget = budget
        self.trips = []

    def add_trip(self, destination, cost, activities):
        """
        Adds a trip to the traveler's list of trips.
        Args:
        destination (str): the name of the destination state
        cost (int): cost of the trip
        activities (list): list of activities for the trip
        """
        trip = Trip(destination, cost, activities)
        self.trips.append(trip)

# Planner.py - Driver script

import csv

def load_states_data(filename):
    """
    Load data from the states.csv file.
    Args:
    filename (str): the name of the CSV file
    Returns:
    list: a list of Trip objects
    """
    trips = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            trip = Trip(row['state'], row['activity'], int(row['cost_rating']), row['weather'])
            trips.append(trip)
    return trips

def poll_user_preferences():
    """
    Poll the user for their preferences.
    Returns:
    tuple: a tuple containing user's budget, desired activity, and preferred weather
    """
    budget = float(input("Enter your budget: "))
    activity = input("Enter your desired activity: ")
    weather = input("Enter your preferred weather conditions: ")
    return budget, activity, weather

def recommend_trip(trips, budget, activity, weather):
    """
    Recommend an ideal trip based on user's preferences.
    Args:
    trips (list): a list of Trip objects
    budget (float): user's budget
    activity (str): user's desired activity
    weather (str): user's preferred weather conditions
    Returns:
    Trip: the recommended trip object
    """
    suitable_trips = []
    for trip in trips:
        if trip.activity.lower() == activity.lower() and trip.weather.lower() == weather.lower():
            if 1 <= trip.cost_rating <= 5:
                suitable_trips.append(trip)

    if suitable_trips:
        return suitable_trips[0]  # Return the first suitable trip found
    else:
        return None

def main():
    trips = load_states_data('states.csv')
    budget, activity, weather = poll_user_preferences()
    recommended_trip = recommend_trip(trips, budget, activity, weather)

    if recommended_trip:
        print(f"Recommended trip: {recommended_trip.state}")
    else:
        print("No suitable trip found based on your preferences.")

if __name__ == "__main__":
    main()
