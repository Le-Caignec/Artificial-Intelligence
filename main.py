from environement.Thread_Env import *
from agent.Thread_Agent import *
from environement.CLI_Environnement import *
from environement.GUI_Environnement import *
from time import *

def Programme(freq, proba, time_break, x_pos_agent, y_pos_agent):
    #creation de l'environement pour l'agent
    cli_environnement = CLI_Environnement()
    cli_environnement.GenerateNewGrid(proba)

    #creation de l'agent
    agent = Agent(x_pos_agent, y_pos_agent, cli_environnement)

    #creation de l'interface graphique
    GUI = GUI_Environnement(cli_environnement)
    GUI.GUI_PutAgent(agent.x_position, agent.y_position)
    GUI.GUI_Display_Grid()
    GUI.fenetre.mainloop()

    # Creation des Threads
    Thread_Env = Thread_Env(proba, freq, GUI, agent, cli_environnement)
    Thread_Agent = Thread_Agent(agent)

    c = 1
    while True:
        # Thread Agent
        Thread_Agent.start()

        # Thread Environnement
        Thread_Env.start(c)
        c += 1

        # Temps d'attente entre les threads afin de mettre à jour l'intercade graphique
        sleep(time_break)


if __name__ == '__main__':
    ######### Variable Gloable ##########
    Probabilite = 1/5
    Frequence = 5
    Time_Break = 3
    X_Posistion_Agent = 0
    Y_Posistion_Agent = 0
    ###################################

    Programme(Probabilite, Frequence, Time_Break, X_Posistion_Agent, Y_Posistion_Agent)


