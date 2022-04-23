from mimetypes import init
from random import Random, random
#trzeba gdzieś dodać beat - wysolość zakładu


def creat_deck():
    deck = []
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    cards_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
    for suit in suits:
        for card in cards:
            deck.append(Card(suit, card, cards_values[card]))
    return deck

class Card:
    def __init__(self, suit,value, card_value):
        self.suit = suit
        self.value = value
        self.card_value = card_value
        

class User:
    def __init__(self, username = "Player 1"):
        self.username = username
        self.chips = 3000
        self.cards = []
        self.beat = 0

    def draw():
        return 0

    def split():
        return 0

    def double_down():
        return 0

    def end_turn():
        return 0

class Casino:
    def __init__(self):
        self.chips = 5000
        self.heand = []

    def dael_the_cards(self, player, deck):
        while len(player.cards) < 2:
            dael = Random.choice(deck)
            player.cards.append(dael)
            deck.remove(dael)
            print("Your cards are {suit}{value}".format(suit = dael.suit, value = dael.value))
        while len(self.heand) < 2:
            dael = Random.choice(deck)
            self.heand.append(dael)
            deck.remove(dael)
        print("Casino first card is {suit}{value}".format(suit = self.heand[0].suit, value = self.heand[0].value))
        
        
    def win(self, player):
        self.chips += player.beat
        player.chips -= player.beat
        print("You lose. You lose {beat} chips, and you have now {chips} chips.".format(beat = player.beat, chips = player.chips))

    def lose(self, player):
        self.chips -= player.beat
        player.chips += player.beat
        print("You win. You get {beat} chips, and you have now {chips} chips.".format(beat = player.beat, chips = player.chips))


    def check_heand(self, player):
        #system sprawdzania punktów na dłoni pracza i casyna
        player_score = 0
        casino_score = 0
        #for card in player.cards:


        if self.heand <= 21 and self.heand > player.heand:
            self.win(player)
        elif self.heand > 21 or self.heand < player.heand:
            self.lose(player)
        else:
            print("There is a tie. You still have {chips} chips.".format(chips = player.chips))





    
username = input("What is your name? ")
player = User(username)
print("Welcom "+ username +" in Blackjak game, also know as 21.")
casino = Casino()
casino.dael_the_cards(player, creat_deck())
