#Jennifer Gunther
#Introduction to Programming
# 27 April 2018

from random import *

class Player:
    def __init__(self, prob):
        self.prob = prob
        self.score = 0

    def winsServe(self):
        # Returns true with probability self.prob
        return random() <= self.prob

    def incScore(self):
        # Add a pouint to this player's score
        self.score = self.score + 15

    def getScore(self):
        # Return this player's current score
        return self.score
