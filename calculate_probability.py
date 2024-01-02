from compare import get_max_score
from compare import pokerStr2pokerID
from compare import pokerID2pokerStr
from compare import poker_type2str
from pokerCard import PokerDeck
from compare import CardForce
from compare import whoIsWinner
import sys
def calu_prob(your_cards,player_num,calcu_num=int(1e5)):
    win_num=0
    splitPot_num=0
    asWin_num=0
    progress=0
    for i in range(1,calcu_num+1):
        

        if i%(calcu_num//100)==0:
            progress+=1
            print("progress:第",i,"次，进度：",progress,"%,win_probability={}%,splitPot_probability={}%,asWin_probability={}%".format(win_num/i*100,splitPot_num/i*100,asWin_num/i*100))

        # 将标准输出保存到临时变量
        original_stdout = sys.stdout
        # 将标准输出重定向到一个空文件（或者可以指定一个其他目标文件）
        sys.stdout = open('nul', 'w')
        # 调用函数，此时所有的打印输出会被重定向到空文件
        winnerid=play1time_SP(your_cards,player_num)
        # 还原标准输出!!!!!
        sys.stdout = original_stdout
        
        if winnerid==[0]:
            win_num+=1
            asWin_num+=1
        elif 0 in winnerid:
            splitPot_num+=1
            asWin_num+=1/len(winnerid)
    
    
    win_probability=win_num/calcu_num
    splitPot_probability=splitPot_num/calcu_num
    asWin_probability=asWin_num/calcu_num
    print("win_probability={}%,splitPot_probability={}%,asWin_probability={}".format(win_probability*100,splitPot_probability*100,asWin_probability*100))
    return win_num/calcu_num,splitPot_num/calcu_num

def play1time_SP(your_cards,player_num,hand1_card=["random"],board_cards_type=["random"]):#,calcu_num)
    print("*************creat deck************")
    deck = PokerDeck()
    deck.print_deck()
    print("**deal**")
    hand=["empty"] * (player_num)

    print("FFFFFFFFFFFFFFFFFFFFFFF:your_cardsFFFFFFFFFFFFFFFFFFFFF:  1  ",your_cards)
    #print("FFFFFFFFFFFFFFFFFFFFFFF:your_cardsFFFFFFFFFFFFFFFFFFFFF:  2  ",deck.deal_specific_cards(your_cards))
    deck.print_deck()
    hand[0] = deck.deal_specific_cards(your_cards)
    print("FFFFFFFFFFFFFFFFFFFFFFF:your_cardsFFFFFFFFFFFFFFFFFFFFF:  3  ",hand[0])
    print("your hand 0:",hand[0])
    for i in range(1, player_num):#前开后闭
        hand[i] = deck.deal_cards(2)
        print("hand ",i,":", hand[i])
    if hand1_card!=["random"]:
        deck.cards.append(hand[1])
        hand[1]=deck.deal_specific_cards(hand1_card)
    
    
    board_cards = deck.deal_cards(5)
    if board_cards_type!=["random"]:#fixme specific_card may in hand
        deck.cards.append(board_cards)
        board_cards=deck.deal_specific_cards(board_cards_type)
    print("Dealt board_cards:", board_cards)
    deck.print_deck

    count = 0
    card_force=()
    for hand_cards_str in hand:
        seven_cards=(pokerStr2pokerID(board_cards+hand_cards_str))
        [card_type, card_value]=get_max_score(seven_cards)
        card_force=card_force+(CardForce(count,card_type, card_value),)
        print("get_hand",count,"_score:",card_type, card_value)
        print("get_hand",count,"_str:",poker_type2str(card_type, card_value))
        count += 1
    WinnerID=whoIsWinner(card_force)
    for id in WinnerID:
        card_force[id].show()
    return WinnerID

