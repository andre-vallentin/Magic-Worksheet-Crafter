import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
import logging
import traceback

from ..config import load_config, save_config, get_user_assets_icons_dir, get_user_assets_logos_dir, _BUNDLED_ICONS, _BUNDLED_LOGOS
from ..main import main as generate_worksheet
from .components import ColorButton, FileRow
logger = logging.getLogger(__name__)

class CreateTab(tk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, padx=20, pady=20, **kwargs)

        tk.Label(self, text="Arbeitsblatt erstellen", font=("Helvetica", 16, "bold")).pack(anchor="w", pady=(0, 16))

        self._input = FileRow(
            self, "Markdown-Datei:",
            filetypes=[("Markdown", "*.md"), ("Alle Dateien", "*.*")],
        )
        self._input.pack(fill="x", pady=6)

        output_row = tk.Frame(self)
        output_row.pack(fill="x", pady=6)
        tk.Label(output_row, text="Ausgabe-Datei:", width=16, anchor="w", font=("Helvetica", 12)).pack(side="left")
        self._output_var = tk.StringVar()
        tk.Entry(output_row, textvariable=self._output_var, width=36, font=("Helvetica", 12)).pack(side="left", padx=(0, 6))
        tk.Button(output_row, text="Wählen", command=self._pick_output, font=("Helvetica", 12)).pack(side="left")

        tk.Button(
            self, text="Arbeitsblatt erstellen",
            command=self._generate,
            fg="black",
            font=("Helvetica", 14, "bold"),
            relief="flat", padx=16, pady=12
        ).pack(pady=20)

        self._status = tk.Label(self, text="", font=("Helvetica", 12), fg="#555555")
        self._status.pack()

    def _pick_output(self):
        path = filedialog.asksaveasfilename(
            defaultextension=".docx",
            filetypes=[("Word Dokument", "*.docx")],
        )
        if path:
            self._output_var.set(path)

    def _generate(self):
        src = self._input.get()
        out = self._output_var.get()
        if not src or not out:
            messagebox.showwarning("Fehlende Eingabe", "Bitte Markdown-Datei und Ausgabe-Datei wählen.")
            return
        try:
            self._status.config(text="Erstelle Arbeitsblatt…", fg="#555555")
            self.update_idletasks()
            generate_worksheet(src, out)
            self._status.config(text=f"Gespeichert: {Path(out).name}", fg="#01A976")
        except Exception as exc:
            error_msg = traceback.format_exc()
            logger.error(f"Fehler beim Erstellen des Arbeitsblatts:\n{error_msg}")
            self._status.config(text=f"Fehler: {type(exc).__name__}: {exc}", fg="#CC0000")


class SettingsTab(tk.Frame):
    _DEFAULTS = {
        "primary_hex": "#FF6F4A",
        "secondary_hex": "#01A976",
        "logo": str(_BUNDLED_LOGOS / "logo.png"),
        "icons": {
            "exercise": str(_BUNDLED_ICONS / "exercise.png"),
            "table": str(_BUNDLED_ICONS / "table.png"),
            "single_choice": str(_BUNDLED_ICONS / "tick_task.png"),
            "information": str(_BUNDLED_ICONS / "info_text.png"),
        },
    }

    def __init__(self, parent, **kwargs):
        super().__init__(parent, padx=20, pady=20, **kwargs)

        tk.Label(self, text="Einstellungen", font=("Helvetica", 16, "bold")).pack(anchor="w", pady=(0, 16))

        config = load_config()

        # Colors
        tk.Label(self, text="Farben", font=("Helvetica", 13, "bold")).pack(anchor="w", pady=(0, 4))

        color_frame = tk.Frame(self)
        color_frame.pack(fill="x", pady=(0, 16))

        tk.Label(color_frame, text="Primärfarbe:", width=16, anchor="w", font=("Helvetica", 12)).grid(row=0, column=0, sticky="w", pady=4)
        self._color1 = ColorButton(color_frame, config.color_primary_hex)
        self._color1.grid(row=0, column=1, sticky="w", pady=4)

        tk.Label(color_frame, text="Sekundärfarbe:", width=16, anchor="w", font=("Helvetica", 12)).grid(row=1, column=0, sticky="w", pady=4)
        self._color2 = ColorButton(color_frame, config.color_secondary_hex)
        self._color2.grid(row=1, column=1, sticky="w", pady=4)

        # Logo
        tk.Label(self, text="Logo", font=("Helvetica", 13, "bold")).pack(anchor="w", pady=(0, 4))
        self._logo = FileRow(self, "Logo-Datei:")
        self._logo.set(config.logo_path)
        self._logo.pack(fill="x", pady=(0, 16))

        # Icons
        tk.Label(self, text="Icons", font=("Helvetica", 13, "bold")).pack(anchor="w", pady=(0, 4))
        icon_frame = tk.Frame(self)
        icon_frame.pack(fill="x", pady=(0, 16))

        icon_labels = {
            "information":   "Informationstext:",
            "exercise":      "Textaufgabe:",
            "table":         "Tabelle:",
            "single_choice": "Richtig/Falsch:",
        }
        self._icons = {}
        for i, (key, label) in enumerate(icon_labels.items()):
            row = FileRow(icon_frame, label)
            row.set(config.icon_paths[key])
            row.pack(fill="x", pady=3)
            self._icons[key] = row

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        tk.Button(
            button_frame, text="Einstellungen speichern",
            command=self._save,
            fg="black",
            font=("Helvetica", 14, "bold"),
            relief="flat", padx=16, pady=12
        ).pack(side="left", padx=5)

        tk.Button(
            button_frame, text="Zurücksetzen",
            command=self._reset,
            fg="black",
            font=("Helvetica", 14, "bold"),
            relief="flat", padx=16, pady=12
        ).pack(side="left", padx=5)

        self._status = tk.Label(self, text="", font=("Helvetica", 12))
        self._status.pack()

    def _save(self):
        try:
            save_config(
                primary_hex=self._color1.get(),
                secondary_hex=self._color2.get(),
                logo_path=self._logo.get(),
                icon_paths={k: v.get() for k, v in self._icons.items()},
            )
            self._status.config(text="Einstellungen gespeichert.", fg="#01A976")
        except Exception as exc:
            error_msg = traceback.format_exc()
            logger.error(f"Fehler beim Speichern der Einstellungen:\n{error_msg}")
            self._status.config(text=f"Fehler: {type(exc).__name__}: {exc}", fg="#CC0000")

    def _reset(self):
        if messagebox.askyesno("Zurücksetzen", "Möchten Sie alle Einstellungen auf die Standard-Werte zurücksetzen?"):
            try:
                import shutil
                user_icons_dir = get_user_assets_icons_dir()
                user_logos_dir = get_user_assets_logos_dir()

                # Copy default assets to user folder, overwriting existing files
                for f in _BUNDLED_ICONS.glob("*.png"):
                    shutil.copy2(f, user_icons_dir / f.name)
                for f in _BUNDLED_LOGOS.glob("*.png"):
                    shutil.copy2(f, user_logos_dir / f.name)

                self._color1._hex_var.set(self._DEFAULTS["primary_hex"])
                self._color2._hex_var.set(self._DEFAULTS["secondary_hex"])
                self._logo.set(self._DEFAULTS["logo"])
                for key, row in self._icons.items():
                    row.set(self._DEFAULTS["icons"][key])
                self._status.config(text="Einstellungen zurückgesetzt.", fg="#01A976")
            except Exception as exc:
                error_msg = traceback.format_exc()
                logger.error(f"Fehler beim Zurücksetzen der Einstellungen:\n{error_msg}")
                self._status.config(text=f"Fehler: {type(exc).__name__}: {exc}", fg="#CC0000")
