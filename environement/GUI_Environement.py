from tkinter import *
from threading import *


class GUI_Environement(Thread):

    def __init__(self, fenetre):
        Thread.__init__(self)
        self.collected_diamond = 0
        self.aspirated_dust = 0
        self.aspirated_diamond = 0
        self.fenetre = fenetre
        self.CreatFenetre()
        self.CreatGrid()
        self.Score()

    def CreatFenetre(self):
        self.fenetre.title('Artificial Intelligence')
        self.fenetre.geometry('1000x672')
        win = self.fenetre.winfo_toplevel()
        win.update_idletasks()
        width = win.winfo_width()
        height = win.winfo_height()
        x = (win.winfo_screenwidth() // 2) - (width // 2)
        y = (win.winfo_screenheight() // 2) - (height // 2)
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def CreatGrid(self):
        for ligne in range(3, 8):
            for colonne in range(5):
                Frame(self.fenetre, width=200, height=120, borderwidth=2, relief=GROOVE).grid(row=ligne, column=colonne)

    def Score(self):
        Label(self.fenetre, text="Collected Diamond : "+str(self.collected_diamond), fg='#043AFF').grid(row=0, column=0, columnspan=5, sticky=NW)
        Label(self.fenetre, text="Aspirated Dust : "+str(self.aspirated_dust), fg='#043AFF').grid(row=1, column=0, columnspan=5, sticky=NW)
        Label(self.fenetre, text="Aspirated Diamond : "+str(self.aspirated_diamond), fg='#043AFF').grid(row=2, column=0, columnspan=5, sticky=NW)

    #Fonction lancée lorsque le thread est start()
    def run(self):
        print("ici la fonction lancé lors du thread")


