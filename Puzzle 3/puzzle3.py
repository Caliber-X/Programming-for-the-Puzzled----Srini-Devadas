# Programming for the Puzzled -- Puzzle 3
# You can Read Minds
# By Caliber_X

#Deck is are a list of strings, each string is a card
#The order of cards in the list matters.
#         0      1      2      3
deck = ['A_C', 'A_D', 'A_H', 'A_S',
        '2_C', '2_D', '2_H', '2_S',
        '3_C', '3_D', '3_H', '3_S',
        '4_C', '4_D', '4_H', '4_S',
        '5_C', '5_D', '5_H', '5_S',
        '6_C', '6_D', '6_H', '6_S',
        '7_C', '7_D', '7_H', '7_S',
        '8_C', '8_D', '8_H', '8_S',
        '9_C', '9_D', '9_H', '9_S',
        '10_C', '10_D', '10_H', '10_S',
        'J_C', 'J_D', 'J_H', 'J_S',
        'Q_C', 'Q_D', 'Q_H', 'Q_S',
        'K_C', 'K_D', 'K_H', 'K_S']

def Assistant_Encode():

        print("Deck = ", deck)

        # Initialization
        cards, cindex = [], []  # Cards
        pair, pindex = [], []  # pair
        t = 0

        # Entry from User
        print("Enter the cards in above format:")
        for i in range(5):

                print("Enter ", i + 1, "card : ", end = '')
                c = input()
                cards.append(c)
                a = deck.index(c)

                flag = 0

                for j in range(i):
                
                        # Prevent Iteration of Same card
                        while cards[j] == cards[i]:
                                print("Pls REenter, Same card not acceptable")
                                cards.pop(-1)  #Remove last added
                                print("Enter ", i + 1, "card : ", end = '')
                                c = input()
                                cards.append(c)
                                a = deck.index(c)

                        # Find Same Suit
                        if t == 0:                              # First Apperance
                                b = deck.index(cards[j])
                                if (a - b) % 4 == 0:
                                        pair.append(cards[i])
                                        pair.append(cards[j])
                                        pindex.append(a // 4)
                                        pindex.append(b // 4)
                                        t = 1
                                        break

                cindex.append(a)

        # print("Cards:", cards, "Index:", cindex)
        # print("Suit:", pair, "Index:", pindex)

        hidden, first, diff = firstcard(pair, pindex)

        # 1st card
        print("1st card is:", first)

        # Sort the remaining cards according to deck priority 
        # CDHS sort (Uncomment the below line for CDHS priority)
        # deck.sort(key = lambda x: x[-1])

        remainingcards = []
        for i in deck:
                for j in cards:
                        if i == j and i != first and i != hidden:
                                remainingcards.append(i)
                                break
        # print("Sorted Remaining Cards:",remainingcards) 

        second, third, fourth = last3cards(remainingcards, diff)

        # 2nd, 3rd, 4th cards
        print("2nd card is:", second)
        print("3rd card is:", third)
        print("4th card is:", fourth)

        # # MAGICIAN Guess Last Card
        # card = input("Guess the 5th card: ")
        # if card == hidden:
        #         print("U r a magician extraordinare !!!")
        # else:
        #         print("Fuck off u fucking asshole !!!")
        
def firstcard(pair, pindex):

        # diff = pindex[0] - pindex[1]

        # if (diff > 0 and diff <= 6) or diff < -6:
        #         show = pair[1]
        #         hide = pair[0]

        # else:
        #         show = pair[0]
        #         hide = pair[1]

        # if diff < 0:
        #         diff *= -1
        # if diff > 6:
        #         diff = 13 - diff
        
        diff = (pindex[0] - pindex[1]) % 13

        if diff > 0 and diff <= 6 :
                show = pair[1]
                hide = pair[0]

        else:
                show = pair[0]
                hide = pair[1]
                diff = 13 - diff

        return hide, show, diff

def last3cards(cards, diff):

        third = 0
                
        if diff % 2 == 1:
                i = diff
        else:
                i = diff - 1
                               
        second = cards[i // 2]

        for j in range (3):
                
                if j != i // 2:
                        if third == 0:
                                third = cards[j]
                        fourth = cards[j]

        if diff % 2 == 0:
                third, fourth = fourth, third

        return second, third, fourth

# DECODE Functinality
def MagicianGuessesCard():

        print("Deck = ", deck)

        # Initialization
        cards, cindex = [], []  # Cards

        # Entry from User
        print("Enter the cards in above format:")
        for i in range(4):

                print("Enter ", i + 1, "card : ", end = '')
                c = input()
                cards.append(c)
                a = deck.index(c)

                for j in range(i):
                
                        # Prevent Iteration of Same card
                        while cards[j] == cards[i]:
                                print("Pls REenter, Same card not acceptable")
                                cards.pop(-1)  #Remove last added
                                print("Enter ", i + 1, "card : ", end = '')
                                c = input()
                                cards.append(c)
                                a = deck.index(c)
                
                cindex.append(a)
        print("Cards:", cards, "Index:", cindex)
        
        # Calculate Difference/Encoding
        if (cindex[1] < cindex[2] and cindex[1] < cindex[3]):
                encode = 1
                if cindex[2] > cindex[3]:
                        encode += 1

        elif (cindex[2] < cindex[1] and cindex[2] < cindex[3]):
                encode = 3
                if cindex[1] > cindex[3]:
                        encode += 2

        elif (cindex[3] < cindex[1] and cindex[3] < cindex[2]):
                encode = 4
                if cindex[1] > cindex[2]:
                        encode += 2
        print("Encoding =", encode)

        n = ((((cindex[0] // 4) + encode) % 13) * 4) + (cindex[0] % 4)
        
        print("Hidden card is", deck[n])

import random
# This procedure is similar to Assistant_Encode() except it "randomly" generates five cards
def ComputerAssistant():

        print("Deck = ", deck)

        cards = random.sample(deck, 5)  # 5 random cards from Deck
        
        # Initialization
        cindex = []             # Cards
        pair, pindex = [], []   # Pair
        t = 0

        for i in range(5):

                a = deck.index(cards[i])

                flag = 0

                for j in range(i):
                
                        # Find Same Suit
                        if t == 0:                              # First Apperance
                                b = deck.index(cards[j])
                                if (a - b) % 4 == 0:
                                        pair.append(cards[i])
                                        pair.append(cards[j])
                                        pindex.append(a // 4)
                                        pindex.append(b // 4)
                                        t = 1
                                        break

                cindex.append(a)

        # print("Cards:", cards, "Index:", cindex)
        # print("Suit:", pair, "Index:", pindex)

        hidden, first, diff = firstcard(pair, pindex)

        # 1st card
        print("1st card is:", first)

        # Sort the remaining cards according to deck priority 
        # CDHS sort (Uncomment the below line for CDHS priority)
        # deck.sort(key = lambda x: x[-1])

        remainingcards = []
        for i in deck:
                for j in cards:
                        if i == j and i != first and i != hidden:
                                remainingcards.append(i)
                                break
        # print("Sorted Remaining Cards:",remainingcards) 

        second, third, fourth = last3cards(remainingcards, diff)

        # 2nd, 3rd, 4th cards
        print("2nd card is:", second)
        print("3rd card is:", third)
        print("4th card is:", fourth)

        # MAGICIAN Guess Last Card
        card = input("Guess the 5th card: ")
        if card == hidden:
                print("U r a magician extraordinare !!!")
        else:
                print("Fuck off u fucking asshole !!!")


# Run this for Assistant Encodes
# Assistant_Encode()

# Run this for Magician Decode
# MagicianGuessesCard()

# Practice for Magician
ComputerAssistant()

# # Debug firstcard function
# pair = ['X', 'Y']
# pindex = []
# for i in range(13):
#         for j in range(13):
#                 if i != j:
#                         pindex.append(i)
#                         pindex.append(j)
#                         hide, show, diff = firstcard(pair, pindex)
#                         print(i, j, show, hide, diff)
#                         pindex.clear()
