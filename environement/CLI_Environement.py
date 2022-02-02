from dataclasses import dataclass
from random import uniform, randint
from agent.Agent import *

@dataclass
class Case:
    x_position: int = 0
    y_position: int = 0
    diamond: bool = False
    dust: bool = False

@dataclass
class Score:
    collected_diamond: int = 0
    aspirated_dust: int = 0
    aspirated_diamond: int = 0

class CLI_Environement:

    def __init__(self):
        self.grid = [[Case() for i in range(5)] for k in range(5)]
        self.score = Score

    def SetCase(self, case):
        if case.diamond is True:
            self.grid[case.x_position][case.y_position].diamond = case.diamond
        if case.dust is True:
            self.grid[case.x_position][case.y_position].dust = case.dust

    def Afficher(self):
        print("--------------GRILLE-------------------")
        print("[")
        for x_position in range(5):
            for y_position in range(5):
                print("["+str(self.grid[x_position][y_position].diamond)+","+str(self.grid[x_position][y_position].dust)+"], ", end='')
            print("")
        print("]")

    def ClearCase(self, x_position, y_position):
        self.grid[x_position][y_position].diamond = False
        self.grid[x_position][y_position].dust = False

    def ClearGrid(self): 
        self.grid = [[Case() for i in range(5)] for k in range(5)]

    def UpdateScore(self, score):
        self.score = score

    def GenerateNewGrid(self):
        Agent(randint(0, 4), randint(0, 4)).AfficherAgent()
        for row in range(5):
            for column in range(5):
                if uniform(0, 3) <= 1:
                    one_case = Case(row, column, True, False)
                    self.SetCase(one_case)
                if uniform(0, 3) <= 1:
                    one_case = Case(row, column, False, True)
                    self.SetCase(one_case)

    def GenerateNewCase(self, x_position, y_position):
        if uniform(0, 3) <= 1:
            one_case = Case(x_position, y_position, True, False)
            self.SetCase(one_case)
        if uniform(0, 3) <= 1:
            one_case = Case(x_position, y_position, False, True)
            self.SetCase(one_case)
