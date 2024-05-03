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

def get_unique_values(trips, attribute):
    """
    Get unique values for a specific attribute from the list of trips.
    Args:
    trips (list): a list of Trip objects
    attribute (str): the attribute to extract unique values from
    Returns:
    list: a list of unique values for the specified attribute
    """
    values = set(getattr(trip, attribute.lower()) for trip in trips)
    return list(values)

def poll_user_preferences(trips):
    """
    Poll the user for their preferences.
    Returns:
    tuple: a tuple containing user's budget, desired activity, and preferred weather
    """
    # budget = float(input("Enter your budget: "))
    # activity = ("These are some fun activities to try! Choose one activity: ", ', '.join(get_unique_values(trips, 'activity')), '\n Enter your desired activity: ' )
    # #activity = input("Enter your desired activity: ")
    # weather = input("Enter your preferred weather conditions: ")
    name = input("Enter your name: ")
    print(f"\n Hi {name}, Welcome to Trip Planner! We will be asking you  a few questions to match with the best fitting trip for your preferences and your budget! \n")
    print("Here's a list of fun activities you can choose from: ", ', '.join(get_unique_values(trips, 'activity')))

    # Get unique weather options
    all_weather = get_unique_values(trips, 'weather')

    while True:
        activity_input = input("\n What do you call a good time? (Enter one activity option): ").strip().title()
        if activity_input not in get_unique_values(trips, 'activity'):
            print("Invalid activity. Please choose from the provided options.")
        else:
            activity = activity_input
            break

    while True:
        weather_input = input(f"What's your preferred weather conditions? Here are the available options: {all_weather}. "
                              "(Enter one weather option): ").strip().title()
        if weather_input not in all_weather:
            print("Invalid weather condition. Please choose from the provided options.")
        else:
            weather = weather_input
            break

    while True:
        try:
            budget = float(input("Enter your budget: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for the budget.")

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
            if budget <= 300 and trip.cost_rating <= 2:
                suitable_trips.append(trip)
            elif budget <= 500 and trip.cost_rating <= 3:
                suitable_trips.append(trip)
            elif budget <= 1000 and trip.cost_rating <= 4:
                suitable_trips.append(trip)
            elif budget <= 1500 and trip.cost_rating <= 4:
                suitable_trips.append(trip)
            elif budget >= 1501 and trip.cost_rating <= 5:
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
    budget, activity, weather = poll_user_preferences(trips)
    recommended_trip = recommend_trip(trips, budget, activity, weather)

    if recommended_trip:
        print(f"We think you would enjoy a trip to {recommended_trip.state}. It is within your budget of ${budget} with a cost rating of {'$' * recommended_trip.cost_rating }. It is nice and {recommended_trip.weather} and you would be able to try {recommended_trip.activity}!")
        add_trip = input("Would you like to add this trip? (Yes/No): ")
        if add_trip.lower() == 'yes':
                # Implement code to add trip to traveler's list of trips
                print(f"Trip to {recommended_trip.state} added to your list of trips.")
        else:
                print("No trip added.")
    else:
        random_trip = get_random_trip(trips, activity)
        if random_trip:
            print(f"I can't find a suitable trip for your preferences, but what about a trip to {random_trip.state}. "
                  f"It would be nice and {random_trip.weather.lower()} but you would still be able to try {random_trip.activity.lower()}. "
                  f"Cost Rating: {'$' * random_trip.cost_rating}.")
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
