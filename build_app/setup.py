import sys
import os
import shutil
import atexit

_here = os.path.dirname(os.path.abspath(__file__))
_root = os.path.join(_here, "..")

sys.path.insert(0, os.path.join(_root, "src"))
from setuptools import setup, Distribution

def _cleanup_build():
    build_dir = os.path.join(_root, "build")
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
        print(f"Cleaned up {build_dir}")

atexit.register(_cleanup_build)

class _Dist(Distribution):
    def parse_config_files(self):
        super().parse_config_files()
        # py2app rejects non-empty install_requires; pyproject.toml auto-sets it
        # Clear it here after config is parsed but before commands run
        self.install_requires = []

setup(
    distclass=_Dist,
    app=["build_app/app_entry.py"],
    options={
        "py2app": {
            "packages": ["magic_worksheet_crafter", "docx", "yaml"],
            "includes": ["tkinter", "tomllib"],
            "resources": [os.path.join(_root, "src", "magic_worksheet_crafter", "assets")],
            "plist": {
                "CFBundleName": "Magic Worksheet Crafter",
                "CFBundleDisplayName": "Magic Worksheet Crafter",
                "CFBundleIdentifier": "de.vallentin.worksheetcrafter",
                "CFBundleVersion": "1.0.0",
                "CFBundleShortVersionString": "1.0",
                "NSHumanReadableCopyright": "Herr Vallentin",
                "LSMinimumSystemVersion": "12.0",
            },
        }
    },
)
