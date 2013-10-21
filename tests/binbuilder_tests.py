from nose import *
from roulette.bin import Bin
from roulette.outcome import Outcome
from roulette.wheel import NonRandom, Wheel
from roulette.binbuilder import BinBuilder


def test_straightBets():
    rng = NonRandom()
    wheel = Wheel(rng)
    binbuilder = BinBuilder(wheel)
    binbuilder.straightBets()

    for i in range(0, 38):
        wheel.rng.setSeed(i)
        returned_bin = wheel.next()
        assert len(returned_bin.outcomes) == 1


def test_splitBets():
    rng = NonRandom()
    wheel = Wheel(rng)
    binbuilder = BinBuilder(wheel)
    binbuilder.splitBets()
    two_splits = [1, 3, 34, 36]

    for i in two_splits:
        wheel.rng.setSeed(i)
        returned_bin = wheel.next()
        assert len(returned_bin.outcomes) == 2

    for i in range(4, 34):
        wheel.rng.setSeed(i)
        returned_bin = wheel.next()
        if (i - 2) % 3 == 0:
            assert len(returned_bin.outcomes) == 4
        else:
            assert len(returned_bin.outcomes) == 3

        remaining = [2, 35]
        for i in remaining:
            wheel.rng.setSeed(i)
            returned_bin = wheel.next()
            assert len(returned_bin.outcomes) == 3


def test_streetBets():
    rng = NonRandom()
    wheel = Wheel(rng)
    binbuilder = BinBuilder(wheel)
    binbuilder.streetBets()
    for i in range(1, 37):
        wheel.rng.setSeed(i)
        returned_bin = wheel.next()
        assert len(returned_bin.outcomes) == 1


def test_cornerBets():
    rng = NonRandom()
    wheel = Wheel(rng)
    binbuilder = BinBuilder(wheel)
    binbuilder.cornerBets()
    one_corner = [1, 3, 34, 36]

    for i in one_corner:
        wheel.rng.setSeed(i)
        returned_bin = wheel.next()
        assert len(returned_bin.outcomes) == 1

    for i in range(4, 34):
        wheel.rng.setSeed(i)
        returned_bin = wheel.next()
        if (i - 2) % 3 == 0:
            assert len(returned_bin.outcomes) == 4
        else:
            assert len(returned_bin.outcomes) == 2

        remaining = [2, 35]
        for i in remaining:
            wheel.rng.setSeed(i)
            returned_bin = wheel.next()
            assert len(returned_bin.outcomes) == 2
