@staticmethod
def add_study_header(paragraph, unit_name, colorOne, colorTwo):
    """
    Add "units" with colors
    """

    unitColorMap = {
        "Naturwissenschaften": [0, 1, 5, 6],
        "Deutsch": [0, 1, 2],
        "Mathe": [0, 1],
        "Musik": [0, 1],
        "Sachunterricht": [0, 4],
        "Sport": [0, 1],
        "Kunst": [0, 1]
    }

    unit = unitColorMap.get(unit_name, []) 
    text = unit_name

    # Indices where we want in first color: 0-1 (Na) and 5-6 (wi)
    colorOneIndicies = set(unit)

    # Empty run first (matching template)
    paragraph.add_run("\n ")

    # Add each character with appropriate color
    for i, char in enumerate(text):
        color = colorOne if i in colorOneIndicies else colorTwo
        run = paragraph.add_run(char)
        run.bold = True
        run.font.color.rgb = color
