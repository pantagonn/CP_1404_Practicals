"""
Testing taxi code
"""
from prac_08.taxi.taxi import Taxi

prius_one = Taxi(name="Prius 1", fuel=100)
prius_one.drive(40)
print(prius_one)
print("\n-------after meter restart-------")
prius_one.start_fare()
prius_one.drive(100)
print(prius_one)
print("Fare:${:.2f}".format(prius_one.get_fare()))