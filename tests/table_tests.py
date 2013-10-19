from nose import *
from roulette.bin import Bin
from roulette.outcome import Outcome
from roulette.wheel import NonRandom, Wheel
from roulette.bet import Bet
from roulette.binbuilder import BinBuilder
from roulette.table import Table, InvalidBet


def test_placeBets():
  table_limit = 1000
  table = Table(table_limit)
  rng = NonRandom()
  wheel = Wheel(rng)
  binbuilder = BinBuilder(wheel)
  binbuilder.straightBets()
  outcome = wheel.getOutcome("1")
  amount = 500
  bet = Bet(amount, outcome)
  invalid = True
  try:
    table.placeBet(bet)
    invalid = False
  except InvalidBet:
    print "bet not valid"
    invalid = True

  assert table.bets[0] == bet
  assert len(table.bets) == 1
  assert invalid == False

  amount = 300
  bet = Bet(amount, outcome)
  invalid = True
  try:
    table.placeBet(bet)
    invalid = False
  except InvalidBet:
    print "bet not valid"
    invalid = True

  assert table.bets[1] == bet
  assert len(table.bets) == 2
  assert invalid == False

  amount = 900
  bet = Bet(amount, outcome)
  invalid = True
  try:
    table.placeBet(bet)
    invalid = False
  except InvalidBet:
    print "bet not valid"
    invalid = True

  assert len(table.bets) == 2
  assert invalid == True