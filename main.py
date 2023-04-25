import customtkinter as ctk
from image_widgets import *
 
class App(ctk.CTk):
    def __init__(self):
        #setup [frame size, name and size]
        super().__init__()
        ctk.set_appearance_mode('dark')
        self.geometry('1000x600')
        self.title('Photo Editor')
        self.minsize(800,500)
         
        # layout
        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 2)
        self.columnconfigure(1, weight = 6)
         
        # widgets
         
        # ImportButton (Frame with a button)
        ImageImport(self, self.import_image)
         
        #run
        self.mainloop()
         
    def import_image(self, path):
        print(path)

App()
