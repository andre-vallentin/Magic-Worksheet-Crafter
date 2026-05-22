import re

from ...builder.modules.source_text import SourceText

def parse_to_source_text(text) -> SourceText:

    lines = text.splitlines()
    lines = [s.strip() for s in lines if s.strip()]

    content = text[len(lines[0]):].lstrip('\n')

    return SourceText(content=content)