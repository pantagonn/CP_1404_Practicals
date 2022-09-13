"""
Silver service taxi
"""

from prac_08.taxi.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialized version of a Taxi that includes additional costs."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = self.price_per_km * fanciness

    def get_fare(self):
        """Addition of flagfall cost and new taxi fare with fanciness"""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Overwrite __str__ in order to add a flagfall."""
        return "{} with extra flagfall cost of ${:.2f}".format(super().__str__(), self.flagfall)