import customtkinter as ctk
from panels import *

class Menu(ctk.CTkTabview):
    def __init__(self, parent):
        super().__init__(master=parent)
        self.grid(row = 0, column = 0, sticky = 'nsew', pady = 10, padx = 10)

        # tabs
        self.add('Position')
        self.add('Color')
        self.add('Effects')
        self.add('Export')
        
        #widgets
        PositionFrame(self.tab('Position'))
        ColorFrame(self.tab('Color'))

class PositionFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color= 'transparent')
        self.pack(expand = True, fill = 'both')
        
        SliderPanel(self, 'Rotation')
        SliderPanel(self, 'Zoom')
        
class ColorFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color= 'transparent')
        self.pack(expand = True, fill = 'both')
