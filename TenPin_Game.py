# IT6039 Software Testing and Maintenance
#
# Student: 90054169
#
# Project: Ten-Pin Game

class BowlingGame(object):
    def __init__(self):
        self.throws= []
        self.score= 0

    def throw(self, pins):
        self.throws.append(pins)
 
 
    def calculate_score(self):  # addedd "frames" inside the function
                                        # parenthese
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