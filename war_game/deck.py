from const import suits, ranks
from card import Card


class Deck:
    def __init__(self):
        self.all_Cards = []
        # prepare deck of all cards
        for suit in suits:
            for rank in ranks:
                self.all_Cards.append(Card(suit, rank))
    
    def shuffle(self):
        from random import shuffle
        shuffle(self.all_Cards)

    def length(self):
        return len(self.all_Cards)
    
    # def get_one(self):
    #     card = self.all_Cards[0]
    #     self.all_Cards.pop(0)
    #     return card
    
    def get_cards(self):
        return self.all_Cards.copy()
    
    def __str__(self):
        return f"Currently Deck has {self.length()} cards!!!"
    
# deck  =Deck()
# print(deck)
# deck.shuffle()
# print(deck.length())
# print(deck.get_one())
# print(deck.length())
