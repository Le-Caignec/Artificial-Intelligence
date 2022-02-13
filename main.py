from environement.CLI_Environnement import *
from environement.GUI_Environnement import *
from agent.Agent import *
from environement.Thread_Env import *
from agent.Thread_Agent import *

def Programme(freq, proba, time_break, x_pos_agent, y_pos_agent, sizeMentalState):
    #creation de l'environement pour l'agent
    cli_environnement = CLI_Environnement()
    cli_environnement.GenerateNewGrid(proba)
    cli_environnement.Afficher()

    #creation de l'agent
    agent = Agent(x_pos_agent, y_pos_agent, cli_environnement)
    agent.Action()

    #creation de l'interface graphique
    GUI = GUI_Environnement(cli_environnement)
    GUI.GUI_Display_Grid()
    GUI.GUI_PutAgent(agent.x_position, agent.y_position)

    # Thread Agent
    thread_Agent = Thread_Agent(agent, time_break, sizeMentalState)
    thread_Agent.start()

    # Thread Environnement
    thread_Env = Thread_Env(proba, freq, GUI, agent, cli_environnement, time_break)
    thread_Env.start()

    GUI.fenetre.mainloop()


if __name__ == '__main__':
    ######### Variable Gloable ##########
    Probabilite = 1/3
    Frequence = 5
    Time_Break = 2
    X_Posistion_Agent = 0
    Y_Posistion_Agent = 0
    sizeMentalState = 1
    ###################################

    Programme(Frequence, Probabilite, Time_Break, X_Posistion_Agent, Y_Posistion_Agent, sizeMentalState)


