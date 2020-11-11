#creating a game.py card

#create a class that contain symbols and colours for cards
class Symbol:

    #creat colors and icons with string symbols and bianry color (red and black)
    #icons must be ["♥", "♦", "♣", "♠"]
    def __init__(self, icon : str):
        self.icon = icon
        if icon == "♥" or icon == "♦" :
            self.color = "red"
        else:
            self.color = "black"

    def __str__(self):
        print("icon: %s , color: %s " % (self.icon, self.color))

class Card(Symbol):

    #class that contain all deck cards values
    #values must be ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    def __init__(self, icon, value: str):
        super().__init__(icon)
        self.value = value

    def __str__(self):
        print(" %s  %s of %s " % (self.color, self.value, self.icon))


#a = Card('♦','heart')
#print(a)
