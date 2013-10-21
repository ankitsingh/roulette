__author__ = 'ankit'

from roulette.bet import Bet
from roulette.wheel import Wheel


class Player(object):

    """A player class. A player will place bets on the table and
    keep count of his stakes"""

    def __init__(self, table, name, stakes):
        self.table = table
        self.name = name
        self.stakes = stakes

    def placeBets(self, amount, outcome):
        bet = Bet(amount, outcome)
        self.table.placeBet(bet)

    def win(self, bet):
        amount_won = bet.winAmount()
        self.stakes += amount_won
        return amount_won

    def lose(self, bet):
        amount_lost = bet.loseAmount()
        self.stakes -= amount_lost
        return abs(amount_lost) * -1
