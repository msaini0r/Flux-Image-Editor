<p>

1. CustomTkinter is a tkinter extension which provides extra ui-elements like the CTkButton, which can be used like a normal tkinter.Button, but can be customized with a border and round edges.

2. To display image inside tkinter we use Canvas

3. When we are calling the `def __init__(self):` we are basically getting image and canvas length and width. by default they are set to 0.

4. When we are calling the `def import_image(self, path):` , we are basically getting image ratio once and then we are just removing the open image button.

5. After that when we call `def resize_image(self, event):` , we basically getting the canvas width and height and resizing the image in a way that it remains in the center and fit properly. To call that image into the canvas properly after fitting we are using `def place_image(self):` .
</p>