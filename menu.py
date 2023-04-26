import customtkinter as ctk


class Menu(ctk.CTkTabview):
    def __init__(self, parent):
        super().__init__(master=parent)
        self.grid(row=0, column=0, sticky='nsew')

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
        
class ColorFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color= 'transparent')
        self.pack(expand = True, fill = 'both')
