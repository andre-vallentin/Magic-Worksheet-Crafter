from .shared.table_structure_parser import parse_table_structure
from ...builder.modules.single_choice import SingleChoiceTask

def parse_single_choice(text) -> SingleChoiceTask:
        
    table_structure = parse_table_structure(text)
    table_structure['tableContent'] = table_structure['tableContent'][1:]  # Remove header row for SingleChoiceTask
    return SingleChoiceTask(title=table_structure['title'], description=table_structure['description'], content=table_structure['tableContent'])
