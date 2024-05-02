"""
Trip Planner Project
"""

import sys
import argparse
import math
Database(Travelers(Trip))
class Traveler:
    # Sign in 
    # make a dictionary of users
    # key username value password
    # if name is not in dictionary append to dictionary if it is start the program
    def __init__(self, name, budget = 0, trip = []):
        """
       This function initializes the attributes of a Traveler object.
       
       Args:
        self(Traveler): the current instance of the Traveler class
        name(str): the name of the traveler
        budget(float): the budget of the individual traveler
	    trips(list): list of Trip objects under the traveler can access and edit

       Returns: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       """
        self.name = name
        self.budget = budget
        self.trip = []
        
    def addTrip(self):
        """
         This function allows the user to add a trip to their r trip attribute.
        
        Args:
            activity (str): the name of the activity desired at the destination
            destination (str): the name of the destination state
            cost (int): cost of the trip 
        
        Returns:
            str: activity, destination, and cost for the trip
        """
        trip.append(Trip)
        
        return f"Trip added to: {newTrip.destination} with activity {newTrip.activity} with a cost of ${newTrip.cost}"

class Trip:
    def __init__(self):
        """
        This function creates default destination, cost, and activities attributes.
        """
        self.destination = ""
        self.cost = 0
        self.activities = []

   
    
    