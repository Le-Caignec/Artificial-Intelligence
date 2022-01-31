
from environement.environement import *

if __name__ == '__main__':
    fenetre = Tk()
    environement = Environement(fenetre, 0, 0, 0)
    environement.start()
    environement.fenetre.mainloop()

