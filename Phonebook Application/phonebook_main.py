from tkinter import *
import tkinter as tk
import phonebook_gui
import phonebook_func


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(500, 300)  # (height, width)
        self.master.maxsize(500, 300)

        # center-window() method will center our app on the user's screen
        phonebook_func.center_window(self, 500, 300)
        self.master.title("The Tkinter Phonebook")
        self.master.configure(bg="#F0F0F0")

        # this protocol method is a tkinter build-in method to catch if
        # the user clicks the upper corner, 'X' on Windows OS
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a separate module
        # keeping your code comparmentalized and clutter free
        phonebook_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
