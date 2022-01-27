import random
# from game.director import Director

# Class declaration
class Card:

    ## A set of cards each with a different value 1-13, default is 0
    ## Start with 300 points

    ## Attributes:
        ## value (int): the number value of the 2 cards, where ace = 1 and king = 13
        ## points (int): start with 300 points 

    def __init__(self):

        self.value1 = 0
        self.value2 = 0
        self.points = 300

    def draw(self):
        # draw random card number and displays it
        self.value1 = random.randint(1,13)
        print(f"\nThe first card is {self.value1}")
            
    
    def after_guess(self, guess):

        self.value2 = random.randint(1,13)
        print(f"The second card is {self.value2}")

        if guess == "h" and self.value1 > self.value2:
            self.points -= 75
        elif guess == "h" and self.value1 < self.value2:
            self.points += 100
        elif guess == "l" and self.value1 < self.value2:
            self.points -= 75
        elif guess == "l" and self.value1 > self.value2:
            self.points += 100
        elif self.value1 == self.value2:
            self.points -= 75
        