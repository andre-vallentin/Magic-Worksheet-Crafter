from .shared.table_structure_parser import parse_table_structure
from ...builder.modules.table_task import TableTask

def parse_table_task(text) -> TableTask:
    
    table_structure = parse_table_structure(text)
    return TableTask(title=table_structure['title'], description=table_structure['description'], content=table_structure['tableContent'])
