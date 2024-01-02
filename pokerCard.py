import random

class PokerDeck:
    def __init__(self, full_deck=True):
        if full_deck:
            self.cards = [
                "As", "Ah", "Ad", "Ac",
                "Ks", "Kh", "Kd", "Kc",
                "Qs", "Qh", "Qd", "Qc",
                "Js", "Jh", "Jd", "Jc",
                "Ts", "Th", "Td", "Tc",
                "9s", "9h", "9d", "9c",
                "8s", "8h", "8d", "8c",
                "7s", "7h", "7d", "7c",
                "6s", "6h", "6d", "6c",
                "5s", "5h", "5d", "5c",
                "4s", "4h", "4d", "4c",
                "3s", "3h", "3d", "3c",
                "2s", "2h", "2d", "2c"
            ]
        else:
            self.cards = [
                "Ts", "Th", "Td", "Tc",
                "Js", "Jh", "Jd", "Jc",
                "Qs", "Qh", "Qd", "Qc",
                "Ks", "Kh", "Kd", "Kc",
                "As", "Ah", "Ad", "Ac"
            ]

    def print_deck(self):
        print("Poker Deck>>>",end="\t")
        print(" ".join(self.cards))

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def deal_cards(self, n):
        if n > len(self.cards):
            print("Cannot deal {} cards. Only {} cards left in the deck.".format(n, len(self.cards)))
            return []

        dealt_cards = random.sample(self.cards, n)
        for card in dealt_cards:
            self.cards.remove(card)
        return dealt_cards

    def deal_specific_cards(self, specific_cards):
        dealt_cards = []
        for card in specific_cards:
            if card in self.cards:
                self.cards.remove(card)
                dealt_cards.append(card)
            else:
                print("!!!Error specific_card not in deck.cards!!!!")
                print("card:",card)
        return dealt_cards
