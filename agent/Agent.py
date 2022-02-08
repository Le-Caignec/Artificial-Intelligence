import encodings
from dataclasses import dataclass
from math import dist
from os import environ
from tkinter import *
from tracemalloc import start
from PIL import ImageTk, Image
from agent import Brain
from environement.CLI_Environnement import *

@dataclass
class Score:
    collected_diamond: int = 0
    aspirated_dust: int = 0
    aspirated_diamond: int = 0

class Agent:

    def __init__(self, x_position, y_position, environnement):
        self.x_position = x_position
        self.y_position = y_position
        self.plan_action = []
        self.environnement = environnement
        self.score = Score()
        self.objectif = self.Search_Objective()

    def AfficherAgent(self):
        print("--------------AGENT-------------------")
        print("- x_position : "+str(self.x_position))
        print("- y_position : "+str(self.y_position))

    def UpdateScore(self, score):
        self.score = score
        
    def Action(self):
        case = self.environnement.grid[self.x_position][self.y_position]
        print("--------------------ACTION---------------")
        if case.dust:
            if case.diamond:
                self.score.aspirated_diamond += 1
                print("J'ai aspirer un diamant !")
            self.score.aspirated_dust += 1
            self.plan_action.remove(case)
            print("J'ai aspirer une poussière !")
        elif case.diamond:
            self.score.collected_diamond += 1
            self.plan_action.remove(case)
            print("J'ai collecter un diamant !")
        self.environnement.ClearCase(case.x_position, case.y_position)
                
    def Deplacement(self):
        if not self.plan_action:
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
        else:
            print("Inutile de se déplacer car la grille est vide : ni diamant, ni poussière")
       
    def Search_Objective(self):
        L = []
        grid = self.environnement.grid
        for x_pos in range(5):
            for y_pos in range(5):
                case = self.environnement.grid[x_pos][y_pos]
                if case.dust or case.diamond:
                    L.append(case)
        return L
    
    def Distance(self, start_case, final_case):
        distance_x = abs(start_case.x_position - final_case.x_position)
        distance_y = abs(start_case.y_position - final_case.y_position)
        distance = distance_x + distance_y
        return distance
    
    def AlgoNonInforme(self):
        list_opti = [self.environnement.grid[self.x_position][self.y_position]]
        n = len(self.objectif)
        for i in range(n):
            obj_to_delete = self.objectif[0]
            distance_min = self.Distance(list_opti[-1], obj_to_delete)
            for obj in self.objectif:
                distance_temp = self.Distance(list_opti[-1], obj)
                if distance_min > distance_temp:
                    distance_min = distance_temp
                    obj_to_delete = obj
            self.objectif.remove(obj_to_delete)
            list_opti.append(obj_to_delete)
        list_opti.pop(0)
        return list_opti


            
