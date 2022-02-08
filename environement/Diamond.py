from tkinter import *
from PIL import Image, ImageTk

class Diamond:

    def __init__(self, fenetre, x_position, y_position):
        self.fenetre = fenetre
        self.x_position = x_position
        self.y_position = y_position

    def GUI_PutDiamond(self):
        image = Image.open('ressources/diamant.png').resize((60, 45), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label = Label(self.fenetre, image=photo)
        label.config(width=50, height=30)
        label.image = photo
        label.grid(row=self.x_position+3, column=self.y_position, sticky=NW, padx=2, pady=8)

    def AfficherDiamond(self):
        print("-----------DIAMOND--------------")
        print("Position en X : "+str(self.x_position))
        print("Position en Y : "+str(self.y_position))
