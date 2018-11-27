import random

class Card(object):
    def __init__(self, suit, number):
        self.suit = suit;
        self.number = number;

    def __str__(self):                                                          #turns the number of the face cards into a letter representing them
        out = "|"
        if self.number == 1:
            out+= "A"
        elif self.number == 11:
            out+= "J"
        elif self.number == 12:
            out+= "Q"
        elif self.number == 13:
            out+= "K"
        else:
            out += str(self.number)
        if self.suit == 0:                                                      #turns the number representing the suit into the unicode character for the suit
            out += "♠"
        if self.suit == 1:
            out += "♥"
        if self.suit == 2:
            out += "♦"
        if self.suit == 3:
            out += "♣"
        out += "|"
        return out

    def CardSuit(self, suit):
        self.suit = suit

    def CardNumber(self, number):
        self.number = number

class Hand(object):
    def __init__(self, cards):
        self.cards = cards;

    def __str__(self):
        out = ""
        out += "--------HAND---------\n"
        for card in self.cards:                                                 #prints all the cards in the hand using the card print magic function
            out += card.__str__()
        out += "\n---------------------"
        return out

    def ResetHand(self):
        self.cards = []

class Deck(object):
    def __init__(self, cards):
        self.cards = cards;

    def __str__(self):
        out = ""
        for card in self.cards:                                                 #prints all the cards in the deck using the card print magic function
            out += card.__str__()
        return out

    def ResetDeck(self):
        self.cards = []
        for i in range(53):                                                     #Fills the deck with the starting cards not shuffled
            if i <= 12:
                self.cards.append(Card(0,i+1))
            if i > 13 and i <= 26:
                self.cards.append(Card(1,i-13))
            if i > 26 and i <= 39:
                self.cards.append(Card(2,i-26))
            if i > 39:
                self.cards.append(Card(3,i-39))

    def ShuffleDeck(self):                                                      #uses random shuffle to shuffle the cards in the deck
        random.shuffle(self.cards)

    def Deal(self, targetHand, amountToDraw):
        if len(self.cards)-1 > 0:
            for i in range(amountToDraw):
                try:
                    targetHand.cards.append(self.cards[len(self.cards)-1])      #add the last card of the deck to the target hand
                    self.cards.pop(len(self.cards)-1)                           #remove that card from the deck
                except:
                    print("The deck has run out of cards!")
                    break

deck1 = Deck([])
hand1 = Hand([])

deck1.ResetDeck()
deck1.ShuffleDeck()

while True:
    playerIn = input("Do you want to deal another hand (y/n)?")
    playerIn.lower()
    if len(deck1.cards) <= 0:                                                   #if the deck is empty, reset it
        deck1.ResetDeck()
        deck1.ShuffleDeck()
    if playerIn == "y":                                                         #deal the player a hand if they type y
        hand1.ResetHand()
        deck1.Deal(hand1, 5)
        print(hand1)
    elif playerIn == "n":                                                       #exit the program if they type n
        break
    else:
        print("Please enter y or n")                                            #make sure the player enters y or n
