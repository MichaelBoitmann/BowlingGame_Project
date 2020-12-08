# IT6039 Software Testing and Maintenance
#
# Student: 90054169
#
# Project: Ten-Pin Game

class BowlingGame(object):
    def __init__(self):
        self.throw= []
        self.score= 0

    def throw(self,pins):
        self.throw.append(pins)


    def calculate_score(self):
        ball = 0
        for frames in range(10):
            if self.throws[ball]==10:
                self.score +=10 + self.throws[ball+1] + self.throws[ball +2]
                ball += 1
            elif self.throw[ball] + self.throws[ball+1] == 10:
                self.score += 10 + self.throws [ball +2]
                ball +=2
            else:
                self.score += self.throws[ball] + self.throw[ball + 1]
                ball += 2