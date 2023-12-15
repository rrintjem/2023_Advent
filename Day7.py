from operator import *

#cards A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2

class Hand:
    def __init__(self, cards, bid, hand_type):
        self.cards = cards
        self.bid = bid
        self.hand_type = hand_type

    def __str__(self):
        return f"{self.cards} type: {self.hand_type} bid: {self.bid}"
    pass

def getHandType(cards):
    hasJokers = False
    if(0 in cards):
        hasJokers = True
    if not hasJokers:
        return getHandTypePart1(cards)

    distinct_cards = set(cards)
    card_count = []
    hand_type = None
    count_Jokers = 0

    for c in distinct_cards:
        if c == 0:
            count_Jokers = countOf(cards,c)
            if(count_Jokers == 5):
                card_count.append(0)
        else:
            card_count.append(countOf(cards,c))
    
    max_matches = max(card_count) + count_Jokers
    num_matches = len(card_count)
    
    if(max_matches >= 4):
        hand_type = max_matches + 1
    elif(num_matches == 3):
        hand_type = max_matches
    elif(num_matches == 5):
        hand_type = 0
    elif(num_matches == 4):
        hand_type = 1
    else:
        hand_type = 4
    
    return hand_type

def setCardVals(cards):
    cards = ['10' if x=='T' else x for x in cards]
    cards = ['0' if x=='J' else x for x in cards]
    cards = ['12' if x=='Q' else x for x in cards]
    cards = ['13' if x=='K' else x for x in cards]
    cards = ['14' if x=='A' else x for x in cards]
    cards = [int(x) for x in cards]
    return cards

def getHandTypePart1(cards):
    distinct_cards = set(cards)
    card_count = []
    hand_type = None

    for c in distinct_cards:
        card_count.append(countOf(cards,c))
    
    max_matches = max(card_count)
    num_matches = len(card_count)
    if(max_matches >= 4):
        hand_type = max_matches + 1
    elif(num_matches == 3):
        hand_type = max_matches
    elif(num_matches == 5):
        hand_type = 0
    elif(num_matches == 4):
        hand_type = 1
    else:
        hand_type = 4
    
    return hand_type


def day7(f):
    f = f.readlines()
    numHands = len(f)
    all_Hands = []
    

    for line in f:
        line = line.strip().split(" ")
        cards = [char for char in line[0]]
        cards = setCardVals(cards)

        bid = line[1]
        hand_type = getHandType(cards)
        all_Hands.append(Hand(cards, bid, hand_type))

    all_Hands.sort(key=lambda x:(x.hand_type,x.cards[0],x.cards[1],x.cards[2],x.cards[3],x.cards[4]),reverse=True)
    result = 0
    for i in range(numHands):
        winnings = 0
        r = numHands-i
        h = all_Hands[i]
        winnings = int(h.bid) * r
        result = result+winnings
        print(h)
        print("  rank:"+str(r)+" winnings: "+str(winnings))

    print(result)
    
    

