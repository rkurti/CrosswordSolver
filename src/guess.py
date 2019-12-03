from clue import Clue

class Guess():
    def __init__(self, clue: Clue, string: str):
        self.clue = clue
        self.string = string
    
    def get_direction(self):
        return self.clue.get_direction()
    
    def get_length(self):
        return self.clue.get_length()
    
    def get_position(self):
        return self.clue.get_position()
    
    def get_string(self):
        return self.string
    
    def get_clue(self):
        return self.clue

    def __str__(self):
        return "GUESS// " + "CLUE: " + str(self. clue) + " GUESS: " + str(self.string)