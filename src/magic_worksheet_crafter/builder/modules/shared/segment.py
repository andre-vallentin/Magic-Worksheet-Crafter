from abc import ABC, abstractmethod

from .segment_header import segment_header

class Segment(ABC):
    
    def __init__(self, title, description, content, icon_path=None):
        self.title = title
        self.description = description
        self.content = content
        self.icon_path = icon_path

    def set_icon_path(self, path: str) -> None:
        self.icon_path = path

    @abstractmethod
    def build(self, doc):
        pass
    
    def add_segment_header(self, doc):
        """Add the information text with icon and Heading 2 title to the document."""
        segment_header(doc, self.icon_path, self.title, self.description)
