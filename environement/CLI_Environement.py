from dataclasses import dataclass
from random import uniform, randint
from agent.Agent import *

@dataclass
class Case:
    x_position: int
    y_position: int
    diamond: bool
    dust: bool

@dataclass
class Score:
    collected_diamond: int = 0
    aspirated_dust: int = 0
    aspirated_diamond: int = 0

class CLI_Environement:

    def __init__(self):
        self.grid = [[Case for i in range(5)] for k in range(5)]
        self.score = Score

    def SetCase(self, case, x_position, y_position):
        if case.diamond is True:
            self.grid[x_position][y_position].diamond = case.diamond
        if case.dust is True:
            self.grid[x_position][y_position].dust = case.dust

    def Afficher(self):
        print("[")
        for x_position in range(5):
            for y_position in range(5):
                print("["+str(self.grid[x_position][y_position].diamond)+","+str(self.grid[x_position][y_position].dust)+"], ", end='')
            print("")
        print("]")

    def ClearCase(self, x_position, y_position):
        if self.grid[x_position][y_position].diamond is True:
            self.grid[x_position][y_position].diamond = False
        if self.grid[x_position][y_position].dust is True:
            self.grid[x_position][y_position].dust = False

    def ClearGrid(self): 
        self.grid = [[Case for i in range(5)] for k in range(5)]

    def getGrid(self):
        return self.grid

    def UpdateScore(self, score):
        self.score = score

    def GenerateGrid(self):
        Agent(randint(0, 4), randint(0, 4))
        for row in range(5):
            for column in range(5):
                if uniform(0, 3) <= 1:
                    OneCase = Case(row, column, True, False)
                    self.SetCase(OneCase, row, column)
                if uniform(0, 3) <= 1:
                    OneCase = Case(row, column, False, True)
                    self.SetCase(OneCase, row, column)

