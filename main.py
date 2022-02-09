#from environement.GUI_Environnement import *
from agent.Brain import *

if __name__ == '__main__':
    # Thread environement
    # GUI = GUI_Environnement()
    # GUI.start()
    # GUI.fenetre.mainloop()

    #Thread algorithme
    brain = Brain(freq=5, proba=1/5, time_break=3)
    brain.start()

