import re

def parse_table_structure(text):
    lines = text.splitlines()   # Alle Zeilen 
    lines = [s.strip() for s in lines if s.strip()]  

    title = re.sub(r'^#+\s', '', lines[0])
    separator_index = next(i for i, line in enumerate(lines) if line.startswith('|-'))

    description = ' '.join(lines[1:separator_index - 1])
    numberOfColumns = lines[separator_index].count('|-')

    headerrow = lines[separator_index - 1].split('|')[1:numberOfColumns + 1]
    headerrow = [cell.strip() for cell in headerrow]
    tableContent = [headerrow]

    for line in lines[separator_index + 1:]:
        row = [cell.strip() for cell in line.split('|')[1:numberOfColumns + 1]]
        tableContent.append(row)

    tablestructure = {
        'title': title,
        'description': description,
        'tableContent': tableContent
    }
    return tablestructure