from dataclasses import dataclass
from agent.Captor import *

@dataclass
class Score:
    collected_diamond: int = 0
    aspirated_dust: int = 0
    aspirated_diamond: int = 0

class Agent:

    def __init__(self, x_position, y_position, environnement):
        self.x_position = x_position
        self.y_position = y_position
        self.mentalState = []
        self.note_moy = 0
        self.plan_action = []
        self.environnement = environnement
        self.score = Score()
        self.objectif = self.Search_Objective()
        self.captor = Captor(environnement)

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
            print("--------Je me déplace---------")
            print("ma position est : x = " + str(self.x_position) + " et y = " + str(self.y_position))
            case_objectif = self.plan_action[0]
            bool = False
            #l'agent se déplace d'une case à chaque appel de Deplacement()
            #l'agent se déplace d'abord suivant les colonnes puis les lignes 
            if self.x_position < case_objectif.x_position:
                self.x_position += 1
                bool = True
            elif self.x_position > case_objectif.x_position:
                self.x_position -= 1
                bool = True
            else:
                if self.y_position < case_objectif.y_position:
                    self.y_position += 1
                    bool = True
                elif self.y_position > case_objectif.y_position:
                    self.y_position -= 1
                    bool = True
            if bool:
                print("j'avance !")
            else:
                print("je reste dans ma case")
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
        list_objectives = self.copy(self.objectif)
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

    def copy(self, list):
        new_list = []
        for el in list:
            new_list.append(el)
        return new_list

    def greedy_upgraded(self):
        #initialisation
        n = len(self.objectif)
        start_case = self.environnement.grid[self.x_position][self.y_position]
        list_objectives = self.copy(self.objectif)

        #creation of the path with the start case at path[0]
        #it is known that there is nothing on the start case
        path = [start_case]
        note_path = start_case.note + n*self.note_moy

        # Dict is a dictionary that keep the note of old path that could be better than the actual path we are taking
        Dict = {}
        Dict[str(start_case.x_position)+str(start_case.y_position)] = (path, note_path, start_case.note)
        

        # we execute this programm until all the interesting case are visited
        while list_objectives != []:
            # the note is calculated with the case note minus the Distance beetween where the agent is and the case
            note_max = list_objectives[0].note - self.Distance(path[-1], list_objectives[0])
            case_opti = list_objectives[0]
            isLessMoy = False
            for obj in list_objectives:
                note_obj = obj.note - self.Distance(path[-1], obj)
                # we check if the note is less than the average note
                if note_obj < self.note_moy:
                    # we actualise the obj only if he has a better note than the actual case
                    if note_obj > note_max:
                        note_max = note_obj
                        case_opti = obj
                        isLessMoy = True
                    Dict[str(obj.x_position)+str(obj.y_position)] = (path, note_path, note_obj)
                if note_obj >= self.note_moy:
                    if note_obj > note_max:
                        note_max = note_obj
                        case_opti = obj
                        isLessMoy = False
                    Dict[str(obj.x_position)+str(obj.y_position)] = (path, note_path,  note_obj)
            
            # if isLessMoy is True, then the maximal note is inferior to the average note the heuristic has calculated
            # In this case, the agent know he may have made a mistake before and check if there is a potentiel other path
            # it is possible that after considering another path he come back to this one because he is the less wrong
            if isLessMoy:
                # we begin with our path so that if nobody has a better note we keep on following the same path
                key_chosen = str(case_opti.x_position)+str(case_opti.y_position)
                for key in Dict:
                    key_obj = self.environnement.grid[int(key[0])][int(key[1])]
                    # we need to check that the case is not already in the path because it means it is the same path
                    # Dict[key][1] is the note_path of the corresponding key
                    # Dict[key][] is the note_max of the corresponding key (it means the note of the case we are considering - the distance)
                    if key_obj not in path and Dict[key][1]+Dict[key][2] > note_path + note_max:
                        key_chosen = key
                        note_max = Dict[key][2]
                (path, note_path, note_max) = Dict[key_chosen]
                # here we just recreate teh list-objectives because we possibly have chenged the path 
                # So there may be objectives that we had visited and that we do not anymore so they have to be add to the list
                # to do so we just remove from a new copy of self.objectif all the objectives that are in the new path
                list_objectives = self.copy(self.objectif)
                chosen_case = self.environnement.grid[int(key_chosen[0])][int(key_chosen[1])]
                path.append(chosen_case)
                note_path += note_max - self.note_moy
                for el in path:
                    if el in list_objectives:
                        list_objectives.remove(el)
            # if isLessMoy is False then we overestimated the average note so we are on the good path for now
            # if the average note is always too low, the heuristic will balanced it after the final path is calculated
            # and the greedy_upgraded will be more accurate
            else:
                path.append(case_opti)
                note_path += note_max - self.note_moy
                list_objectives.remove(case_opti)
        path.pop(0)
        return path

    # this function choose beetwen the informed algorythm and the non informed alogorythm
    # it depends on the size of the mental state and the size asked when the thread is starting
    def ChoiceAlgo(self, sizeMentalState):
        if len(self.mentalState) < sizeMentalState:
            path = self.AlgoNonInforme()
            print("----------------ALGO NON INFORME-----------------------")
        else:
            print("-------------------ALGO INFORME------------------------")
            path = self.greedy_upgraded()
            print(path)
            print(self.note_moy)
        return path
    
    # when a new path is calculated, we update the mentale state with a new average note
    def UpdateMentalState(self):
        self.mentalState.append((len(self.plan_action)-1, self.EvalPath(self.plan_action)))
        self.updateNoteMoy()
    
    # this function calculated the average note of the path
    def EvalPath(self, path):
        startcase = path[0]
        n = len(path)
        noteMoy = 0
        for obj in path:
            if obj != startcase:
                noteMoy += obj.note - self.Distance(startcase, obj)
        noteMoy = noteMoy / (n-1)
        return noteMoy
    
    #this function just re calculate the global average note
    def updateNoteMoy(self):
        note = 0
        n = 0
        for tuple in self.mentalState:
            note += tuple[0]*tuple[1]
            n += tuple[0]
        self.note_moy = note/n
        print("-----------------NOTE UPGRADED-------------------")
        print("la nouvelle note est : " + str(self.note_moy))
