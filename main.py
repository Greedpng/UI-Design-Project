#!/usr/bin/env python

import tkinter as tk
from PIL import Image, ImageTk

class Application(tk.Canvas):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.style()
        self.create_widgets()

    def style(self):
        self.master['bg'] = '#353535'

    def create_widgets(self):
        self.hey = tk.Button(self)
        self.hey['text'] = 'hey'
        self.hey['command'] = self.say_hey
        self.hey.pack(side='top')

        self.quit_button = tk.Button(self, text='quit', bg='red', command=self.master.destroy)
        self.quit_button.pack(side='bottom')

    # Keep a ref to the image? http://effbot.org/tkinterbook/photoimage.htm
    # def draw_image(self, path):
        # img = Image.open(path)
        # tk_img = ImageTk.PhotoImage(img)
        # # self.create_image((0, 0), img)
        # # img = tk.PhotoImage(file=path)
        # self.create_image(0, 0, img)
        # image_label = Label(root, image=Image)
        # image_label.image = Image
        # image_label.pack()

    def say_hey(self):
        print("hiiiiiiiiiii...")


root = tk.Tk()
app = Application(master=root)
# app.draw_image("img/loz.jpg")
app.mainloop()
