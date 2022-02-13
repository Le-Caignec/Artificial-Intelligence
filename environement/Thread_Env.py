import threading
from threading import *


class Thread_Env(Thread):

    def __init__(self, conteur, proba, freq, GUI, agent, cli_environnement):
        Thread.__init__(self)
        self.cli_environnement = cli_environnement
        self.agent = agent
        self.GUI = GUI
        self.proba = proba
        self.freq = freq
        self.conteur = conteur

    def SetCounteur(self, conteur):
        self.conteur = conteur

    # Fonction lancée lorsque le thread est start()
    def run(self):
        threadLock = threading.Lock()
        # Get lock to synchronize threads
        threadLock.acquire()

        if self.conteur % self.freq == 0:
            self.cli_environnement.GenerateNewGrid(self.proba)
            self.cli_environnement.Afficher()
        self.GUI.GUI_PutAgent(self.agent.x_position, self.agent.y_position)
        self.GUI.GUI_Display_Grid(self.cli_environnement.grid)

        # Free lock to release next thread
        threadLock.release()
