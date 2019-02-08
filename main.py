#!/usr/bin/env python

import sys, os
sys.path.append(os.path.abspath('./include'))

import tkinter as tk
from PIL import Image, ImageTk

from theme import *

class Application(tk.Canvas):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.style()
        self.create_widgets()

    def style(self):
        self.master['bg'] = BG_COLOR

    def create_widgets(self):
        self.hey = tk.Button(self)
        self.hey['text'] = 'hey'
        self.hey['command'] = self.say_hey
        self.hey.pack(side='top')

        self.quit_button = tk.Button(self, text='quit', command=self.master.destroy)
        self.quit_button.pack(side='bottom')

    def draw_image(self, path):
        img = ImageTk.PhotoImage(Image.open(path))

        self.image_label = tk.Label(self, image=img)
        self.image_label.image = img
        self.image_label.pack()

    def say_hey(self):
        print("hiiiiiiiiiii...")


root = tk.Tk()
app = Application(master=root)

app.draw_image("img/loz.jpg")

app.mainloop()
