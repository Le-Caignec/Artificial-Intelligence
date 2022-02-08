from dataclasses import dataclass
from random import uniform, randint
from agent.Agent import *

@dataclass
class Case:
    x_position: int = 0
    y_position: int = 0
    diamond: bool = False
    dust: bool = False


class CLI_Environnement:

    def __init__(self):
        self.grid = [[Case() for i in range(5)] for k in range(5)]

    def Afficher(self):
        print("-----------------GRILLE-------------------")
        print("[")
        for y_position in range(5):
            for  x_position in range(5):
                print("["+self.isDiamond(x_position, y_position)+","+self.isDust(x_position, y_position)+"], ", end='')
            print("")
        print("]")

    def isDiamond(self, x_position, y_position):
        if self.grid[x_position][y_position].diamond:
            return "Diams"
        else : return "00000"

    def isDust(self, x_position, y_position):
        if self.grid[x_position][y_position].dust:
            return "Dust"
        else : return "0000"

    def ClearCase(self, x_position, y_position):
        self.grid[x_position][y_position].diamond = False
        self.grid[x_position][y_position].dust = False

    def ClearGrid(self): 
        self.grid = [[Case() for i in range(5)] for k in range(5)]


    def GenerateNewGrid(self, proba):
        for x in range(5):
            for y in range(5):
                #ajout d'un diamond
                if uniform(0, 1/proba) <= 1:
                    if self.grid[x][y].dust:
                        one_case = Case(x, y, True, True)
                    else: 
                        one_case = Case(x, y, True, False)
                    self.grid[one_case.x_position][one_case.y_position] = one_case
                #ajout de Dust
                if uniform(0, 1/proba) <= 1:
                    if self.grid[x][y].diamond:
                        one_case = Case(x, y, True, True)
                    else: 
                        one_case = Case(x, y, False, True)
                    self.grid[one_case.x_position][one_case.y_position] = one_case

