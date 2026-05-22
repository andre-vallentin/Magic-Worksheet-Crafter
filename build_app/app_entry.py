import sys
import os

if getattr(sys, "frozen", False):
    # py2app bundled the project folder as a package; add the inner src to path
    for _p in list(sys.path):
        _src = os.path.join(_p, "magic_worksheet_crafter", "src")
        if os.path.isdir(_src):
            sys.path.insert(0, _src)
            break
else:
    _here = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, os.path.join(_here, "..", "src"))

from magic_worksheet_crafter.gui import launch

if __name__ == "__main__":
    launch()
