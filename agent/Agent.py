from calendar import c
from dataclasses import dataclass
from tkinter import *
from PIL import ImageTk, Image
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
            if case in self.plan_action:
                self.plan_action.remove(case)
            print("J'ai aspirer une poussière !")
        elif case.diamond:
            self.score.collected_diamond += 1
            if case in self.plan_action:
                self.plan_action.remove(case)
            print("J'ai collecter un diamant !")
        self.environnement.ClearCase(case.x_position, case.y_position)
                
    def Deplacement(self):
        if self.plan_action != []:
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
                case = grid[x_pos][y_pos]
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
        list_objectives=self.copy(self.objectif)
        for i in range(n):
            obj_to_delete = list_objectives[0]
            distance_min = self.Distance(list_opti[-1], obj_to_delete)
            for obj in list_objectives:
                distance_temp = self.Distance(list_opti[-1], obj)
                if distance_min > distance_temp:
                    distance_min = distance_temp
                    obj_to_delete = obj
            list_objectives.remove(obj_to_delete)
            list_opti.append(obj_to_delete)
        list_opti.pop(0)
        return list_opti

    def Reconstruct_path(self, currentCase, cameFrom, startCase):
        reconst_path = []

        while cameFrom[str(currentCase.x_position)+str(currentCase.y_position)] != currentCase:
            reconst_path.append(currentCase)
            currentCase = cameFrom[str(currentCase.x_position)+str(currentCase.y_position)]

        reconst_path.reverse()
        return reconst_path

    #On utilise l'algorithme informé A* search
    def AlgoInforme(self):
        list_objectives = self.copy(self.objectif)

        noteMax = self.environnement.getNoteMax()

        startCase = self.environnement.grid[self.x_position][self.y_position]

        caseToVisit = [startCase]
        visitedCase = []
 
        noteFromStart = {}
        noteFromStart[str(startCase.x_position)+str(startCase.y_position)] = startCase.note
 
        cameFrom = {}
        cameFrom[str(startCase.x_position)+str(startCase.y_position)] = startCase
 
        while len(caseToVisit) > 0:
            currentCase = None
            for nextCase in caseToVisit:
                if currentCase == None or (noteFromStart[str(nextCase.x_position)+str(nextCase.y_position)]) > (noteFromStart[str(currentCase.x_position)+str(currentCase.y_position)]):
                    currentCase = nextCase
            if visitedCase != []:
                while cameFrom[str(currentCase.x_position)+str(currentCase.y_position)] != visitedCase[-1]:
                    if visitedCase[-1] in self.objectif:
                        list_objectives.append(visitedCase[-1])
                        caseToVisit.append(visitedCase[-1])
                        visitedCase.pop(-1)
 
            if currentCase == None:
                print('1 : Path does not exist!')
                return None

            if noteFromStart == noteMax or list_objectives == []:
                path = self.Reconstruct_path(currentCase, cameFrom, startCase)
                return path

            for neighboor in self.get_neighboors(currentCase, list_objectives):
                if neighboor not in caseToVisit and neighboor not in visitedCase:
                    caseToVisit.append(neighboor)
                    cameFrom[str(neighboor.x_position)+str(neighboor.y_position)] = currentCase
                    noteFromStart[str(neighboor.x_position)+str(neighboor.y_position)] = noteFromStart[str(currentCase.x_position)+str(currentCase.y_position)] + neighboor.note - self.Distance(currentCase, neighboor)

            caseToVisit.remove(currentCase)
            visitedCase.append(currentCase)
            if currentCase in list_objectives:
                list_objectives.remove(currentCase)

        print('2: Path does not exist!')
        return None

    def copy(self, list):
        new_list=[]
        for el in list:
            new_list.append(el)
        return new_list

    def get_neighboors(self, case, list_objectives):
        list_neighboors = {}
        for obj in list_objectives:
            list_neighboors[str(self.Distance(case,obj))] = obj
        neighboors_sorted = sorted(list_neighboors.items())
        if len(neighboors_sorted)<3:
            L=[]
            for i in range(len(neighboors_sorted)):
                L.append(neighboors_sorted[i][1])
            return L
        else: 
            return [neighboors_sorted[0][1], neighboors_sorted[1][1], neighboors_sorted[2][1]]

    def greedy_upgraded(self, note_moy):
        n=len(self.objectif)
        start_case = self.environnement.grid[self.x_position][self.y_position]
        list_objectives = self.copy(self.objectif)

            
        path=[start_case]
        note_path=start_case.note + n*note_moy

        cameFrom={}
        cameFrom[str(start_case.x_position)+str(start_case.y_position)]=(path,note_path,start_case.note)
            
        while list_objectives != []:
            note_max = list_objectives[0].note - self.Distance(path[-1], list_objectives[0])
            case_opti = list_objectives[0]
            isLessMoy=False
            for obj in list_objectives:
                note_obj = obj.note - self.Distance(path[-1], obj)
                if note_obj < note_moy:
                    if note_obj > note_max:
                        note_max=note_obj
                        case_opti=obj
                        isLessMoy=True
                    cameFrom[str(obj.x_position)+str(obj.y_position)]=(path,note_path, note_obj)
                if note_obj >= note_moy:
                    if note_obj > note_max:
                        note_max=note_obj
                        case_opti=obj
                        isLessMoy=False
                    cameFrom[str(obj.x_position)+str(obj.y_position)]=(path, note_path,  note_obj)

            if isLessMoy:
                key_chosen = str(case_opti.x_position)+str(case_opti.y_position)
                for key in cameFrom:
                    key_obj=self.environnement.grid[int(key[0])][int(key[1])]
                    if key_obj not in path and cameFrom[key][1]+cameFrom[key][2] > note_path + note_max:
                        key_chosen=key
                        note_max=cameFrom[key][2]
                (path,note_path,note_max)=cameFrom[key_chosen]
                list_objectives = self.copy(self.objectif)
                chosen_case = self.environnement.grid[int(key_chosen[0])][int(key_chosen[1])]
                path.append(chosen_case)
                note_path+=note_max - note_moy
                for el in path:
                    if el in list_objectives:
                        list_objectives.remove(el)
            else:
                path.append(case_opti)
                note_path+=note_max - note_moy
                list_objectives.remove(case_opti)
        return path
