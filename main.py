from environement.CLI_Environement import *
from time import *
from agent.Agent import *

def main(freq,proba):
    cli_environement = CLI_Environement()
    cli_environement.GenerateNewGrid(proba)
    cli_environement.Afficher()
    agent = Agent(0,0,cli_environement)
    agent.AfficherAgent()
    agent.plan_action = agent.algoNonInformé()
    c=1
    while True:
        print("--------------------PLAN ACTION---------------")
        print(agent.plan_action)
        agent.Deplacement()
        agent.AfficherAgent()
        agent.Action()       
        cli_environement.Afficher()
        if c%freq==0 :
            print(" --------------------NEW GRID--------------------")
            cli_environement.GenerateNewGrid(proba)
            cli_environement.Afficher()
            agent.objectif = agent.Search_Objective()
            agent.plan_action = agent.algoNonInformé()
            sleep(5)
        c+=1
        sleep(5)
    
    
if __name__ == '__main__':
    main(freq=5,proba=1/10)
