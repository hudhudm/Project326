"""
Trip Planner
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

