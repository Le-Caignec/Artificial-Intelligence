from environement.CLI_Environnement import *
from environement.GUI_Environnement import *
from agent.Thread_Agent import *
from time import *

def Programme(freq, proba, time_break, x_pos_agent, y_pos_agent):
    #creation de l'environement pour l'agent
    cli_environnement = CLI_Environnement()
    cli_environnement.GenerateNewGrid(proba)

    #creation de l'agent
    agent = Agent(x_pos_agent, y_pos_agent, cli_environnement)

    #creation de l'interface graphique
    GUI = GUI_Environnement()
    GUI.GUI_PutAgent(agent.x_position, agent.y_position)

    GUI.fenetre.mainloop()

    while True:
        # Thread environement
        Thread_Env = Thread_Env()
        Thread_Env.start()

        # Temps d'attente entre les threads afin de mettre à jour l'intercade graphique
        sleep(5)

        #Thread Agent
        Thread_Agent = Thread_Agent(freq, proba, time_break)
        Thread_Agent.start()


if __name__ == '__main__':
    ######### Variable Gloable ##########
    Probabilite = 1/5
    Frequence = 5
    Time_Break = 3
    X_Posistion_Agent = 0
    Y_Posistion_Agent = 0
    ###################################

    Programme(Probabilite, Frequence, Time_Break, X_Posistion_Agent, Y_Posistion_Agent)


