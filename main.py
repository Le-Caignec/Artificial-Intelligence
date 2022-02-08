from environement.GUI_Environnement import *
from agent.Agent import *
from agent.Brain import *

if __name__ == '__main__':
    # Thread environement
    GUI = GUI_Environnement()
    GUI.start()
    GUI.fenetre.mainloop()

    #Thread algorithme
    brain = Brain(5, 1/10)
    Brain.start()

