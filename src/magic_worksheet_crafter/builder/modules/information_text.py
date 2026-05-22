from .shared.segment import Segment
from .shared.markdown_handler import build_formatted_paragraph

class InformationText(Segment):

    def __init__(self, title, content):
        self.title = title
        self.content = content
        super().__init__(title, description="", content=content, icon_path=None)

    def build(self, doc):

        self.add_segment_header(doc)
        build_formatted_paragraph(doc, self.content)
        doc.add_paragraph()  # Add spacing after the table        

