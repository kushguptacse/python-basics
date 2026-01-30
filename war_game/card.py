from const import scores


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.score = scores[rank.lower()]

    def __str__(self):
        return f"{self.rank.capitalize()} of {self.suit.capitalize()}"
    
    def get_score(self):
        return self.score


# print(Card('diamonds','three'))
