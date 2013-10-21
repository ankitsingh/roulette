from nose import *
from roulette.bin import Bin
from roulette.outcome import Outcome


def test_add():
    outcome1 = Outcome("red", 1)
    outcome2 = Outcome("1", 1)
    outcome3 = Outcome("Odd", 5)
    new_outcome = Outcome("five bet", 50)

    bin = Bin(outcome1, outcome2, outcome3)
    assert outcome1 in bin.outcomes
    assert outcome2 in bin.outcomes
    assert outcome3 in bin.outcomes

    bin.add(new_outcome)
    assert new_outcome in bin.outcomes
