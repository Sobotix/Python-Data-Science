import tkinter as tk

class Page(tk.Frame):
    """
    Base class of all pages
    Don't create object of this class, check it's derived classes
    """
    def __init__(self, master):
        """
        Constructor for initialization
        """
        tk.Frame.__init__(self, master)
    def show(self):
        """
        Call this method to bring this page into view
        """
        self.lift()