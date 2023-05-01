import customtkinter as ctk
from settings import *

# Panels
class Panel(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=DARK_GREY)
        self.pack(fill='x', pady='4', ipady='8')


class SliderPanel(Panel):
    def __init__(self, parent, text, data_var, min_value, max_value):
        super().__init__(parent=parent)

        # Layout
        self.rowconfigure((0, 1), weight=1)
        self.columnconfigure((0, 1), weight=1)
        
        self.data_var = data_var
        self.data_var.trace('w', self.update_text)

        ctk.CTkLabel(self, text=text).grid(column=0, row=0, sticky='W', padx=5)
        self.num_label = ctk.CTkLabel(self, text=data_var.get())
        self.num_label.grid(column=1, row=0, sticky='E', padx=5)
        ctk.CTkSlider(self, fg_color=SLIDER_BG, variable=self.data_var, from_=min_value, to=max_value).grid(row=1, column=0, columnspan=2, sticky='ew', padx=5, pady=5)

    def update_text(self, *args):
        self.num_label.configure(text=f'{round(self.data_var.get(), 2)}')


class SegmentedPanel(Panel):
    def __init__(self, parent, text, data_var, options):
        super().__init__(parent=parent)

        ctk.CTkLabel(self, text=text).pack()
        ctk.CTkSegmentedButton(self, variable=data_var, values=options).pack(
            expand=True, fill='both', padx=4, pady=4)


class SwitchPanel(Panel):
    def __init__(self, parent, *args):  # ((var, text), (var, text)) ~ basically tuples
        super().__init__(parent=parent)

        for var, text in args:
            switch = ctk.CTkSwitch(
                self, text=text, variable=var, button_color=BLUE, fg_color=SLIDER_BG)
            switch.pack(side='left', expand=True, fill='both', padx=5, pady=5)


class DropDownPanel(ctk.CTkOptionMenu):
    # ((var, text), (var, text)) ~ basically tuples
    def __init__(self, parent, data_var, options):
        super().__init__(master=parent, values=options, fg_color=DARK_GREY, button_color=DROPDOWN_MAIN_COLOR,
                         button_hover_color=DROPDOWN_Hover_COLOR, dropdown_fg_color=DROPDOWN_MENU_COLOR, variable=data_var)
        self.pack(fill='x', pady=4)

class RevertButton(ctk.CTkButton):
    def __init__(self, parent, *args):
        super().__init__(master=parent, text='Revert', command=self.revert)
        self.pack(side='bottom', pady=10)
        self.args = args
    
    def revert(self):
        for var, value in self.args:
            var.set(value)
        