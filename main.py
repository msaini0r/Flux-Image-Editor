import customtkinter as ctk
from image_widgets import *
from PIL import Image, ImageTk


class App(ctk.CTk):
    def __init__(self):
        # setup [frame size, name and size]
        super().__init__()
        ctk.set_appearance_mode('dark')
        self.geometry('1000x600')
        self.title('Photo Editor')
        self.minsize(800, 500)

        # layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=6)

        # ImportButton (Frame with a button)
        self.image_import = ImageImport(self, self.import_image)

        # run
        self.mainloop()

    # import image from path
    def import_image(self, path):
        self.image = Image.open(path)
        self.image_ratio = self.image.size[0] / \
            self.image.size[1]  # image ratio
        self.image_tk = ImageTk.PhotoImage(self.image)

    # hidding the Import button while selecting image
        self.image_import.grid_forget()
        # we are directly importing resize image in image output
        self.image_output = ImageOutput(self, self.resize_image)

    # putting image into canvas
    def resize_image(self, event):

        # current canvas ratio
        canvas_ratio = event.width / event.height

        # resize
        if canvas_ratio > self.image_ratio:  # canvas is wider tham image
            image_height = int(event.height)
            image_width = int(image_height * self.image_ratio)
        else:  # image is wider than the canvas
            image_width = int(event.width)
            image_height = int(image_width / self.image_ratio)

        # place image
        self.image_output.delete('all')
        resized_image = self.image.resize((image_width, image_height))
        self.image_tk = ImageTk.PhotoImage(resized_image)
        self.image_output.create_image(
            event.width / 2, event.height / 2, image=self.image_tk)  # [x,y,imagetk]


App()
