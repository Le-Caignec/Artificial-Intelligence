from threading import *
from tkinter import *
from PIL import Image, ImageTk


class GUI_Environnement(Thread):

    def __init__(self):
        Thread.__init__(self)
        #score label
        #self.collected_diamond_label, self.aspirated_dust_label, self.aspirated_diamond_label = self.Score()
        #GUI
        self.fenetre = Tk()
        self.Creat_GUI()

    def Creat_GUI(self):
        self.CreatFenetre()
        self.CreatGrid()
        #self.Score()

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
        for row in range(3, 8):
            for column in range(5):
                Frame(self.fenetre, width=200, height=120, borderwidth=2, relief=GROOVE).grid(row=row, column=column)

    def Score(self):
        #Collected Diamond
        collected_diamond = Label(self.fenetre, text="Collected Diamond : 0", fg='#043AFF')
        collected_diamond.grid(row=0, column=0, columnspan=5, sticky=NW)
        #Aspirated Dust
        aspirated_dust = Label(self.fenetre, text="Aspirated Dust : 0", fg='#043AFF')
        aspirated_dust.grid(row=1, column=0, columnspan=5, sticky=NW)
        #Aspirated Diamond
        aspirated_diamond = Label(self.fenetre, text="Aspirated Diamond : 0", fg='#043AFF')
        aspirated_diamond.grid(row=2, column=0, columnspan=5, sticky=NW)
        return collected_diamond, aspirated_dust, aspirated_diamond
    
    def UpdateScore(self, collected_diamond, aspirated_dust, aspirated_diamond):
        self.collected_diamond_label = collected_diamond
        self.aspirated_dust_label = aspirated_dust
        self.aspirated_diamond_label = aspirated_diamond

    def GUI_PutDiamond(self, x_position, y_position):
        image = Image.open('ressources/diamant.png').resize((60, 45), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label = Label(self.fenetre, image=photo)
        label.config(width=50, height=30)
        label.image = photo
        label.grid(row=x_position+3, column=y_position, sticky=NW, padx=2, pady=8)

    def GUI_PutDust(self, x_position, y_position):
        image = Image.open('ressources/pierre.png').resize((50, 40), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label = Label(self.fenetre, image=photo)
        label.config(width=50, height=30)
        label.image = photo
        label.grid(row=x_position+3, column=y_position, sticky=SW, padx=18, pady=18)

    def GUI_PutAgent(self, x_position, y_position):
        image = Image.open("ressources/agent.png").resize((50, 50), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label = Label(self.fenetre, image=photo)
        label.config(width=50, height=50)
        label.image = photo
        label.grid(row=x_position+3, column=y_position, sticky=E, padx=10)

    #Fonction lancée lorsque le thread est start()
    def run(self):
        print("je dessine mon interface")
        #self.GUI_PutAgent(0, 0)
        #self.GUI_PutDiamond(0, 0)
        #self.GUI_PutDust(0, 0)


