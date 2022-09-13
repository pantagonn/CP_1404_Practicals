"""
Unreliable car test
"""

from prac_08.unreliable_car.unreliable_car import UnreliableCar

# car_one = UnreliableCar(name="Subaru 2002", fuel=150, reliability=42)
car_two = UnreliableCar(name="Toyota Soluna 2005", fuel=240, reliability=33)
car_two.drive(50)
print(f"{car_two.name} has attempted to drive 50 miles and managed to drive {car_two.odometer} miles in total. {car_two.fuel} of fuel remaining.")
