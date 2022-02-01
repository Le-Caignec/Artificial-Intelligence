from dataclasses import dataclass
import agent.Agent
import environement.Diamond
from environement import Diamond, Dust
from agent import Agent
from random import uniform, randint

@dataclass
class Case:
    diamond: Diamond
    dust: Dust
    agent: Agent

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
        if case.diamond is not None:
            self.grid[x_position][y_position].diamond = case.diamond
        if case.dust is not None:
            self.grid[x_position][y_position].dust = case.dust
        if case.agent is not None:
            self.grid[x_position][y_position].agent = case.agent

    def Afficher(self):
        for row in range(5):
            for case in range(5):
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
        ag = agent.Agent.Agent(randint(0, 4), randint(0, 4))
        self.SetCase(Case(None, None, ag), ag.x_position, ag.y_position)
        for row in range(5):
            for column in range(5):
                if uniform(0, 3) <= 1:
                    diamond = environement.Diamond.Diamond(row, column)
                    self.SetCase(Case(diamond, None, None), diamond.x_position, diamond.y_position)
                if uniform(0, 3) <= 1:
                    dust = environement.Dust.Dust(row, column)
                    self.SetCase(Case(None, dust, None), dust.x_position, dust.y_position)

