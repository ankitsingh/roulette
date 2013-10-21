from nose import *
from roulette.bin import Bin
from roulette.outcome import Outcome
from roulette.wheel import NonRandom, Wheel
from roulette.bet import Bet
from roulette.binbuilder import BinBuilder
import random


def test_win_loseAmount():

    rng = NonRandom()
    wheel = Wheel(rng)
    binbuilder = BinBuilder(wheel)
    binbuilder.straightBets()
    outcome = wheel.getOutcome("1")
    amount = 500
    bet = Bet(amount, outcome)

    for i in range(0, 38):
        wheel.rng.setSeed(i)
        returned_bin = wheel.next()
        returned_outcomes = returned_bin.outcomes
        if outcome in returned_outcomes:
            assert bet.winAmount() == 500 + 500 * outcome.odds
        else:
            assert bet.loseAmount() == 500
