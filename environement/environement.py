##VARIABLE GLOBALE
from time import sleep
from tkinter import *
from PIL import Image,ImageTk
from threading import *
from random import uniform, randint


class Environement(Thread):

    def __init__(self, fenetre,collected_diamond, aspirated_dust, aspirated_diamond):
        Thread.__init__(self)
        self.collected_diamond = collected_diamond
        self.aspirated_dust = aspirated_dust
        self.aspirated_diamond = aspirated_diamond

        self.fenetre = fenetre
        self.CreatFenetre()
        self.CenterFenetre()
        self.CreatGrid()
        self.DrawScore()

    def CreatFenetre(self):
        self.fenetre.title('Artificial Intelligence')
        self.fenetre.geometry('1000x672')

    def CenterFenetre(self):
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

    def DrawScore(self):
        Label(self.fenetre, text="Collected Diamond : "+str(self.collected_diamond), fg='#043AFF').grid(row=0, column=0, columnspan=5, sticky=NW)
        Label(self.fenetre, text="Aspirated Dust : "+str(self.aspirated_dust), fg='#043AFF').grid(row=1, column=0, columnspan=5, sticky=NW)
        Label(self.fenetre, text="Aspirated Diamond : "+str(self.aspirated_diamond), fg='#043AFF').grid(row=2, column=0, columnspan=5, sticky=NW)

    #Fonction lancée lorsque le thread est start()
    def run(self):
        self.PutAgent(randint(3, 7), randint(0, 4))
        for row in range(3, 8):
            for column in range(5):
                if uniform(0, 3) <= 1:
                    self.PutDiamant(row, column)
                if uniform(0, 3) <= 1:
                    self.PutPierre(row, column)

    def PutDiamant(self, row, column):
        image = Image.open('ressources/diamant.png').resize((60, 45), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label = Label(self.fenetre, image=photo)
        label.config(width=50, height=30)
        label.image = photo
        label.grid(row=row, column=column, sticky=NW, padx=2, pady=8)

    def PutPierre(self, row, column):
        image = Image.open('ressources/pierre.png').resize((50, 40), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label = Label(self.fenetre, image=photo)
        label.config(width=50, height=30)
        label.image = photo
        label.grid(row=row, column=column, sticky=SW, padx=18, pady=18)


    def PutAgent(self, row, column):
        image = Image.open('ressources/agent.png').resize((50, 50), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label = Label(self.fenetre, image=photo)
        label.config(width=50, height=50)
        label.image = photo
        label.grid(row=row, column=column, sticky=E, padx=10)
