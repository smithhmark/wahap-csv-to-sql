"""
This module is used for turning extracted schema description tables into sql.
"""


def column_generator(column_spec):
    """generates a column's DDL based on a spec
    """
    column_name = column_spec['name']
    column_type = column_spec['type']
    return f'''{column_name} {column_type}'''


def table_generator(table_spec):
    """generates a table's DDL based on a spec
    """
    cols = [column_generator(spec) for spec in table_spec['columns']]
    return f"""CREATE TABLE {table_spec['name']} ( {', '.join(cols)} ) ;"""

def _transform_column(raw, type_overrides):
    """helper function to facilitate converting specs to SQL
    """
    output = {}
    output['name'] = raw['field']
    output['type'] = type_overrides.get(raw['type'], raw['type'])
    return output

def to_spec(table_name, columns, type_overrides):
    """Transform's an extracted schema description into a table spec that
    can be turned into SQL.
    """
    spec = {"name": table_name}
    cols = [ _transform_column(dd, type_overrides) for dd in columns]
    spec['columns'] = cols
    return spec
