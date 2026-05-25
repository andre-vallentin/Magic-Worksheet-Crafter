import re

from ...builder.modules.reference_list import ReferenceList

def parse_to_reference_list(text) -> ReferenceList:

    lines = text.splitlines()
    lines = [s.strip() for s in lines if s.strip()]

    content = text[len(lines[0]):].lstrip('\n')

    return ReferenceList(content=content)