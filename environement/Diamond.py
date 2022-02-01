from tkinter import *
from PIL import Image, ImageTk

class Diamond:

    def __init__(self, x_position, y_position):
        self.x_position = x_position
        self.y_position = y_position

    def AfficherDiamond(self):
        print("-----------DIAMOND--------------")
        print("Position en X : "+str(self.x_position))
        print("Position en Y : "+str(self.y_position))
