from roulette.bin import Bin
from roulette.outcome import Outcome
from roulette.wheel import NonRandom, Wheel

class BinBuilder(object):
  """ a class to build all the bins
      with their outcomes"""

  def __init__(self, wheel):
    self.wheel = wheel

  def buildBins(self):
    """ building all bins with their respective outcomes"""
    self.straightBets()
    self.splitBets()
    self.streetBets()
    self.cornerBets()
    self.lineBets()
    self.dozenBets()
    self.columnBets()
    self.evenMoneyBets()

  def straightBets(self):
    """A straight bet is a bet on a single number.
    There are 38 possible bets, and they pay odds of 35 to 1.
    Each bin on the wheel pays one of the straight bets."""

    for n in range(1,37):
      outcome = Outcome(str(n), 35)
      self.wheel.addOutcome(n, outcome)

    outcome = Outcome("0", 35)
    self.wheel.addOutcome(0, outcome)
    outcome = Outcome("00", 35)
    self.wheel.addOutcome(37, outcome)

  def splitBets(self):
    """A split bet is a bet on an adjacent pair of numbers.
    It pays 17:1. Any of two bins can make a split
    bet a winner."""

    #left-right pairs
    for r in range(0,12):
      n = 3*r + 1
      outcome = Outcome("%d-%d" % (n,n+1), 17)
      self.wheel.addOutcome(n, outcome)
      self.wheel.addOutcome(n+1, outcome)

      n = 3*r + 2
      outcome = Outcome("%d-%d" % (n,n+1), 17)
      self.wheel.addOutcome(n, outcome)
      self.wheel.addOutcome(n+1, outcome)

    #up-down pairs
    for n in range(1,34):
      outcome = Outcome("%d-%d" % (n,n+3), 17)
      self.wheel.addOutcome(n, outcome)
      self.wheel.addOutcome(n+3, outcome)

  def streetBets(self):
    """A street bet includes three numbers on the same row"""

    for r in range(0,12):
      n = 3*r + 1
      outcome = Outcome("%d-%d-%d" % (n, n+1, n+2), 11)
      self.wheel.addOutcome(n, outcome)
      self.wheel.addOutcome(n+1, outcome)
      self.wheel.addOutcome(n+2, outcome)


  def cornerBets(self):
    """A bet on a square of four corners"""

    for r in range(0,11):
      n= 3*r + 1
      outcome = Outcome("%d-%d-%d-%d" % (n, n+1, n+3, n+4), 8)
      self.wheel.addOutcome(n, outcome)
      self.wheel.addOutcome(n+1, outcome)
      self.wheel.addOutcome(n+3, outcome)
      self.wheel.addOutcome(n+4, outcome)

      n= 3*r + 2
      outcome = Outcome("%d-%d-%d-%d" % (n, n+1, n+3, n+4), 8)
      self.wheel.addOutcome(n, outcome)
      self.wheel.addOutcome(n+1, outcome)
      self.wheel.addOutcome(n+3, outcome)
      self.wheel.addOutcome(n+4, outcome)


  def lineBets(self):
    """A bet on six consecutive numbers"""

    for r in range(0,10):
      n = 3*r + 1
      outcome = Outcome("%d-%d-%d-%d-%d-%d" % (n, n+1, n+2, n+3, n+4, n+5), 5)
      self.wheel.addOutcome(n, outcome)
      self.wheel.addOutcome(n+1, outcome)
      self.wheel.addOutcome(n+2, outcome)
      self.wheel.addOutcome(n+3, outcome)
      self.wheel.addOutcome(n+4, outcome)
      self.wheel.addOutcome(n+5, outcome)

  def dozenBets(self):
    """A bet on the ranges 0-12, 12-24, 24-36"""
    for d in range(0,3):
      outcome = Outcome("dozen %d" % (d+1), 2)
      for m in range(0,12):
        self.wheel.addOutcome(12*d + m + 1, outcome)

  def columnBets(self):
    """A bet on a column of the roulette wheeel"""
    for c in range(0,3):
      outcome = Outcome("column %d" % (c+1), 2)
      for r in range(0,12):
          self.wheel.addOutcome(3*r + c + 1, outcome)


  def evenMoneyBets(self):
    """A bet that covers half of the outcomes"""
    redOutcome = Outcome("red", 1)
    blackOutcome = Outcome("black", 1)
    evenOutcome = Outcome("even", 1)
    oddOutcome = Outcome("odd", 1)
    highOutcome = Outcome("high", 1)
    lowOutcome = Outcome("low", 1)
    reds = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

    for n in range(1,37):
      if (n >= 1 and n < 19):
        self.wheel.addOutcome(n, lowOutcome)
      if (n >= 19 and n < 37):
        self.wheel.addOutcome(n, highOutcome)
      if ((n % 2) == 0):
        self.wheel.addOutcome(n, evenOutcome)
      if ((n % 2) != 0):
        self.wheel.addOutcome(n, oddOutcome)
      if (n in reds):
        self.wheel.addOutcome(n, redOutcome)
      if (n not in reds):
        self.wheel.addOutcome(n, blackOutcome)




