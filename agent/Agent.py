from tkinter import *
from PIL import ImageTk, Image

class Agent:

    def __init__(self, fenetre, x_position, y_position):
        self.fenetre = fenetre
        self.x_position = x_position
        self.y_position = y_position

    def GUI_PutAgent(self):
        image = Image.open("ressources/agent.png").resize((50, 50), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label = Label(self.fenetre, image=photo)
        label.config(width=50, height=50)
        label.image = photo
        label.grid(row=self.x_position+3, column=self.y_position, sticky=E, padx=10)


