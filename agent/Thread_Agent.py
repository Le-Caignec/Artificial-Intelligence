import threading
from threading import *
from time import *

class Thread_Agent(Thread):

    def __init__(self, agent, time_break):
        Thread.__init__(self)
        self.agent = agent
        self.time_break = time_break
        self.bool = False
        self.sizeMentalState = sizeMentalState

    #Fonction lancée lorsque le thread est start()
    def run(self):
        while True:
            if self.bool:
                threadLock = threading.Lock()
                # Get lock to synchronize threads
                threadLock.acquire()
        threadLock = threading.Lock()
        # Get lock to synchronize threads
        threadLock.acquire()
        #check if the environnment changed <=> self.agent.objectif == self.agent.Search_Objective() 
        # if self.captor.isNewEnvironnment:
        if self.agent.objectif != self.agent.Search_Objective():
            self.agent.objectif = self.agent.Search_Objective()
            self.agent.Action()
            self.agent.plan_action = self.agent.ChoiceAlgo(self.sizeMentalState)
            self.agent.UpdateMentalState()
            self.agent.Deplacement()
            self.agent.Action()
        else:
            self.agent.Deplacement()
            self.agent.Action()

                self.agent.objectif = self.agent.Search_Objective()
                self.agent.plan_action = self.agent.AlgoNonInforme()
                self.agent.Action()
                self.agent.Deplacement()
                self.agent.Action()

                # Free lock to release next thread
                threadLock.release()
                # Temps d'attente entre les threads afin de mettre à jour l'intercade graphique
            self.bool = True
            sleep(self.time_break)



