#creating the Player class and its features

#importing files from card module
from card import *

#importing random module for shuffle use
import random


class Player(Symbol):
    #class that iterate the Symbol class and contains all the player turn informations

    #method that contain all about the player
    def __init__(self, name: str, icon):
        super().__init__(icon)
        self.name = name        #player name
        self.cards = []          #card name
        self.turn_count = 0     #number of turn
        self.card_numb = len(self.cards)     #number of cards
        self.history = []       #all cards played by the player

    def play(self):
        """
        Take a card from the player's hand and play it on the board
        :return: The card he plays.
        """
        #choose a random card
        number = int(input("You have {} left, choose the index for te card to be played:".format(len(self.cards))))
        card = self.cards[number]
        self.history += [card]
        print(self.name, self.turn_count, "played:", card.value, card.icon)
        return card

    def __str__(self):
        return " %s %s played : %s %s" % (self.name,
             self.turn_count,  self.card_numb, self.cards)

#a = Player()
#print(a)

#class Deck that contain all card decks for the game.py
class Deck():
    #init method
    def __init__(self):
        self.cards = []
    #    self.get_cards() # running the get_card method defined below to initiate with a full set of cards as your deck

    #def get_cards(self):
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        icons = ["♥", "♦", "♣", "♠"]
        for value in values:
            for icon in icons:
                self.cards.append((value, icon))

    def shuffle(self):
        random.shuffle(self.cards)



    def print_deck(self):
        for card in self.cards:
            print(card)
    def distribute(self, list_of_players : list):
        """
        Distribute the deck's cards in players' hands.
        :param list_of_players: The list of players in the game.py.
        """
        number_of_cards = int(52 / len(list_of_players))
        for i in list_of_players:
            for j in range(0, number_of_cards):
                i.cards += [self.cards[0]]
                self.cards.remove(self.cards[0])

    def __str__(self):
        return "Cards in deck : %s " % (self.cards)

#a = Deck()
#print(a)
