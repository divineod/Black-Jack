from Player import Player
from Dealer import Dealer
from Card import Card
from Deck import Deck

print('Welcome to blackjack')

player1 = input("Enter name player 1: ")
player2 = input("Enter name player 2: ")
while True:
        try:
            bank1 = int(input(player1 + " ,please place your bet:"))
            bank2 = int(input(player2 + " ,please place your bet:"))
        except ValueError:
            print("Please enter integer value bets")
            continue
        else:
            pl1 = Player(player1, bank1)
            pl2 = Player(player2, bank2)
            break
deal = Dealer(bankroll=0)
deck = Deck()
deck.shuffle()
i = 0
while i <= 1:
    deal.draw()
    pl1.draw()
    pl2.draw()
    i += 1

deal.show()
pl1.show()
pl2.show()
print("The dealer's upward facing card is:")
deal.turn()
print("Player moves list:\n")
print("1. Draw\n")
print("2. Stand\n")
print("3. Double down\n")
print("4. Surrender\n")
print("5. Split\n")


def player_choice():
    play = " "
    while play not in "1 2 3 4 5".split():
        play = input(player1 + "'s turn: ")
    return int(play)


play = player_choice()
# Condition statements for the 5 plays
if play == 1:
    pl1.draw()
    pl1.show()
    pl1.check()
else:
    pass
if play == 2:
    pl1.stand()
    pl1.check()
if play == 3:
    pl1.doubledown()
if play == 4:
    pl1.surrender()
if play == 5:
    pl1.split()









