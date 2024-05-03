import csv
import random

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
            trip = Trip(row['State'], row['Activity'], int(row['Cost']), row['Weather'])
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

def get_random_trip(trips, activity):
    """
    Generate a random trip matching the selected activity.
    Args:
    trips (list): a list of Trip objects
    activity (str): user's desired activity
    Returns:
    Trip: a random trip object matching the activity
    """
    matching_trips = [trip for trip in trips if trip.activity.lower() == activity.lower()]
    if matching_trips:
        return random.choice(matching_trips)
    else:
        return None

def main():
    trips = load_states_data('TripData.csv')
    budget, activity, weather = poll_user_preferences()
    recommended_trip = recommend_trip(trips, budget, activity, weather)

    if recommended_trip:
        print(f"Recommended trip: {recommended_trip.state}")
    else:
        random_trip = get_random_trip(trips, activity)
        if random_trip:
            print(f"I can't find a suitable trip for your preferences, but what about a trip to {random_trip.state}. "
                  f"It will be nice and {random_trip.weather.lower()} and you will be able to {random_trip.activity.lower()}. "
                  f"It would cost around {random_trip.cost_rating}.")
            add_trip = input("Would you like to add this trip? (Yes/No): ")
            if add_trip.lower() == 'yes':
                # Implement code to add trip to traveler's list of trips
                print(f"Trip to {random_trip.state} added to your list of trips.")
            else:
                print("No trip added.")
        else:
            print("No suitable trip found based on your preferences.")

if __name__ == "__main__":
    main()
