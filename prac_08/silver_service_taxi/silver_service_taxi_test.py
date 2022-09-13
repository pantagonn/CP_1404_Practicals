"""
Silver service taxi test
"""

from prac_08.silver_service_taxi.silver_service_taxi import SilverServiceTaxi

my_taxi = SilverServiceTaxi("Royce Phantom", 300, 3)
my_taxi.drive(21)
print(my_taxi)
print(f"Fare: ${my_taxi.get_fare()}")