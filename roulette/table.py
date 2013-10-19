from roulette.bin import Bin
from roulette.outcome import Outcome
from roulette.wheel import NonRandom, Wheel
from roulette.bet import Bet
from roulette.binbuilder import BinBuilder

class Table(object):
  """The Table has the responsibility to keep
  the Bets placed by the Player (the bet placed should be
  within the table limit"""
  
  def __init__(self, limit):
    self.bets = []
    self.limit = limit
    self.totalBetsPlaced = 0
    
  def isValid(self, bet):
    amountBet = bet.amountBet
    return ((self.totalBetsPlaced + amountBet) <= self.limit)
  
  
  def placeBet(self, bet):
    if (self.isValid(bet)):
      self.bets.append(bet)
      self.totalBetsPlaced += bet.amountBet
    else:
      raise InvalidBet
    
  
  def __iter__(self):
    return iter(self.bets)
  
  
class InvalidBet(Exception):
  def __init__(self, value = "InvalidBet"):
    self.value = value
    
  def __str__(self):
    return repr(self.value)