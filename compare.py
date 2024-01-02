#花色有4种，刚好可用最后2位表示4种花色。
def get_card_suit_id(card_id):
    return card_id & 3
#ID最后2位是花色，那么右移2位，剩下的信息就是牌的数字了。
def get_card_num_id(card_id):
    return card_id >> 2
# 组合算法不用自己实现，各个编程语言都有库。

# 这就是根据7张牌，计算max_type和max_value的逻辑。其中get_type()和get_value()是我们后面需要实现的。
from itertools import combinations
class CardForce :
    def __init__(self, card_id, card_type, card_value):
        self.id = card_id
        self.type = card_type
        self.value = card_value
    def show(self):
        print("*********************")
        print("hand",self.id,"is the winner!!!\n!!!!",poker_type2str(self.type, self.value))
        print("*********************")
def whoIsWinner(card_force_list):
    max_type = None
    max_value = None
    winners = []

    for card_force in card_force_list:
        if max_type is None or card_force.type > max_type:
            max_type = card_force.type
            max_value = card_force.value
            winners = [card_force.id]
        elif card_force.type == max_type:
            if max_value is None or card_force.value > max_value:
                max_value = card_force.value
                winners = [card_force.id]
            elif card_force.value == max_value:
                winners.append(card_force.id)

    return winners

def get_max_score(seven_cards):
    max_type = -1
    res = []
    for cards in combinations(seven_cards, 5):
        t, v = get_type(cards)
        if t > max_type:
            max_type = t
            res = [(t, v, cards)]
        elif t == max_type:
            res.append((t, v, cards))
    max_value = get_value(*res[0])
    for r in res[1:]:
        value = get_value(*r)
        if value > max_value:
            max_value = value
    return max_type, max_value
# 这里介绍一个小小的优化点：我们遍历时，并不会计算所有的5张牌组合的max_type和max_value，因为可以先把max_type算出来，得到最大的type后，只需要计算最大type的max_value，省了一些没有必要的计算。

# 当然由于遇到顺子时，可以很快得到max_value，所以会在get_type时就算出来



# card_type 8 同花顺：比最大的牌即可。card_value就是最大牌的数字大小
# card_type 7 四条：card_value需要先比四条的数字，再比单牌的数字。所以card_value是个二维的结构：（四条的数字, 单牌的数字）
# card_type 6 葫芦：card_value是个二维的结构：（三条的数字, 一对的数字）
# card_type 5 同花：card_value是个五维的结构，从大到小排列的5个牌的数字
# card_type 4 顺子：card_value就是最大牌的数字大小
# card_type 3 三条：card_value是个三维的结构：（三条的数字, 较大单牌的数字, 较小单牌的数字）
# card_type 2 两对：card_value是个三维的结构：（较大对子的数字, 较小对子的数字, 单牌的数字）
# card_type 1 一对：card_value是个三维的结构：（对子的数字, 最大单牌的数字, 第二大单牌的数字, 第三大单牌的数字）
# card_type 0 高牌：card_value是个五维的结构，从大到小排列的5个牌的数字
def get_type(five_cards):
    straight, straight_value = is_straight(five_cards)
    flush = is_flush(five_cards)
    if flush and straight:
        return 8, straight_value
    if flush:
        return 5, None  # sorted([get_card_num_id(c) for c in five_cards], reverse=True)
    if straight:
        return 4, straight_value
    nums = [0] * 13
    for card in five_cards:
        nums[get_card_num_id(card)] += 1#哈希计数
    max_freq = max(nums)
    if max_freq == 1:
        return 0, None  # sorted([get_card_num_id(c) for c in five_cards], reverse=True)
    if max_freq == 4:
        return 7, None  # [nums.index(4), nums.index(1)]
    if max_freq == 3:
        if 2 in nums:
            return 6, None  # [nums.index(3), nums.index(2)]
        return 3, None
    # max_freq == 2
    if nums.count(2) == 1:
        return 1, None
    return 2, None

def get_value(t, v, five_cards):
    if v is not None:
        return v
    if t in (0, 5):
        return sorted((get_card_num_id(c) for c in five_cards), reverse=True)
    nums = [0] * 13
    for card in five_cards:
        nums[get_card_num_id(card)] += 1
    return sorted(list(set(get_card_num_id(c) for c in five_cards)), reverse=True, key=lambda x: (nums[x] << 5) + x)


def is_flush(five_cards):
    s = get_card_suit_id(five_cards[0])
    for c in five_cards[1:]:
        if s != get_card_suit_id(c):
            return False
    return True

def is_straight(five_cards):
    nums = sorted([get_card_num_id(c) for c in five_cards])
    if nums == [0, 1, 2, 3, 12]:#A 2 3 4 5
        return True, 3
    n4 = nums[4]
    for i, n in enumerate(nums[:4]):
        if n4 - n != 4 - i:
            return False, 0
    return True, n4

def pokerStr2pokerID(poker):
    # 建立花色和点数的映射关系
    suit_map = {'s': 0, 'h': 1, 'd': 2, 'c': 3}
    rank_map = {'A': 12, '2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T':8,'10': 8, 'J': 9, 'Q': 10, 'K': 11}

    # 新建空列表用于存储扑克ID
    pokerIDList = []

    # 检查输入类型
    if isinstance(poker, str):
        pokerList = [poker]
    elif isinstance(poker, list):
        pokerList = poker
    else:
        raise TypeError("Invalid poker type. Expected str or list, got {}".format(type(poker)))

    # 迭代扑克字符串列表
    for pokerStr in pokerList:
        # 解析扑克字符串
        suit = pokerStr[-1]  # 获取最后一个字符表示的花色
        rank = pokerStr[:-1]  # 获取除了最后一个字符以外的字符串表示的点数

        # 判断输入格式是否符合要求
        if suit not in suit_map:
            raise ValueError("Invalid pokerStr_suit: {}".format(suit))
        if rank not in rank_map:
            raise ValueError("Invalid pokerStr_rank: {}".format(rank))
        
        # 计算扑克ID，并添加到列表中
        pokerID = suit_map[suit] + (rank_map[rank] << 2)
        pokerIDList.append(pokerID)

    return pokerIDList


def pokerID2pokerStr(poker):
    # 建立花色和点数的映射关系
    suit_map = {0: 's', 1: 'h', 2: 'd', 3: 'c'}
    rank_map = {12: 'A', 0: '2', 1: '3', 2: '4', 3: '5', 4: '6', 5: '7', 6: '8', 7: '9', 8: 'T', 9: 'J', 10: 'Q', 11: 'K'}
    
    # 新建空列表用于存储扑克字符串
    pokerStrList = []

    # 检查输入类型
    if isinstance(poker, int):
        pokerList = [poker]
    elif isinstance(poker, list):
        pokerList = poker
    else:
        raise TypeError("Invalid poker type. Expected int or list, got {}".format(type(poker)))

    # 迭代扑克ID列表
    for pokerID in pokerList:
        # 验证扑克ID是否在有效范围内
        if not 0 <= pokerID <= 51:
            raise ValueError("Invalid poker ID. Expected a number between 0 and 51, got {}".format(pokerID))

        # 解析扑克ID
        suit = suit_map[pokerID & 0b11]
        rank = rank_map[pokerID >> 2]

        # 拼接扑克字符串，并添加到列表中
        pokerStr = rank + suit
        pokerStrList.append(pokerStr)

    return pokerStrList

def poker_type2str(card_type, card_value):
    rank_map = {12: 'A', 0: '2', 1: '3', 2: '4', 3: '5', 4: '6', 5: '7', 6: '8', 7: '9', 8: 'T', 9: 'J', 10: 'Q', 11: 'K'}
    if card_type == 8:
        return "Straight flush!"
    elif card_type == 7:
        four_of_a_kind = rank_map[card_value[0]]
        single_card = rank_map[card_value[1]]
        return "Four of a kind: four {} and one {}".format(four_of_a_kind, single_card)
    elif card_type == 6:
        three_of_a_kind = rank_map[card_value[0]]
        pair = rank_map[card_value[1]]
        return "Full house: three {} and two {}".format(three_of_a_kind, pair)
    elif card_type == 5:
        flush_cards = [rank_map[card] for card in card_value]
        return "Flush: {}".format(" ".join(flush_cards))
    elif card_type == 4:
        straight_value = rank_map[card_value]
        return "Straight: {}".format(straight_value)
    elif card_type == 3:
        three_of_a_kind = rank_map[card_value[0]]
        high_card1 = rank_map[card_value[1]]
        high_card2 = rank_map[card_value[2]]
        return "Three of a kind: three {} with high cards {} and {}".format(three_of_a_kind, high_card1, high_card2)
    elif card_type == 2:
        high_pair =     rank_map[card_value[0]]
        low_pair =      rank_map[card_value[1]]
        single_card =   rank_map[card_value[2]]
        return "Two pair: pair {} and {} with a single card {}".format(high_pair, low_pair, single_card)
    elif card_type == 1:
        pair = rank_map[card_value[0]]
        high_card1 = rank_map[card_value[0]]
        high_card2 = rank_map[card_value[1]]
        high_card3 = rank_map[card_value[2]]
        return "One pair: pair {} with high cards {}, {}, and {}".format(pair, high_card1, high_card2, high_card3)
    elif card_type == 0:
        high_cards = [rank_map[card] for card in card_value]
        return "High card: {}".format(" ".join(high_cards))
    else:
        return "Invalid card type"

card_type = 5
card_value = [10, 8, 2, 1, 0]
result = poker_type2str(card_type, card_value)
print(result)
