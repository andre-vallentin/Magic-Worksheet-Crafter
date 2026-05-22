from docx.shared import Mm

def set_column_width(table, column, width_mm):
    """Set column width by iterating through rows and setting individual cell widths."""
    table.allow_autofit = False
    for row in table.rows:
        row.cells[column].width = Mm(width_mm)