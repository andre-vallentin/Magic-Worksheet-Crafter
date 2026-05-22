import tkinter as tk
from tkinter import ttk

from .tabs import CreateTab, SettingsTab


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Magic Worksheet Crafter")
        self.resizable(False, False)

        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True)

        create_tab = CreateTab(notebook)
        notebook.add(create_tab, text="  Erstellen  ")

        settings_tab = SettingsTab(notebook)
        notebook.add(settings_tab, text="  Einstellungen  ")
