import encodings
from dataclasses import dataclass
from os import environ
from tkinter import *
from PIL import ImageTk, Image
from agent import Captor
from environement import CLI_Environement

@dataclass
class Score:
    collected_diamond: int = 0
    aspirated_dust: int = 0
    aspirated_diamond: int = 0

class Agent:

    def __init__(self, x_position, y_position, environnement):
        self.plan_action = []
        self.environnement = environnement
        self.score = Score()
        self.x_position = x_position
        self.y_position = y_position

    def AfficherAgent(self):
        print("--------------AGENT-------------------")
        print("- x_position : "+str(self.x_position))
        print("- y_position : "+str(self.y_position))

    def UpdateScore(self, score):
        self.score = score
        
    def Action(self):
        case = self.environnement.grid[self.x_position][self.y_position]
        if case.dust:
            if case.diamond:
                self.score.aspirated_diamond += 1
            self.score.aspirated_dust += 1
            self.plan_action.remove(case)
            print("--------------------PLAN ACTION---------------")
            print(self.plan_action)
        elif case.diamond:
            self.score.collected_diamond += 1
            self.plan_action.remove(case)
            print("--------------------PLAN ACTION---------------")
            print(self.plan_action)
        self.environnement.ClearCase(case.x_position, case.y_position)
                
    def Deplacement(self):
        case_objectif = self.plan_action[0]
        #l'agent se déplace d'une case à chaque appel de Deplacement()
        #l'agent se déplace d'abord suivant les colonnes puis les lignes 
        if self.x_position < case_objectif.x_position:
            self.x_position += 1
        elif self.x_position > case_objectif.x_position:
            self.x_position -= 1
        else:
            if self.y_position < case_objectif.y_position:
                self.y_position += 1
            elif self.y_position > case_objectif.y_position:
                self.y_position -= 1

    def vie(self):
        if self.plan_action == []:
            self.algoNonInformé()
            print("--------------------PLAN ACTION---------------")
            print(self.plan_action)
        self.Deplacement()
        self.AfficherAgent()
        self.Action()

    def algoNonInformé(self):
        L=[]
        grid = self.environnement.grid
        for x_pos in range(5):
            for y_pos in range(5):
                case = self.environnement.grid[x_pos][y_pos]
                if case.dust or case.diamond:
                    L.append(case)
        self.plan_action = L



