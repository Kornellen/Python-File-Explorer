from tkinter import *
from tkinter import ttk


class Window:
    def __init__(self, program_name: str, padding: int) -> None:
        # Root setup
        self.root = Tk()
        self.root.title(program_name)
        self.root.geometry("1000x800")

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Frame setup
        self.frame = ttk.Frame(self.root, padding=padding)
        self.frame.grid(row=0, column=0, sticky="nsew")

        self.frame.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)

        # Components Setup
        self.InitializeComponents()

    def InitializeComponents(self):
        self.tree = ttk.Treeview(self.frame, height=1500)
        self.tree.grid(row=0, column=0, sticky="nsew")

        self.buttons_frame = ttk.Frame(self.frame)
        self.buttons_frame.grid(row=1, column=0, sticky="ew", pady=100, padx=50)

        self.button = ttk.Button(
            self.buttons_frame, command=self.root.destroy, text="Quit"
        )
        self.button.pack(side=LEFT, padx=10)

    def AddComponent(self, parent, text):
        return self.tree.insert(parent, "end", text=text)

    def Run(self):
        self.root.mainloop()
