import sys
import os
import shutil
import atexit
from typing import Any

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

_py2app_opts: dict[str, Any] = {
    "packages": ["magic_worksheet_crafter", "docx", "yaml"],
    "includes": ["tkinter", "tomllib"],
    "resources": [os.path.join(_root, "src", "magic_worksheet_crafter", "assets")],
    #"iconfile": os.path.join(_here, "magic_worksheet_crafter.icns"),
    "plist": {
        "CFBundleName": "Magic Worksheet Crafter",
        "CFBundleDisplayName": "Magic Worksheet Crafter",
        "CFBundleIdentifier": "de.vallentin.worksheetcrafter",
        "CFBundleVersion": "1.0.0",
        "CFBundleShortVersionString": "1.0",
        "NSHumanReadableCopyright": "André Vallentin",
        "LSMinimumSystemVersion": "12.0",
    },
}

class _Dist(Distribution):
    def parse_config_files(self, filenames=None, ignore_option_errors=False):
        super().parse_config_files(filenames=filenames, ignore_option_errors=ignore_option_errors)
        # py2app rejects non-empty install_requires; pyproject.toml auto-sets it
        # Clear it here after config is parsed but before commands run
        self.install_requires = []

setup(  # type: ignore[arg-type]
    distclass=_Dist,
    app=["build_app/app_entry.py"],
    options={"py2app": _py2app_opts},
)
