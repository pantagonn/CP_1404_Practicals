"""
Features of each programming language
"""


class ProgrammingLanguage:

    def __init__(self, field, typing, reflection, year):
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing.lower() == 'dynamic'

    def __str__(self):
        return '{}, {} Typing, Reflection={}, First appeared in {}'.format(self.field, self.typing, self.reflection,
                                                                           self.year)
