"""
Unreliable car class
"""

from prac_08.taxi.car import Car
import random


class UnreliableCar(Car):
    """Represent unreliable car class"""
    def __init__(self, name, fuel, reliability):
        """Specialized version of a Car that includes reliability."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Indicate whether drive distance is zero or not using a random number generated"""
        if self.reliability > random.randint(1, 100):
            distance = super().drive(distance)
        else:
            distance = 0
        return
