import threading
from threading import *


class Thread_Env(Thread):

    def __init__(self, proba, freq, GUI, agent, cli_environnement):
        Thread.__init__(self)
        self.cli_environnement = self.cli_environnement
        self.agent = self.agent
        self.GUI = self.GUI
        self.proba = proba
        self.freq = self.freq

    # Fonction lancée lorsque le thread est start()
    def run(self, c):
        threadLock = threading.Lock()
        # Get lock to synchronize threads
        threadLock.acquire()

        if c % self.freq == 0:
            self.cli_environnement.GenerateNewGrid(self.proba)
        self.GUI.GUI_PutAgent(self.agent.x_position, self.agent.y_position)
        self.GUI.GUI_Display_Grid()

        # Free lock to release next thread
        threadLock.release()
