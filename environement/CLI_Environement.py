from struct import Struct
from environement import Diamond, Dust
from agent import Agent
from random import uniform, randint

class Case(Struct):
    diamond = Diamond
    dust = Dust

class Score(Struct):
    collected_diamond = int
    aspirated_dust = int
    aspirated_diamond = int

class CLI_Environement:

    def __init__(self):
        self.grid = [[Case for i in range(5)] for k in range(5)]
        self.score = Score

    def SetCase(self, diamond, dust, x_position, y_position):
        if diamond is not None:
            self.grid[x_position][y_position].diamond = diamond
        if dust is not None:
            self.grid[x_position][y_position].dust = dust

    def AfficherGrid(self):
        for row in len(self.grid):
            for case in len(row):
                print("-----------CASE--------------")
                case.dust.AfficherDust()
                case.diamond.AfficherDiamond()

    def ClearCase(self, x_position, y_position):
        if self.grid[x_position][y_position].diamond is not None:
            self.grid[x_position][y_position].diamond = None
        if self.grid[x_position][y_position].dust is not None:
            self.grid[x_position][y_position].dust = None

    def ClearGrid(self):
        self.grid = [[Case for i in range(5)] for k in range(5)]

    def UpdateScore(self, score):
        self.score = score

    def GenerateGrid(self):
        agent = Agent(self.fenetre, randint(3, 7), randint(0, 4))
        agent.PutAgent()
        for row in range(3, 8):
            for column in range(5):
                if uniform(0, 3) <= 1:
                    diamond = Diamond(self.fenetre, row, column)
                    diamond.PutDiamond()
                    agent.captor.SetCase(diamond, None, row, column)
                if uniform(0, 3) <= 1:
                    dust = Dust(self.fenetre, row, column)
                    dust.PutDust()
                    agent.captor.SetCase(None, dust, row, column)
        # agent.captor.AfficherGrid()

