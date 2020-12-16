from Deck import Deck
from Dealer import Dealer
from Card import Card

deal = Dealer()
deck = Deck()
deck.shuffle()

class Player(object):
    hand = []
    sp_hand = []

    def __init__(self, name, bankroll=0, spbankroll=0):
        self.name = name
        self.bankroll = bankroll
        self.sp_bankroll = spbankroll
        self.hand = []
        self.sp_hand = []
        self.ace = False

    def draw(self):
        self.hand.append(deck.hit())
        return self

    def show(self):
        for c in self.hand:
            c.show()

    def split(self):
        if self.hand[1] == self.hand[0]:
            self.sp_hand.append(self.hand.pop())
            self.bankroll /= 2
            self.sp_bankroll = self.bankroll
            self.hand.append(deck.hit())
            self.sp_hand.append(deck.hit())

    def stand(self):

        pass

    def doubledown(self):
        self.bankroll *= 2
        self.hand.append(deck.hit())
        return self

    def surrender(self):
        self.bankroll /= 2
        deal.bankroll += self.bankroll

    def check(self):
        card = Card()

        for card in self.hand:
            if self.hand[card.grab_value()] == 'A':
                self.ace = True
                self.hand[card.grab_value()] = 11
            self.hand[card.grab_value()] += self.hand[card.grab_value()]
        if self.hand[card.grab_value()] > 21 and self.ace is True:
            self.hand[card.grab_value()] -= 10
        elif self.hand[card.grabvalue()] > 21:
            print("Sorry, you bust!")
        elif self.hand[card.grab_value()] == 21:
            print("Blackjack!!!")
        else:
            pass

    def calc_val(self):
        card = 0
        if self.ace == True and self.hand[card.grab_value()] < 12:
            return self.hand[card.grab_value()] + 10
        else:
            return self.hand[card.grab_value()]




