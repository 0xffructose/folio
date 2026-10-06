from tkinter import Tk, Menu

class FolioMenuBar:
    def __init__(self, root: Tk = None) -> None:
        self.menubar = Menu(root)

        file = Menu(self.menubar, tearoff=0)

        self.menubar.add_cascade(label="File", menu=file)

        file.add_command(label="New Workspace", command=None)
        file.add_command(label="Open Workspace", command=None)
        file.add_separator()
        file.add_command(label="Exit", command=None)

    def get(self) -> Menu:
        return self.menubar