from nose.tools import *
from roulette.outcome import Outcome


def test_equality():
    outcome1 = Outcome("red", 1)
    outcome2 = Outcome("red", 1)
    equality = (outcome1 == outcome2)
    assert equality is True


def test_inequality():
    outcome1 = Outcome("red", 1)
    outcome2 = Outcome("blue", 1)
    inequality = (outcome1 != outcome2)
    assert inequality is True


def test_winAmount():
    outcome = Outcome("red", 1)
    amount = 500
    winnings = outcome.winAmount(amount)
    assert_almost_equal(winnings, 500)
