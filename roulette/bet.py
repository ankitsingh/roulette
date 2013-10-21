from roulette.outcome import Outcome


class Bet():

    """A Bet is an amount that the player has wagered
    on a specific Outcome. This class has the responsibility
    for maintaining the association between an amount,
    an Outcome, and a specific Player"""

    def __init__(self, amount, outcome):
        self.amountBet = amount
        self.outcome = outcome

    def winAmount(self):
        amount_won = self.amountBet + self.outcome.winAmount(self.amountBet)
        return amount_won

    def loseAmount(self):
        return self.amountBet

    def __str__(self):
        return "%d on %s" % (self.amountBet, self.outcome)
