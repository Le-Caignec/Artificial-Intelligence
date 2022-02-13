from threading import *
from tkinter import *
from PIL import Image, ImageTk


class GUI_Environnement(Thread):

    def __init__(self, cli_environnement):
        self.fenetre = Tk()
        self.cli_environnement = cli_environnement
        self.label_agent = None
        self.photo_diamond, self.photo_dust, self.label_agent = None, None, None
        self.gui_grid = [[0 for k in range(5)]for k in range(5)]
        self.Creat_GUI()
        self.collected_diamond_label, self.aspirated_dust_label, self.aspirated_diamond_label = self.Score()

    def Creat_GUI(self):
        self.CreatFenetre()
        self.LoadImage()
        self.CreatGrid()
        self.label_agent = self.Creat_Agent_GUI()

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

    def LoadImage(self):
        # Creation de l'objet image Diamond
        image_diamond = Image.open('ressources/diamant.png').resize((60, 45), Image.ANTIALIAS)
        self.photo_diamond = ImageTk.PhotoImage(image_diamond)

        # Creation de l'objet image Dust
        image_dust = Image.open('ressources/pierre.png').resize((50, 40), Image.ANTIALIAS)
        self.photo_dust = ImageTk.PhotoImage(image_dust)

    def Creat_Agent_GUI(self):
        # Creation de l'objet image Agent
        image_agent = Image.open("ressources/agent.png").resize((50, 50), Image.ANTIALIAS)
        photo_agent = ImageTk.PhotoImage(image_agent)
        label_agent = Label(self.fenetre, image=photo_agent)
        label_agent.config(width=50, height=50)
        label_agent.image = photo_agent
        return label_agent

    def CreatGrid(self):
        for row in range(3, 8):
            for column in range(5):
                Frame(self.fenetre, width=200, height=120, borderwidth=2, relief=GROOVE).grid(row=row, column=column)
                label_dust = self.GUI_PutDust(column, row)
                label_diamond = self.GUI_PutDiamond(column, row)
                self.gui_grid[column][row-3] = [label_diamond, label_dust]
                label_dust.grid_remove()
                label_diamond.grid_remove()

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
        label_diamond = Label(self.fenetre, image=self.photo_diamond)
        label_diamond.config(width=50, height=30)
        label_diamond.image = self.photo_diamond
        label_diamond.grid(row=y_position, column=x_position, sticky=NW, padx=2, pady=8)
        return label_diamond

    def GUI_PutDust(self, x_position, y_position):
        label_dust = Label(self.fenetre, image=self.photo_dust)
        label_dust.config(width=50, height=30)
        label_dust.image = self.photo_dust
        label_dust.grid(row=y_position, column=x_position, sticky=SW, padx=18, pady=18)
        return label_dust

    def GUI_PutAgent(self, x_position, y_position):
        self.label_agent.grid(row=y_position+3, column=x_position, sticky=E, padx=10)

    def GUI_Display_Grid(self):
        for x in range(5):
            for y in range(5):
                if self.cli_environnement.grid[x][y].diamond:
                    self.gui_grid[x][y][0].grid()
                if self.cli_environnement.grid[x][y].dust:
                    self.gui_grid[x][y][1].grid()

    def GUI_Clear(self):
        for x in range(5):
            for y in range(5):
                self.gui_grid[x][y][0].grid_remove()
                self.gui_grid[x][y][1].grid_remove()

    def GUI_Clear_Case(self, x, y):
        self.gui_grid[x][y][0].grid_remove()
        self.gui_grid[x][y][1].grid_remove()

