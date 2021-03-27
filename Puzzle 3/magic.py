#Programming for the Puzzled -- Srini Devadas
#You Can Read Minds (With a Little Calibration)
#Five random cards are chosen and one of them is hidden.
#Given four cards in a particular order, you can figure out what the fifth card is!

#Deck is are a list of strings, each string is a card
#The order of cards in the list matters.
deck = ['A_C', 'A_D', 'A_H', 'A_S', '2_C', '2_D', '2_H', '2_S', '3_C', '3_D', '3_H', '3_S',
        '4_C', '4_D', '4_H', '4_S', '5_C', '5_D', '5_H', '5_S', '6_C', '6_D', '6_H', '6_S',
        '7_C', '7_D', '7_H', '7_S', '8_C', '8_D', '8_H', '8_S', '9_C', '9_D', '9_H', '9_S',
        '10_C', '10_D', '10_H', '10_S', 'J_C', 'J_D', 'J_H', 'J_S',
        'Q_C', 'Q_D', 'Q_H', 'Q_S', 'K_C', 'K_D', 'K_H', 'K_S']
         
#Given 5 cards, Assistant hides an appropriate card
#He/she reads out the remaining four cards after choosing their order carefully!
def AssistantOrdersCards():

    print ('Cards are character strings as shown below.')
    print ('Ordering is:', deck)

    #Initialization
    cards, cind, cardsuits, cnumbers = [], [], [], []
    numsuits = [0, 0, 0, 0]

    #Take cards as input from user/audience
    #Various data structures are filled in
    for i in range(5):
        print ('Please give card', i+1, end = ' ')
        card = input('in above format:')
        cards.append(card)
        n = deck.index(card)
        cind.append(n)
        cardsuits.append(n % 4)
        cnumbers.append(n // 4)
        numsuits[n % 4] += 1
        if numsuits[n % 4] > 1:
            pairsuit = n % 4

    #Find two cards out of the 5 that have the same suit. Guaranteed to exist.
    cardh = []
    for i in range(5):
        if cardsuits[i] == pairsuit:
            cardh.append(i)

    #Figure out which card needs to be hidden and what number to encode
    hidden, other, encode = outputFirstCard(cnumbers, cardh, cards)

    remindices = []
    for i in range(5):
        if i != hidden and i != other:
            remindices.append(cind[i])

    #Order the three cards in ascending order
    sortList(remindices)

    #Given the number that needs to be encoded, order the cards appropriately
    outputNext3Cards(encode, remindices)

    return



#This procedure figures out which card should be hidden based on the distance
#between the two cards that have the same suit.
#It returns the hidden card, the first exposed card, and the distance
def outputFirstCard(numbers, oneTwo, cards):


    encode = (numbers[oneTwo[0]] - numbers[oneTwo[1]]) % 13
    if encode > 0 and encode <= 6:
        hidden = oneTwo[0]
        other = oneTwo[1]
    else:
        hidden = oneTwo[1]
        other = oneTwo[0]
        encode = (numbers[oneTwo[1]] - numbers[oneTwo[0]]) % 13

    ##    #The following print statement is just for debugging!
    ##    print ('Hidden card is:', cards[hidden], 'and need to encode', encode)
    print ('First card is:', cards[other])

    return hidden, other, encode


#This procedure orders three cards depending on the number "code" that
#needs to be encoded. 
def outputNext3Cards(code, ind):
    
    if code == 1:
        second, third, fourth = ind[0], ind[1], ind[2]
    elif code == 2:
        second, third, fourth = ind[0], ind[2], ind[1]
    elif code == 3:
        second, third, fourth = ind[1], ind[0], ind[2]       
    elif code == 4:
        second, third, fourth = ind[1], ind[2], ind[0]
    elif code == 5:
        second, third, fourth = ind[2], ind[0], ind[1]
    else:
        second, third, fourth = ind[2], ind[1], ind[0]

    print ('Second card is:', deck[second])
    print ('Third card is:', deck[third])
    print ('Fourth card is:', deck[fourth])

    
#Sorts elements in tlist in ascending order.
def sortList(tlist):
    for index in range(0, len(tlist)-1):
        ismall = index
        for i in range(index, len(tlist)):
            if tlist[ismall] > tlist[i]:
                ismall = i
        tlist[index], tlist[ismall] = tlist[ismall], tlist[index]
    
    return


#This procedure takes four cards encoded properly and determines the hidden card.
def MagicianGuessesCard():
    print ('Cards are character strings as shown below.')
    print ('Ordering is:', deck)
    cards, cind = [], []
    for i in range(4):
        print ('Please give card', i+1, end = ' ')
        card = input('in above format:')
        cards.append(card)
        n = deck.index(card)
        cind.append(n)
        if i == 0:
            suit = n % 4
            number = n // 4
            
    #Use the ordering of the last 3 cards to determine distance from 1st card
    if cind[1] < cind[2] and cind[1] < cind[3]:
        if cind[2] < cind[3]:
            encode = 1
        else:
            encode = 2
    elif ((cind[1] < cind[2] and cind[1] > cind[3])
         or (cind[1] > cind[2] and cind[1] < cind[3])):
        if cind[2] < cind[3]:
            encode = 3
        else:
            encode = 4
    elif cind[1] > cind[2] and cind[1] > cind[3]:
        if cind[2] < cind[3]:
            encode = 5
        else:
            encode = 6

    #Knowing the number and the suit gives the card index and then string
    hiddennumber = (number + encode) % 13
    index = hiddennumber * 4 + suit

    print ('Hidden card is:', deck[index])


#This procedure is similar to AssistantOrdersCards() except it
#takes in a large number and "randomly" generates five cards.
def ComputerAssistant():

    print ('Cards are character strings as shown below.')
    print ('Ordering is:', deck)
    cards, cind, cardsuits, cnumbers = [], [], [], []
    numsuits = [0, 0, 0, 0]
    number = 0
    while number < 99999:
        number = int(input('Please give random number' +
                               ' of at least 6 digits:'))
    for i in range(5):
        number = number * (i + 1) // (i + 2)
        n = number % 52
        cards.append(deck[n])
        cind.append(n)
        cardsuits.append(n % 4)
        cnumbers.append(n // 4)
        numsuits[n % 4] += 1
        if numsuits[n % 4] > 1:
            pairsuit = n % 4
            
    ##    #Just for debugging
    ##    print (cards)
    cardh = []
    for i in range(5):
        if cardsuits[i] == pairsuit:
            cardh.append(i)

    hidden, other, encode = outputFirstCard(cnumbers, cardh, cards)

    remindices = []
    for i in range(5):
        if i != hidden and i != other:
            remindices.append(cind[i])

    sortList(remindices)
    outputNext3Cards(encode, remindices)

    guess = input('What is the hidden card?')
    if guess == cards[hidden]:
        print ('You are a Mind Reader Extraordinaire!')
    else:
        print ('Sorry, not impressed!')

    return

# AssistantOrdersCards()
MagicianGuessesCard()
