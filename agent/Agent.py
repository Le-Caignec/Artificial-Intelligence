from tkinter import *
from PIL import ImageTk, Image
from agent import Captor
from environement import CLI_Environement

class Agent:

    def __init__(self, x_position, y_position):
        self.x_position = x_position
        self.y_position = y_position

    def AfficherAgent(self):
        print("AGENT")

    def algoNonInformé(self):

        plan_action = []

        return plan_action