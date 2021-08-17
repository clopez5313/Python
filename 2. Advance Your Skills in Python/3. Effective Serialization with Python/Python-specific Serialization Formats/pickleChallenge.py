"""Add __repr__ to Ride class and then loads rides from rides.pkl (pickle
format) and print repr of each ride.
"""
import pickle
from datetime import datetime


class Ride:
    def __init__(self, start, end, distance, num_passengers):
        self.start = start  # type: datetime
        self.end = end  # type: datetime
        self.distance = distance  # type: float
        self.num_passengers = num_passengers  # type: int

    def __repr__(self):
        return f"The Ride started at {self.start} and ended at {self.end}. It covered {self.distance} miles and carried {self.num_passengers} passengers."

if __name__ == "__main__":
    with open("rides.pkl", "rb") as theFile:
        while(True):
            try:
                ride = pickle.load(theFile)
                print(ride)
            except EOFError:
                break
