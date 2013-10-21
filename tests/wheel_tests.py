from nose import *
from roulette.bin import Bin
from roulette.outcome import Outcome
from roulette.wheel import NonRandom, Wheel
import random


def test_init():
    """ checking if out Nonrandom class is working properly"""
    rng = NonRandom()
    seed = 5
    rng.setSeed(seed)
    wheel = Wheel(rng)
    assert len(wheel.bins) == 38
    assert wheel.rng.value == seed
    assert wheel.rng.choice(range(0, 38)) == range(
        0, 38)[wheel.rng.value]  # == seed


def test_bin_addition():
    """ testing if we can add/get outcomes to corresponding bins on the wheel"""
    outcome1 = Outcome("red", 1)
    outcome2 = Outcome("black", 1)
    outcome3 = Outcome("low", 5)
    outcome4 = Outcome("high", 5)

    rng = NonRandom()
    wheel = Wheel(rng)

    wheel.addOutcome(1, outcome1)
    wheel.addOutcome(1, outcome3)
    wheel.addOutcome(31, outcome2)
    wheel.addOutcome(31, outcome4)

    # since we added only two outcomes for each of the two bins,
    # the number of outcomes for both bins should be 2 and 0 for all others
    wheel.rng.setSeed(1)
    returned_bin = wheel.next()
    outcomes = returned_bin.outcomes
    print outcomes
    assert len(outcomes) == 2
    assert outcome1 in returned_bin.outcomes
    assert outcome3 in returned_bin.outcomes

    wheel.rng.setSeed(31)
    returned_bin = wheel.next()
    assert outcome3, outcome2 in returned_bin.outcomes
    assert outcome3, outcome4 in returned_bin.outcomes

    for i in range(0, 38):
        if i not in [1, 31]:
            wheel.rng.setSeed(i)
            returned_bin = wheel.next()
            assert len(returned_bin.outcomes) == 0


def test_mapping():
    outcome1 = Outcome("red", 1)
    outcome2 = Outcome("black", 2)
    rng = NonRandom()
    wheel = Wheel(rng)

    wheel.addOutcome(1, outcome1)
    wheel.addOutcome(2, outcome2)
    wheel.addOutcome(4, outcome2)
    out = wheel.getOutcome("red")
    assert out == outcome1

    out = wheel.getOutcome("black")
    assert out == outcome2
