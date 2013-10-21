from roulette.bin import Bin
import random


class Wheel(object):

    """ Wheel contains the 38 individual bins on a Roulette wheel,
     plus a random number generator. It can select a Bin at random,
      simulating a spin of the Roulette wheel. """

    def __init__(self, rng=None):
        """ constructor """
        self.bins = list(Bin() for i in range(38))
        # for making it unit-testable, this class should be able to accept a
        # non-uniform random number generator
        self.rng = rng if rng is not None else random.Random()
        self.all_outcomes = []
            # acting as a factory class to hold all outcomes

    def addOutcome(self, number, outcome):
        assert number >= 0
        assert number <= 37  # since we have 38 bins
        self.bins[number].add(outcome)
        self.all_outcomes.append(outcome)

    def next(self):
        """Generates a random number between 0 and 37, and returns the randomly selected Bin."""
        random_number = self.rng.choice(range(0, 38))
        returned_bin = self.get(random_number)
        return returned_bin

    def get(self, bin):
        """ Returns the given Bin from the internal collection."""
        return self.bins[bin]

    def getOutcome(self, name):
        for oc in self.all_outcomes:
            if name == oc.name:
                return oc
# return set( [ oc for oc in self.all_outcomes if name.lower() in
# oc.name.lower() ] ) #why are we returning a set?


class NonRandom(random.Random):

    """ create a non random generator to aid us in testing"""

    def __init__(self):
        self.value = 0

    def setSeed(self, value):
        """Saves this value as the next value to return."""
        self.value = value

    def choice(self, sequence):
        """Use the given seed value as an index and return the requested item from the sequence."""
        return sequence[self.value]
