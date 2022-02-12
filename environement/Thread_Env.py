import threading
from threading import *
from environement.CLI_Environnement import *
from environement.GUI_Environnement import *

class Thread_Env(Thread):

    def __init__(self, freq, proba, time_break):
        Thread.__init__(self)

    # Fonction lancée lorsque le thread est start()
    def run(self):
        threadLock = threading.Lock()
        # Get lock to synchronize threads
        threadLock.acquire()



        # Free lock to release next thread
        threadLock.release()
