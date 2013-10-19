from roulette.bin import Bin
from roulette.outcome import Outcome
from roulette.wheel import NonRandom, Wheel
from roulette.bet import Bet
from roulette.binbuilder import BinBuilder


class Game(object):
  """Game manages the sequence of actions that 
  defines the game of Roulette. This includes 
  notifying the Player to place bets, spinning 
  the Wheel and resolving the Bets actually 
  present on the Table."""
  def __init__(self, wheel, table):
    self.wheel = wheel
    self.table = table
    self.player = None
    
  def cycle(self, player):
    self.player = player
    selected_bin = self.wheel.next()
    outcomes = selected_bin.outcomes
    i = iter(self.table)
    while 1:
      try:
        bet = i.next()
      except StopIteration:
        break
      else:
        outcome = bet.outcome
    if outcome in outcomes:
      return player.win(bet)
    else:
      return player.lose(bet)
  
  
class Person57(object):
  """dummy person who place bets only on black"""
  
  def __init__(self, outcome, table):
    self.outcome = outcome
    self.table = table
    
  def placeBets(self, amount):
    bet = Bet(amount, self.outcome)
    self.table.placeBet(bet)
    
  def win(self, bet):
    amount_won = bet.winAmount()
    return amount_won
    
  def lose(self, bet):
    amount_lost = bet.loseAmount()
    return abs(amount_lost) * -1
    
    
    
