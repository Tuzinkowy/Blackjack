from mimetypes import init
import random
#trzeba gdzieś dodać beat - wysokość zakładu

def creat_deck():
    deck = []
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    cards_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
    for suit in suits:
        for card in cards:
            deck.append(Card(suit, card, cards_values[card]))
    return deck

def player_turn():
    player_choice = input("What is your next move?(draw, split, pass) ")
    if player_choice == "draw":
        player.draw(deck)
    elif player_choice == "split":
        player.split()
    elif player_choice == "pass":
        player.end_turn(casino, deck)
    else:
        player_turn()


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

    def set_beat(self):
        beat = input("You have {chips}. How much do you wont beat? ".format(chips = self.chips))
        if int(beat) <= 0 and int(beat) > self.chips:
            print("something")
        else:
            self.beat = int(beat)
            print("You beat {beat} chips".format(beat = self.beat))


    def draw(self, deck):
        card = random.choice(deck)
        self.cards.append(card)
        deck.remove(card)
        print("your cards are: ")
        for card in self.cards:
            print("{suit} {value}".format(suit = card.suit, value = card.value))
        player_turn()

    def split():
        return 0

    def double_down():
        return 0

    def end_turn(self, casino, deck):
        #place holder pewnie bedzie wywołąnie metody z kasyna
        print("Now it's Casino turn.")
        casino.check_heand(self, deck)


class Casino:
    def __init__(self):
        self.chips = 5000
        self.heand = []

    def dael_the_cards(self, player, deck):
        while len(player.cards) < 2:
            dael = random.choice(deck)
            player.cards.append(dael)
            deck.remove(dael)
            print("Your cards are {suit} {value}".format(suit = dael.suit, value = dael.value))
        while len(self.heand) < 2:
            dael = random.choice(deck)
            self.heand.append(dael)
            deck.remove(dael)
        print("Casino first card is {suit} {value}".format(suit = self.heand[0].suit, value = self.heand[0].value))
        
        
    def win(self, player):
        self.chips += player.beat
        player.chips -= player.beat
        print("You lose. You lose {beat} chips, and you have now {chips} chips.".format(beat = player.beat, chips = player.chips))

    def lose(self, player):
        self.chips -= player.beat
        player.chips += player.beat
        print("You win. You get {beat} chips, and you have now {chips} chips.".format(beat = player.beat, chips = player.chips))


    def check_heand(self, player, deck):
        print("Casino second card is {suit} {value}".format(suit = self.heand[1].suit, value = self.heand[1].value))
        player_score = 0
        casino_score = 0

        for card in player.cards:
            player_score += card.card_value
        
        for card in self.heand:
            casino_score += card.card_value
        
        while (player_score > casino_score):
            print("Casino draw a card.")
            card = random.choice(deck)
            self.heand.append(card)
            deck.remove(card)
            casino_score += card.card_value
            print("New card is {suit} {value}".format(suit = card.suit, value = card.value))

        if casino_score <= 21 and casino_score > player_score:
            self.win(player)
        elif casino_score > 21 or casino_score < player_score:
            self.lose(player)
        else:
            print("There is a tie. You still have {chips} chips.".format(chips = player.chips))


username = input("What is your name? ")
player = User(username)
print("Welcom "+ username +" in Blackjak game, also know as 21.")
casino = Casino()
deck = creat_deck()
player.set_beat()
casino.dael_the_cards(player, deck)
player_turn()