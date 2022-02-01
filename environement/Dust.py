from tkinter import *
from PIL import Image, ImageTk

class Dust:

    def __init__(self, fenetre, x_position, y_position):
        self.fenetre = fenetre
        self.x_position = x_position
        self.y_position = y_position

    def GUI_PutDust(self):
        image = Image.open('ressources/pierre.png').resize((50, 40), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label = Label(self.fenetre, image=photo)
        label.config(width=50, height=30)
        label.image = photo
        label.grid(row=self.x_position, column=self.y_position, sticky=SW, padx=18, pady=18)

    def AfficherDust(self):
        print("-----------DUST--------------")
        print("Position en X : " + str(self.x_position))
        print("Position en Y : " + str(self.y_position))
