import re

from django.core.exceptions import ValidationError


class ColumnTitle:
    def __init__(self, canonical_name, alternatives=None):
        self.canonical_name = canonical_name
        self.alternatives = alternatives or []

    @staticmethod
    def normalize(s):
        return re.sub(r'\s+', '', str(s).lower())

    def matches(self, value):
        normval = self.normalize(value)
        if self.normalize(self.canonical_name) == normval:
            return True
        for alt in self.alternatives:
            if isinstance(alt, str):
                if self.normalize(alt) == normval:
                    return True
            else:
                # Assume it's a compiled regular expression.
                if alt.match(value):
                    return True
        return False

    def __str__(self):
        return self.canonical_name


def safe_cell_str_value(sheet, rownum, colnum, coercer=None):
    val = ''

    try:
        val = sheet.cell_value(rownum, colnum)
    except IndexError:
        pass

    print(f"val before: '{val}'")
    if coercer is not None:
        try:
            val = coercer(val)
            print(f"val after: '{val}'")
        except ValueError:
            print(f"Failed on '{val}'")
            pass
    print("-----------------------")

    return str(val)


def generate_column_index_map(heading_row, field_title_map):
    def find_col(col_title):
        for idx, cell in enumerate(heading_row):
            if col_title.matches(cell.value):
                return idx
        raise ValidationError('Column heading "{}" was not found.'.format(
            col_title))

    col_idx_map = {}
    for field, title in field_title_map.items():
        if isinstance(title, str):
            title = ColumnTitle(title)
        col_idx_map[field] = find_col(title)

    return col_idx_map
