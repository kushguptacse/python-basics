class Player:
    def __init__(self, name):
        self.all_cards = []
        self.name = name

    def remove_one(self):
        if self.length()==0:
            return None
        card  = self.all_cards.pop(0)
        print(f"{self.name}: card withdrawn: {card}")
        return card

    def add_cards(self, cards):
        for card in cards:
            if card is None:
                continue
            self.all_cards.append(card)

    def length(self):
        return len(self.all_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards!!"
    
# player = Player("A")
# from deck import Deck
# card = Deck().get_one()
# player.add_cards([card])
# print(player)
