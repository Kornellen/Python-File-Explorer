from tkinter import *
from tkinter import ttk, Tk


class Window:
    def __init__(self, program_name: str, padding: int) -> None:
        # Root setup
        self.ConfigureRoot(program_name)

        self.SetUpStyles()

        self.SetUpFrame(padding)

        self.InitializeComponents()

    def ConfigureRoot(self, program_name: str) -> None:
        self.root = Tk()
        self.root.title(program_name)
        self.root.geometry("1000x800")

        self.root.config(bg="skyblue")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def SetUpStyles(self) -> None:
        """Style Setup"""
        font = ("Verdana", 15)
        self.style = ttk.Style()

        self.style.configure(
            "Back.TFrame",
            background="#2d2e2e",
            foreground="#c9c9c9",
            font=font,
        )
        self.style.configure(
            "Back.Treeview",
            foreground="#c9c9c9",
            background="#2d2e2e",
            font=font,
            borderwidth=0,
            relief="falt",
            rowheight=25,
        )

    def SetUpFrame(self, padding) -> None:
        """Frame Setup"""

        self.frame = ttk.Frame(
            self.root, style="Back.TFrame", padding=padding, height=100, width=200
        )
        self.frame.grid(row=0, column=0, sticky="nsew")

        self.frame.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)

    def InitializeComponents(self) -> None:
        """TreeView"""
        self.tree = ttk.Treeview(self.frame, height=2000, style="Back.Treeview")
        self.tree.grid(row=0, column=0, sticky="nsew")

        self.buttons_frame = ttk.Frame(self.frame, style="Back.TFrame")
        self.buttons_frame.grid(row=1, column=0, sticky="ew", ipady=100, ipadx=50)

        """Button"""
        self.button = ttk.Button(
            self.buttons_frame, command=self.root.destroy, text="Quit"
        )
        self.button.pack(side=LEFT, ipadx=10, ipady=20)

    def InsertTreeViewNode(self, parent, text) -> str:
        return self.tree.insert(parent, "end", text=text)

    def Run(self) -> None:
        """Main loop"""
        self.root.mainloop()
