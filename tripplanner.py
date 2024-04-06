"""
Trip Planner Project
"""

import sys
import argparse
import math

class Traveler:
    def __init__(self, name, budget = 0, trip = []):
        """
       This function initializes the attributes of a Traveler object.
       Args:
       self(Traveler) the current instance of the Traveler class
       name(str) the name of the traveler
       budget(float) the budget of the individual traveler
	    trips(list) list of Trip objects under the traveler can access and edit


       Returns: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       """
        self.name = name
        self.budget = budget
        self.trip = []

class Trip:
    def __init__(self):
        """
        This function creates default destination, cost, and activities attributes.
        """
        self.destination = ""
        self.cost = 0
        self.activities = []

    def addTrip(self, destination, cost, activity):
        """
         This function allows the user to add a trip to their traveler attribute.
        
        Args:
            activity (str): the name of the activity desired at the destination
            destination (str): the name of the destination state
            cost (int): cost of the trip 
        Returns:
            str: activity, destination, and cost for the trip
        """
        self.activities.append(activity)
        self.destination = destination
        self.cost = cost
        return f"Trip added to: {destination} with activity {activity} with a cost of ${cost}"