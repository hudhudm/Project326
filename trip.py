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
    """
    Initializes a Traveler object.
        
    Args:
        name (str): the name of the traveler
        budget (float): the budget of the individual traveler
    """
    def __init__(self, name, password, budget):
        self.name = name
        self.password = password
        self.budget = budget
        self.trips = []
        self.activity = None
        self.weather = None

    def add_trip(self, destination, cost_rating, activities, weather):
        """
        Adds a trip to the traveler's list of trips.
        
        Args:
            destination (str): the name of the destination state
            cost (int): cost of the trip
            activities (list): list of activities for the trip
        """
        new_trip = Trip(destination, activities, cost_rating, weather)
        self.trips.append(new_trip)

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
    print("Here's a list of fun activities you can choose from: ", ', '.join(get_unique_values(trips, 'activity')))
    all_weather = get_unique_values(trips, 'weather')
    while True:
        activity_input = input("\nWhat do you call a good time? (Enter one activity option): ").strip().title()
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
        return suitable_trips[0]
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
    group_size = int(input("Enter the number of travelers in the group: "))
    travelers = []
    for i in range(group_size):
        name = input(f"Enter name of traveler {i+1}: ")
        password = input(f"Enter password for traveler {i+1}: ")  # You can choose to include password functionality
        budget, activity, weather = poll_user_preferences(trips)
        traveler = Traveler(name, password, budget)
        traveler.activity = activity
        traveler.weather = weather
        travelers.append(traveler)

    common_activity = set(get_unique_values(trips, 'activity'))
    common_weather = set(get_unique_values(trips, 'weather'))
    common_budget = sum(traveler.budget for traveler in travelers) / group_size

    for traveler in travelers:
        recommended_trip = recommend_trip(trips, traveler.budget, traveler.activity, traveler.weather)
        if recommended_trip:
            print(f"{traveler.name}, we recommend a trip with your group to {recommended_trip.state}. "
                  f"It is within your budget of ${traveler.budget} with a cost rating of {'$' * recommended_trip.cost_rating }. "
                  f"It is nice and {recommended_trip.weather} and you would be able to try {recommended_trip.activity}!")
            add_trip = input("Would you like to add this trip? (Yes/No): ")
            if add_trip.lower() == 'yes':
                traveler.add_trip(recommended_trip.state, [recommended_trip.activity], recommended_trip.cost_rating, recommended_trip.weather)
                print(f"Trip to {recommended_trip.state} added to your list of trips.")
            else:
                print("No trip added.")
        else:
            random_trip = get_random_trip(trips, traveler.activity)
            if random_trip:
                print(f"{traveler.name}, we can't find a suitable trip for your preferences, "
                      f"but what about a trip to {random_trip.state}. "
                      f"It would be nice and {random_trip.weather.lower()} but you would still be able to try {random_trip.activity.lower()}. "
                      f"Cost Rating: {'$' * random_trip.cost_rating}.")
                add_trip = input("Would you like to add this trip? (Yes/No): ")
                if add_trip.lower() == 'yes':
                    traveler.add_trip(random_trip.state, [random_trip.activity], random_trip.cost_rating, random_trip.weather)
                    print(f"Trip to {random_trip.state} added to your list of trips.")
                else:
                    print("No trip added.")
            else:
                print(f"{traveler.name}, no suitable trip found based on your preferences.")

    # Additional group functionalities can be implemented here

if __name__ == "__main__":
    main()
