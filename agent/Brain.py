from environement.CLI_Environnement import *
from time import *
from threading import *

class Brain(Thread):

    def __init__(self, freq, proba):
        Thread.__init__(self)
        self.freq = freq
        self.proba = proba

    #Fonction lancée lorsque le thread est start()
    def run(self):
        # cli_environnement = CLI_Environnement()
        # cli_environnement.GenerateNewGrid(self.proba)
        # cli_environnement.Afficher()
        # agent = Agent(0, 0, cli_environnement)
        # agent.AfficherAgent()
        # agent.plan_action = agent.AlgoNonInforme()
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
        #         sleep(5)
        #     c += 1
        #     sleep(5)
        print("j'avance")
