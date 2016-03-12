"""
Clock module for MirrorOS
Autor: Bastian Schroll
"""

from tkinter import *
import time

class clock:
    def __init__(self, window, config):
        self.window = window
        self.config = config

        self.clock = Label(self.window, fg=self.config.get("clock","color"), font=self.config.get("clock","font"), bg='black')
        self.clock.place(x=self.window.winfo_screenwidth()/2, y=self. window.winfo_screenheight()/2-150, anchor=N)

        self.update() #starts his own update routine

    def update(self):
        self.clock.configure(text=time.strftime(self.config.get("clock","format")))
        self.clock.after(self.config.getint("clock","update_interval"), self.update)
