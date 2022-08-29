"""
Guitar's description & features
"""


class Guitar:
    """Describe guitar """

    def __init__(self, name="", year=0, cost=0):
        """Constructor"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return the guitar information"""
        return '{} ({}) : ${:.2f}'.format(self.name, self.year, self.cost)

    def get_age(self):
        """Return the age of guitar"""
        return 2022-self.year

    def is_vintage(self):
        """Check whether guitar is considered a vintage"""
        return self.get_age() >= 50



