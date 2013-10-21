
class Bin(object):

    """bin in a roulette. Each bin class with have
      a collection of outcomes that win if the ball
      falls over that bin."""

    def __init__(self, *outcomes):
        """initialization with the outcomes for a bin"""
        self.outcomes = set(outcomes)

    def add(self, outcome):
        """ used to add a new outcome to a bin """
        self.outcomes |= set([outcome])

    def __str__(self):
        """printing the contents of the bin neatly """
        return ', '.join(map(str, self.outcomes))
