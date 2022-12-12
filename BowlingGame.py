#File 2 (BowlingGame.py)
#This file has information about Bowling Game for which the description is provided in project assessment.

class BowlingGame:
    def __init__(self):
        self.rolls=[]

    def roll(self,pins):
        self.rolls.append(pins)

    def score(self):
        result = 0
        rollIndex=0
        for frameIndex in range(10):                
            # conditional statements for checking different cases targeting index of an array
            if self.rolls[rollIndex] == 10:
                result += 10 + self.rolls[rollIndex + 1] + self.rolls[rollIndex + 2]     # score target 10 points plus next 2 index numbers (total of these 2 niumbers as a bonus points) as a bonus points
                rollIndex += 1
            elif self.rolls[rollIndex] + self.rolls[rollIndex + 1] == 10:
                result += 10 + self.rolls[rollIndex + 2]                       #score targeting 10 points plus 1 bonus ball points if 2 ball in a frame are 10
                rollIndex += 2
            else:
                result += self.rolls[rollIndex] + self.rolls[rollIndex + 1]     # score targeting just normal ball points
                rollIndex += 2
        return result

    # def isStrike(self, rollIndex):
    #     return self.rolls[rollIndex] == 10
    # def isSpare(self, rollIndex):
    #     return self.rolls[rollIndex]+ self.rolls[rollIndex+1]==10
    # def stickeScore(self,rollIndex):
    #     return  10+ self.rolls[rollIndex+1]+ self.rolls[rollIndex+2]

    # def spareScore(self,rollIndex):
    #     return  10+ self.rolls[rollIndex+2]

    # def frameScore(self, rollIndex):
    #     return self.rolls[rollIndex] + self.rolls[rollIndex + 1]
		

#Your tasks for code parts:
#1: If there are any bugs in the code, you have to remove using debugging and run the project and test cases.
#2: Refactor the code (Improve its structure without changing external behaviour).
#3: Report everything using github commits and versioning control.


###### Important #####
# Please complete your project and all tasks according to assessment description provided in CANVAS.