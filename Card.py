class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print("{} of {}".format(self.value, self.suit))

    def grab_value(self):
        return self.value

    def grab_suit(self):
        return self.suit









