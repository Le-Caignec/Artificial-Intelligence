from environement.CLI_Environement import *
from time import *

def main(freq):
    cli_environement = CLI_Environement()
    cli_environement.GenerateNewGrid()
    cli_environement.Afficher()
    agent = Agent(0,0,cli_environement)
    agent.AfficherAgent()
    c=0
    for i in range (8):
        agent.vie()
        # if c%freq==0 :
            # cli_environement.GenerateNewGrid()
        c+=1
        cli_environement.Afficher()
    
    
if __name__ == '__main__':
    main(freq=5)
