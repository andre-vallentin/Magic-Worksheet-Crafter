from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("magic-worksheet-crafter")
except PackageNotFoundError:
    __version__ = "unknown"
