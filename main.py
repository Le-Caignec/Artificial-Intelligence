
from environement.GUI_Environement import *


if __name__ == '__main__':
    fenetre = Tk()
    environement = GUI_Environement(fenetre)
    environement.start()
    environement.fenetre.mainloop()
