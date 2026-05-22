from .shared.segment import Segment
from .shared.markdown_handler import build_formatted_paragraph

class SourceText(Segment):

    def __init__(self, content):        

        self.content = content
        super().__init__(title="", description="", content=content, icon_path=None)

    def build(self, doc):
        build_formatted_paragraph(doc, self.content)

