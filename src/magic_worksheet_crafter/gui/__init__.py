import logging
from pathlib import Path

from .app import App

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(Path.home() / ".worksheet_crafter.log"),
        logging.StreamHandler()
    ]
)


def launch():
    app = App()
    app.mainloop()
