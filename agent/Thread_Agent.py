import threading
from threading import *

class Thread_Agent(Thread):

    def __init__(self, agent):
        Thread.__init__(self)
        self.agent = agent

    #Fonction lancée lorsque le thread est start()
    def run(self):
        threadLock = threading.Lock()
        # Get lock to synchronize threads
        threadLock.acquire()

        self.agent.objectif = self.agent.Search_Objective()
        self.agent.plan_action = self.agent.AlgoNonInforme()
        self.agent.Action()
        self.agent.Deplacement()
        self.agent.Action()

        # Free lock to release next thread
        threadLock.release()


