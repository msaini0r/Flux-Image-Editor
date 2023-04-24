import customtkinter as ctk
 
class ImageImport(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master = parent)
        self.grid(column = 0, columnspan = 2, row = 0, sticky = 'nsew')
        
        ctk.CTkButton(self, text = 'Open Image').pack(expand = True)