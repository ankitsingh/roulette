from roulette.table import Table, InvalidBet
from roulette.player import Player
from roulette.wheel import Wheel
from roulette.binbuilder import BinBuilder
from roulette.game import Game


"""
> how many players?
> player[i] name
> while no of players>0
  >player[i] bet
  >roll wheel
  >display amount of each player

"""

if __name__ == "__main__":

    table_limit = int(raw_input("> Table limit? "))
    while (table_limit < 0):
        print "table limit should be greater than 0"
        table_limit = int(raw_input("> Table limit? "))
    table = Table(table_limit)

    wheel = Wheel()
    bin_builder = BinBuilder(wheel)
    bin_builder.buildBins()
    game = Game(wheel, table)

    num_of_players = raw_input(">How many players (currently just one)?")
    while num_of_players.isdigit() is False:
        print "number of players should be an integer value"
        num_of_players = raw_input(">How many players?")

    players = []
    player_stakes = 1000
    for i in xrange(int(num_of_players)):
        player_name = raw_input("> Name for player%d: " % (i+1))
        player = Player(table, player_name, player_stakes)
        players.append(player)

    bets = []
    while num_of_players > 0:
        for p in num_of_players:
            outcome_name  = raw_input("> bet for %s: " % (players[i].name))
            amount = int(raw_input("> amount: "))
            while amount > players[i].stakes:
                print "not enough money left. Remaining stakes: %d" % players[i].stakes
                amount = raw_input("> amount: ")
            outcome = wheel.getOutcome(outcome_name)
            try:
                players[i].placeBets(amount, outcome)
            except InvalidBet:
                print "invalid bet"

        game.cycle(players[0])
        print "Remaining stakes: %d" % players[i].stakes
        more = raw_input("> want to play more(y/n)?:")
        if "y" in more:
            pass
        else:
            num_of_players = 0
    print "Thank you! have a good day!"



