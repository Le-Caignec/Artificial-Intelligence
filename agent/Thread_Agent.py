import threading
from threading import *
from time import *

class Thread_Agent(Thread):

    def __init__(self, agent, time_break):
        Thread.__init__(self)
        self.agent = agent
        self.time_break = time_break

    #Fonction lancée lorsque le thread est start()
    def run(self):
        for k in range(3):
            if k != 0:
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
                # Temps d'attente entre les threads afin de mettre à jour l'intercade graphique
            sleep(self.time_break)



