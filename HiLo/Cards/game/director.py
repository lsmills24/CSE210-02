from game.card import Card

class Director:

    """A person who directs the game.
    
    Responsibility of a director is to control the sequence of play. 
    
    Attributes: 
        cards (list[card]): a list of the 2 cards
        is_playing (boolean): whether or not the game is being played. 
        score (int): The score for one round of play. 
        total_score: The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director
        
        Args:
            self (Director): an instance of Director.
        """

        self.cards = 0 # update it so it knows it is a number, doesn't need to be a list because it is only shows one card at a time
        self.is_playing = True
        self.guess = 0
        self.total_score = 300 #the score starts at 300
        self.card = Card() # make it so we can use the card class

    def start_game(self):
        """Starts the game by running the main loop.
        
        Args:
            self (Director): and instance of Director
        """
        while self.is_playing:
            self.card.draw() # call the function
            # guess = self.get_inputs()
            self.do_updates()
            self.do_outputs()
            self.play_again()

    def get_inputs(self):
        """Ask the user """
        self.guess = input("Is the next card higher or lower (h/l)? ")
    


    def do_updates(self):
        """Updates the player's score. 
        
        Args: 
            self (Director): ...
        """
        self.get_inputs()
        guess = self.guess
        self.card.after_guess(guess)
        self.total_score = self.card.points



    def do_outputs(self):
        print(f"Your score is {self.total_score}\n")
        if self.is_playing == (self.total_score > 0):
            return
        else: 
            print("You ran right out of points...")

    def play_again(self):
        play_again = input("Would you like to play again (y/n)? ")
        if play_again == 'y':
            self.is_playing
            self.start_game()
        else: 
            self.is_playing = False
            print(f"You ended the game with {self.total_score} points.")
            print("Come back soon ;)\n")