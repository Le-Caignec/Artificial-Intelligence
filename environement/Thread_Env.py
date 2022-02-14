import threading
from threading import *
from time import *

class Thread_Env(Thread):

    def __init__(self, proba, freq, GUI, agent, cli_environment, time_break):
        Thread.__init__(self)
        self.cli_environment = cli_environment
        self.agent = agent
        self.GUI = GUI
        self.proba = proba
        self.freq = freq
        self.compteur = 1
        self.time_break = time_break

    #Function that is run when the Thread Environment is start
    def run(self):
        while True:
            # Get lock to synchronize threads
            threadLock = threading.Lock()
            threadLock.acquire()

            if self.compteur % self.freq == 0:
                self.cli_environment.GenerateNewGrid(self.proba)
                self.cli_environment.DisplayGrid()
                self.GUI.GUI_Clear()
                self.GUI.GUI_Display_Grid()
            self.GUI.GUI_Clear_Case(self.agent.x_position, self.agent.y_position)
            self.GUI.GUI_PutAgent(self.agent.x_position, self.agent.y_position)
            self.GUI.UpdateScore(self.agent.score.collected_diamond, self.agent.score.aspirated_dust, self.agent.score.aspirated_diamond)
            self.compteur += 1

            # Free lock to release next thread
            threadLock.release()

            # Wait time between threads to update GUI
            sleep(self.time_break)
