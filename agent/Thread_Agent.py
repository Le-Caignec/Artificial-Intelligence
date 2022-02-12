import threading
from threading import *

class Thread_Agent(Thread):

    def __init__(self, agent, sizeMentalState):
        Thread.__init__(self)
        self.agent = agent
        self.sizeMentalState = sizeMentalState

    #Fonction lancée lorsque le thread est start()
    def run(self):
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

        # Free lock to release next thread
        threadLock.release()


