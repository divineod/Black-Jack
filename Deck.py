from Card import Card
import random


class Deck(object):
    def __init__(self):
        self.cards = []
        self.hand = []
        self.build()

    def build(self):
        joker = 10
        queen = 10
        king = 10
        arr = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, joker, queen, king]
        for s in ["SPADES", "CLUBS", "DIAMONDS", "HEARTS"]:
            for v in arr:
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def hit(self):
            if len(self.cards) > 1:
                x = self.cards.pop()
                return x





