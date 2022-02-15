from environement.CLI_Environment import *
from environement.GUI_Environment import *
from agent.Agent import *
from environement.Thread_Env import *
from agent.Thread_Agent import *

def Programme(freq, proba, time_break, x_pos_agent, y_pos_agent, x):
    #creation of the environment for the agent
    cli_environment = CLI_Environment()
    cli_environment.GenerateNewGrid(proba)
    cli_environment.DisplayGrid()

    #agent creation
    agent = Agent(x_pos_agent, y_pos_agent, cli_environment)
    agent.Action()

    #creation of the graphical interface
    GUI = GUI_Environment(cli_environment)
    GUI.GUI_Display_Grid()
    GUI.GUI_PutAgent(agent.x_position, agent.y_position)

    #Thread Environment
    thread_Env = Thread_Env(proba, freq, GUI, agent, cli_environment, time_break)
    thread_Env.start()

    #Thread Agent
    thread_Agent = Thread_Agent(agent, time_break, sizeMentalState)
    thread_Agent.start()

    GUI.fenetre.mainloop()


if __name__ == '__main__':
    ######### Gloable variable ##########
    Probability = 1/10
    Frequency = 10
    Time_Break = 0.5
    X_Position_Agent = 0
    Y_Position_Agent = 0
    sizeMentalState = 10
    ###################################

    Programme(Frequency, Probability, Time_Break, X_Position_Agent, Y_Position_Agent, sizeMentalState)
