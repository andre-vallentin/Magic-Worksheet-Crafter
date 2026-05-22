import tkinter as tk
from tkinter import filedialog, colorchooser


class ColorButton(tk.Frame):
    """Canvas showing current color; click opens color picker or edit hex directly."""

    def __init__(self, parent, initial_hex: str, **kwargs):
        super().__init__(parent, **kwargs)
        self._hex = initial_hex
        self._canvas = tk.Canvas(
            self, width=50, height=30, bg="white", bd=1, relief="solid", highlightthickness=0
        )
        self._canvas.pack(side="left", padx=(0, 6))
        self._canvas.bind("<Button>", lambda _: self._pick())
        self._draw_color()

        self._hex_var = tk.StringVar(value=initial_hex)
        self._hex_var.trace_add("write", self._on_hex_change)
        self._entry = tk.Entry(self, textvariable=self._hex_var, width=8, font=("Menlo", 12))
        self._entry.pack(side="left")

    def _draw_color(self):
        self._canvas.delete("all")
        self._canvas.create_rectangle(0, 0, 50, 30, fill=self._hex, outline="#999")

    def _on_hex_change(self, *_):
        text = self._hex_var.get().upper()
        if text.startswith("#") and len(text) == 7:
            try:
                int(text[1:], 16)
                self._hex = text
                self._draw_color()
            except ValueError:
                pass

    def _pick(self):
        result = colorchooser.askcolor(color=self._hex, title="Farbe wählen")
        if result[1]:
            self._hex = result[1].upper()
            self._hex_var.set(self._hex)
            self._draw_color()

    def get(self) -> str:
        return self._hex


class FileRow(tk.Frame):
    """Label + path entry + browse button row."""

    def __init__(self, parent, label: str, filetypes=None, **kwargs):
        super().__init__(parent, **kwargs)
        self._filetypes = filetypes or [("PNG", "*.png"), ("Alle Dateien", "*.*")]
        tk.Label(self, text=label, width=16, anchor="w", font=("Helvetica", 12)).pack(side="left")
        self._var = tk.StringVar()
        tk.Entry(self, textvariable=self._var, width=36, font=("Helvetica", 12)).pack(side="left", padx=(0, 6))
        tk.Button(self, text="Wählen", command=self._browse, font=("Helvetica", 12)).pack(side="left")

    def _browse(self):
        path = filedialog.askopenfilename(filetypes=self._filetypes)
        if path:
            self._var.set(path)

    def get(self) -> str:
        return self._var.get()

    def set(self, value: str):
        self._var.set(value)
