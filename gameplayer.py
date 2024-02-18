import math
import random

#This class becomes the super base class
#Now we will have human player and computer player
class Player:
    def __init__(self, letter):
        #Letter for the player whether x or o
        self.letter = letter
    #This will provide with the moves to be made by the players in game
    def get_move(self,game):
        pass

class compPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square
class humanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move(0-9):')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again')
        return val