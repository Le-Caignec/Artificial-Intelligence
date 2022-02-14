from random import uniform
from dataclasses import dataclass


@dataclass
class Case:
    x_position: int = 0
    y_position: int = 0
    diamond: bool = False
    dust: bool = False
    note: float = 0.0


class CLI_Environment:

    def __init__(self):
        self.grid = [[Case(k, i) for i in range(5)] for k in range(5)]
        self.isNew = False

    # Function that enable to display the actual grid
    def DisplayGrid(self):
        print("-----------------NEW GRID-------------------")
        print("[")
        for y_position in range(5):
            for x_position in range(5):
                print("[" + self.isDiamond(x_position, y_position) + "," + self.isDust(x_position, y_position) + "], ",
                      end='')
            print("")
        print("]")

    # Function which is used to display the grid
    def isDiamond(self, x_position, y_position):
        if self.grid[x_position][y_position].diamond:
            return "Diams"
        else:
            return "00000"

    # Function which is used to display the grid
    def isDust(self, x_position, y_position):
        if self.grid[x_position][y_position].dust:
            return "Dust"
        else:
            return "0000"

    # Function that clear all the object in the case, diamond will be set to false
    # and dust too
    def ClearCase(self, x_position, y_position):
        self.grid[x_position][y_position].diamond = False
        self.grid[x_position][y_position].dust = False

    # Function which will give the neighbours of one case
    def get_neighboors(self, case):
        list_neighbors = []
        if case.x_position + 1 <= 4:
            list_neighbors.append(self.grid[case.x_position + 1][case.y_position])
        if case.x_position - 1 >= 0:
            list_neighbors.append(self.grid[case.x_position - 1][case.y_position])
        if case.y_position + 1 <= 4:
            list_neighbors.append(self.grid[case.x_position][case.y_position + 1])
        if case.y_position - 1 >= 0:
            list_neighbors.append(self.grid[case.x_position][case.y_position - 1])
        return list_neighbors

    # Function that will creat a new grid with a random probability to creat
    # a Dust or a Diamond for each case
    def GenerateNewGrid(self, proba):
        for x in range(5):
            for y in range(5):
                # ajout d'un diamond
                if uniform(0, 1 / proba) <= 1:
                    self.SetDiamond(x, y)

                # ajout de Dust
                if uniform(0, 1 / proba) <= 1:
                    self.SetDust(x, y)
                self.Evaluation(self.grid[x][y])
        self.isNew = True

    # Evaluation Function : It will enable to evaluate the cost of a case and
    # improve the decision of the informed algorithm
    def Evaluation(self, case):
        if case.dust:
            case.note = 6.6
            if case.diamond:
                case.note = 4.3
        elif case.diamond:
            case.note = 7.0

    # Diamond Setter
    def SetDiamond(self, x, y):
        self.grid[x][y].diamond = True

    # Dust Setter
    def SetDust(self, x, y):
        self.grid[x][y].dust = True
