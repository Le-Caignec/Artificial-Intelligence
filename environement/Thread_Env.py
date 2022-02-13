import threading
from threading import *
from time import *

class Thread_Env(Thread):

    def __init__(self, compteur, proba, freq, GUI, agent, cli_environnement, time_break):
        Thread.__init__(self)
        self.cli_environnement = cli_environnement
        self.agent = agent
        self.GUI = GUI
        self.proba = proba
        self.freq = freq
        self.compteur = compteur
        self.time_break = time_break

    def SetCounteur(self, conteur):
        self.conteur = conteur

    # Fonction lancée lorsque le thread est start()
    def run(self):
        for k in range(3):
            threadLock = threading.Lock()
            # Get lock to synchronize threads
            threadLock.acquire()

            if self.compteur % self.freq == 0:
                self.cli_environnement.GenerateNewGrid(self.proba)
                self.GUI.GUI_Display_Grid()
            self.GUI.GUI_PutAgent(self.agent.x_position, self.agent.y_position)

            # Free lock to release next thread
            threadLock.release()
            # Temps d'attente entre les threads afin de mettre à jour l'intercade graphique
            sleep(self.time_break)
