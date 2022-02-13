from pydoc import cli
from environement.CLI_Environnement import *
from environement.GUI_Environnement import *
from time import *
from agent.Agent import *
from environement.Thread_Env import *
from agent.Thread_Agent import *
from agent.Brain import *

def Programme(freq, proba, time_break, x_pos_agent, y_pos_agent, sizeMentalState):
    #creation de l'environement pour l'agent
    cli_environnement = CLI_Environnement()
    cli_environnement.GenerateNewGrid(proba)
    print(cli_environnement.grid)

    #creation de l'agent
    agent = Agent(x_pos_agent, y_pos_agent, cli_environnement)

    # creation de l'interface graphique
    GUI = GUI_Environnement(cli_environnement)
    # GUI.GUI_PutAgent(agent.x_position, agent.y_position)
    # GUI.GUI_Display_Grid(cli_environnement.grid)
    # GUI.fenetre.mainloop()

    # Creation des Threads
    conteur = 1
    thread_Agent = Thread_Agent(agent, sizeMentalState)
    thread_Env = Thread_Env(conteur, proba, freq, GUI, agent, cli_environnement)

    for k in range(12):
        # Thread Agent
        #thread_Agent.start()
        
        thread_Agent.run()
        
        # Thread Environnement
        thread_Env.run()
        conteur += 1
        thread_Env.SetCounteur(conteur)

        # Temps d'attente entre les threads afin de mettre à jour l'intercade graphique
        sleep(time_break)


if __name__ == '__main__':
    ######### Variable Gloable ##########
    Probabilite = 1/3
    Frequence = 5
    Time_Break = 3
    X_Posistion_Agent = 0
    Y_Posistion_Agent = 0
    sizeMentalState = 1
    ###################################

    Programme(Frequence, Probabilite, Time_Break, X_Posistion_Agent, Y_Posistion_Agent, sizeMentalState)

    #Thread algorithme
    # brain = Brain(freq=5, proba=1/3, time_break=3)
    # brain.start()

