import encodings
from dataclasses import dataclass
from math import dist
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

    def Life(self):
        if self.plan_action == []:
            self.algoNonInformé()
            print("--------------------PLAN ACTION---------------")
            print(self.plan_action)
        self.Deplacement()
        self.AfficherAgent()
        self.Action()

    def Search_Objective(self):
        L=[]
        grid = self.environnement.grid
        for x_pos in range(5):
            for y_pos in range(5):
                case = self.environnement.grid[x_pos][y_pos]
                if case.dust or case.diamond:
                    L.append(case)
        return L
    
    def Distance(self,start_case, final_case):
        distance_x = abs(start_case.x_position - final_case.x_position)
        distance_y = abs(start_case.y_position - final_case.y_position)
        distance = distance_x + distance_y
        return distance
    
    def algoNonInformé(self):
        Objectives = self.Search_Objective()
        List_opti = []
        n = len(Objectives)
        distance_min = 0
        for i in range(n):
            distance = 0
            List = []
            distance, List, bool= self.Parcours(Objectives, i, distance, distance_min, List, True) 
            if bool:
                distance_min = distance
                List_opti = List
        self.plan_action = List_opti
    
    def Parcours(self, Objectives, i, distance, distance_min, List, bool):
        n = len(Objectives)
        distance += self.Distance(List[-1], Objectives[i])
        if distance >= distance_min:
            return distance, List, False
        elif bool:
            List.append(Objectives[i])
            if n == 1:
                return distance, List, True
            else:
                Objectives.pop(i)
                for j in range(n):
                    distance, List, bool = self.Parcours(Objectives, j, distance, distance_min, List, True)
                    return 