from agent.Agent import Agent
from time import *
import threading
from threading import *

class Thread_Agent(Thread):

    def __init__(self, freq, proba, time_break):
        Thread.__init__(self)
        self.freq = freq
        self.proba = proba
        self.time_break = time_break

    #Fonction lancée lorsque le thread est start()
    def run(self):
        threadLock = threading.Lock()
        # Get lock to synchronize threads
        threadLock.acquire()

        agent.plan_action = agent.AlgoNonInforme()
        print("--------------------PLAN ACTION NON INFORME---------------")
        print(agent.plan_action)
        print("Nombre de case avec quelque chose : ", len(agent.plan_action))
        # c = 1
        # while True:
        #     print("--------------------PLAN ACTION---------------")
        #     print(agent.plan_action)
        #     agent.Deplacement()
        #     agent.AfficherAgent()
        #     agent.Action()
        #     cli_environnement.Afficher()
        #     if c % self.freq == 0:
        #         print(" --------------------NEW GRID--------------------")
        #         cli_environnement.GenerateNewGrid(self.proba)
        #         cli_environnement.Afficher()
        #         agent.objectif = agent.Search_Objective()
        #         agent.plan_action = agent.AlgoNonInforme()
        #         sleep(self.time_break)
        #     c += 1
        #     sleep(5)

        # Free lock to release next thread
        threadLock.release()


