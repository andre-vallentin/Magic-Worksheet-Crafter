import re

def build_formatted_paragraph(doc, text):
    p = doc.add_paragraph()
    formatted_paragraph(p, text)

def formatted_paragraph(paragraph, text):
    """
    Supports:
    **bold**
    _italic_
    """

    pattern = r'(\*\*.+?\*\*|_.+?_|#.+?#)'
    last_end = 0

    for match in re.finditer(pattern, text):
        # normal text before match
        if match.start() > last_end:
            paragraph.add_run(text[last_end:match.start()])

        token = match.group(0)

        if token.startswith("**"):
            run = paragraph.add_run(token[2:-2])
            run.bold = True

        elif token.startswith("_"):
            run = paragraph.add_run(token[1:-1])
            run.italic = True

        last_end = match.end()

    # remaining text
    if last_end < len(text):
        paragraph.add_run(text[last_end:])

    return paragraph
