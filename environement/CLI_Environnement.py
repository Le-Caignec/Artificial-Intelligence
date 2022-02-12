from random import uniform
from dataclasses import dataclass

@dataclass
class Case:
    x_position: int = 0
    y_position: int = 0
    diamond: bool = False
    dust: bool = False
    note: float = 0.0


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

    def get_neighboors(self, case):
        list_neighbors = []
        if case.x_position+1 <= 4:
            list_neighbors.append(self.grid[case.x_position+1][case.y_position])
        if case.x_position-1 >= 0:
            list_neighbors.append(self.grid[case.x_position-1][case.y_position])
        if case.y_position+1 <= 4:
            list_neighbors.append(self.grid[case.x_position][case.y_position+1])
        if case.y_position-1 >= 0:
            list_neighbors.append(self.grid[case.x_position][case.y_position-1])        
        return list_neighbors

    def GenerateNewGrid(self, proba):
        for x in range(5):
            for y in range(5):
                one_case = Case(x, y, False, False)
                self.grid[one_case.x_position][one_case.y_position] = one_case
                #ajout d'un diamond
                if uniform(0, 1/proba) <= 1:
                    if self.grid[x][y].dust:
                        one_case = Case(x, y, True, True)
                    else: 
                        one_case = Case(x, y, True, False)

                #ajout de Dust
                if uniform(0, 1/proba) <= 1:
                    if self.grid[x][y].diamond:
                        one_case = Case(x, y, True, True)
                    else: 
                        one_case = Case(x, y, False, True)
                    self.grid[one_case.x_position][one_case.y_position] = one_case
                self.Evaluation(self.grid[x][y])

    def Evaluation(self, case):
            if case.dust:
                case.note = 15
                if case.diamond:
                    case.note = 10
            elif case.diamond:
                case.note = 20

