from Deck import Deck


class Dealer(object):
    hand = []

    def __init__(self, bankroll=0):
        self.hand = []
        self.bankroll = bankroll

    def draw(self):
        self.hand.append(deck.hit())
        return self

    def show(self):
        for c in self.hand:
            c.show()

    def turn(self):
        for c in self.hand:
            if c == self.hand[0]:
                c.show()
            else:
                pass


deck = Deck()

#deal.draw(deck)
#deal.show()

