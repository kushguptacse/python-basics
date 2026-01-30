from deck import Deck
from player import Player
from const import war_resolution_count


class Game:
    def start_game(self):
        self.distribute_card()
        self.play_game()

    def check_winner(self):
        if self.playerA.length() == 0:
            print(f"player {self.playerB.name} won the game")
        elif self.playerB.length() == 0:
            print(f"player {self.playerA.name} won the game")
        else:
            return False
        return True

    def play_game(self):
        extra_cards = []
        while True:
            if self.check_winner():
                return
            print("Start round —", self.playerA, self.playerB)
            card_a = self.playerA.remove_one()
            card_b = self.playerB.remove_one()
            extra_cards.extend([card_a, card_b])
            print("After draw —", self.playerA, self.playerB)
            if card_a.score < card_b.score:
                self.playerB.add_cards(extra_cards)
                extra_cards=[]
            elif card_a.score > card_b.score:
                self.playerA.add_cards(extra_cards)
                extra_cards=[]
            else:
                for i in range(0, war_resolution_count):
                    card_a = self.playerA.remove_one()
                    card_b = self.playerB.remove_one()
                    if card_a is None or card_b is None:
                        break
                    extra_cards.append(card_a)
                    extra_cards.append(card_b)
                        
            # winner adds cards...
            print("After round —", self.playerA, self.playerB)

    def distribute_card(self):
        self.deck.shuffle()
        self.playerA.add_cards(self.deck.get_cards()[0 : self.deck.length() // 2])
        self.playerB.add_cards(self.deck.get_cards()[self.deck.length() // 2 :])
        print(self.playerA)   # initial total A
        print(self.playerB)   # initial total B

    def __init__(self):
        self.deck = Deck()
        self.playerA = Player("A")
        self.playerB = Player("B")

    def __str__(self):
        return f"{self.playerA}:{self.playerB}:{self.deck}"


if __name__ == "__main__":
    Game().start_game()
