"""
Silver service taxi
"""

from prac_08.taxi.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialized version of a Taxi that includes additional costs."""
    flag_fall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = self.price_per_km * fanciness

    def get_fare(self):
        """Calculation of flagfall cost and new taxi fare with fanciness accounted for"""
        return super().get_fare() + self.flag_fall

    def __str__(self):
        """Overwrite __str__ in order to add a flagfall cost."""
        return f"{super().__str__()} with an additional flagfall cost of ${self.flag_fall:.2f}"
