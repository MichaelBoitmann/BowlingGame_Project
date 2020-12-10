# IT6039 Software Testing and Maintenance
#
# Student: 90054169
#
# Project: Ten-Pin Game

class BowlingGame(object):

    """Class for Bowling Game frames

    Args:
        object ([self]): [
            Class has functions which allow the tests to check if a strike, 
            spare or number of pins were counted
            ]
    """
    
    def __init__(self):
        self.throws= [] # refactor throw to throw
        self.score= 0

        """Generate Array for throws of Score
        """    

    def throw(self, pins):
        self.throws.append(pins)

        """ Uses pins for every throw out of 10
        """         
 
    def calculate_score(self):

        """This is the function for throwing, striking and spare
        """        

        ball = 0
        
        for frames in range(10):        # corrected all the syntax error
            if self.throws[ball]==10:   # from "throw" to "throws"
                self.score +=10 + self.throws[ball+1] + self.throws[ball +2]
                ball += 1
            elif self.throws[ball] + self.throws[ball+1] == 10:
                self.score +=10 + self.throws[ball +2]
                ball +=2
            else:
                self.score += self.throws[ball] + self.throws[ball + 1]
                ball += 2
