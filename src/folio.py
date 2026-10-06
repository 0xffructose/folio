from tkinter import Tk
from src.fmenubar import FolioMenuBar

class FolioApp:
    def __init__(self) -> None:
        self.root = Tk()

        self.root.title("Folio v0.0.1")

        self.root.geometry("640x480")
        self.root.minsize(640, 480)

        self.menubar = FolioMenuBar(self.root).get()

        self.root.config(menu=self.menubar)
        self.root.mainloop()