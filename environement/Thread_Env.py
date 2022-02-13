import threading
from threading import *
from time import *

class Thread_Env(Thread):

    def __init__(self, proba, freq, GUI, agent, cli_environnement, time_break):
        Thread.__init__(self)
        self.cli_environnement = cli_environnement
        self.agent = agent
        self.GUI = GUI
        self.proba = proba
        self.freq = freq
        self.compteur = 1
        self.time_break = time_break

    # Fonction lancée lorsque le thread est start()
    def run(self):
        while True:
            # Get lock to synchronize threads
            threadLock = threading.Lock()
            threadLock.acquire()

            if self.compteur % self.freq == 0:
                self.cli_environnement.GenerateNewGrid(self.proba)
                self.cli_environnement.Afficher()
                self.GUI.GUI_Clear()
                self.GUI.GUI_Display_Grid()
            self.GUI.GUI_Clear_Case(self.agent.x_position, self.agent.y_position)
            self.GUI.GUI_PutAgent(self.agent.x_position, self.agent.y_position)
            print(self.agent.x_position, self.agent.y_position)
            self.compteur += 1

            # Free lock to release next thread
            threadLock.release()

            # Temps d'attente entre les threads afin de mettre à jour l'interface graphique
            sleep(self.time_break)
