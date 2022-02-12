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
        # print("--------------------PLAN ACTION NON INFORME---------------")
        # print(agent.plan_action)
        # print("Nombre de case avec quelque chose : ", len(agent.plan_action))
        # print("--------------------PLAN ACTION INFORME---------------")
        # print("GOAL : ", agent.plan_action[-1])
        # print(agent.AlgoInforme())
        # print("Nombre de case avec quelque chose : ", test_algo_informe(agent.AlgoInforme()))
        # print("Case avec des objects non visitée : ", diff_plan_action(agent.AlgoInforme()))
        path = agent.greedy_upgraded(12)
        print(path)
        print(len(path))





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

def test_algo_informe(plan_action):
    count = 0
    for case in plan_action:
        if case.note > 0:
            count += 1
    return count

def diff_plan_action(list_informe, list_non_informe):
    L=[]
    for case in list_non_informe:
        if case not in list_informe:
            L.append(case)
    return L

