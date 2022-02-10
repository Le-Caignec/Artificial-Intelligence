from agent.Agent import Agent
from environement.CLI_Environnement import *
from time import *
from threading import *

class Brain(Thread):

    def __init__(self, freq, proba, time_break):
        Thread.__init__(self)
        self.freq = freq
        self.proba = proba
        self.time_break = time_break

    #Fonction lancée lorsque le thread est start()
    def run(self):
        # print("j'avance")
        cli_environnement = CLI_Environnement()
        cli_environnement.GenerateNewGrid(self.proba)
        cli_environnement.Afficher()
        agent = Agent(0, 0, cli_environnement)
        agent.AfficherAgent()
        agent.plan_action = agent.AlgoNonInforme()
        print("--------------------PLAN ACTION NON INFORME---------------")
        print(agent.plan_action)
        print("--------------------PLAN ACTION INFORME---------------")
        agent.plan_action = agent.AlgoInforme()
        print(agent.AlgoInforme())
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
