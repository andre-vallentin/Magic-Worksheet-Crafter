import re

from ...builder.modules.information_text import InformationText

def parse_to_information_text(text) -> InformationText:

    lines = text.splitlines()
    lines = [s.strip() for s in lines if s.strip()]

    title = re.sub(r'^#+\s', '', lines[0])
    content = text[len(lines[0]):].lstrip('\n')

    return InformationText(title=title, content=content)