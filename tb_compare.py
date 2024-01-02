from compare import get_max_score
from compare import pokerStr2pokerID
from compare import pokerID2pokerStr
from compare import poker_type2str

from pokerCard import PokerDeck
from calculate_probability import play1time_SP
seven_cards_str=["As","Qc","Th","Tc","2c","3c","4c"]

print(pokerStr2pokerID("As"))
print(pokerID2pokerStr(48))
seven_cards=(pokerStr2pokerID(seven_cards_str))
print(pokerID2pokerStr(seven_cards))
[card_type, card_value]=get_max_score(seven_cards)
print("get_max_score:",card_type, card_value)
print("poker_type2str:",poker_type2str(card_type, card_value))


print("*************creat deck************")
deck = PokerDeck()
deck.print_deck()


print("**deal**")
specific_cards = ["As", "Qc"]
hand = deck.deal_specific_cards(specific_cards)
print("Dealt specific cards:", hand)
deck.print_deck()
# deck.shuffle_deck()
# print("Shuffled deck:")
# deck.print_deck()
board_cards = deck.deal_cards(5)
print("Dealt random cards:", board_cards)

hand = deck.deal_cards(2)
print("Dealt random cards:", hand)
deck.print_deck()
if hand in deck.cards:
    print("hand in deck!!!!")
if "9c" in deck.cards:
    print("9c in deck!!!!")
print("实例化一副只有10及10以上牌面值的扑克牌")
ten_plus_deck = PokerDeck(full_deck=False)
ten_plus_deck.print_deck()
print("***************play1time_SP*******")
play1time_SP(["Qs","Tc"],5)

#play1time_SP(["As","2c"],5,["6s","7d"],["3c","4s","5h","kd","5d"])