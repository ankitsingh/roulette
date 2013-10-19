from nose import *
from roulette.bin import Bin
from roulette.outcome import Outcome
from roulette.wheel import NonRandom, Wheel
from roulette.bet import Bet
from roulette.binbuilder import BinBuilder
from roulette.game import Game, Person57
from roulette.table import Table, InvalidBet


def test_cycle():
  """ Test to check if the player is winning and losing appropriately"""
  rng = NonRandom()
  wheel = Wheel(rng)
  wheel.rng.setSeed(2)
  binbuilder = BinBuilder(wheel)
  binbuilder.evenMoneyBets()
  
  table_limit = 1000
  table = Table(table_limit)
  
  outcome = wheel.getOutcome("black")
  
  player = Person57(outcome, table)
  try:
    player.placeBets(100)
  except InvalidBet:
    print "invalid bet"
  else:
    assert player.outcome == outcome
    assert table.totalBetsPlaced == 100
    assert len(table.bets) == 1

    game = Game(wheel, table)
    win = game.cycle(player)
    assert win == 200

    wheel.rng.setSeed(1)
    win = game.cycle(player)
    assert win == -100
