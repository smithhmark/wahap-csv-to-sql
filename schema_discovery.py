import excel



def column_generator(column_spec):
    column_name = column_spec['name']
    column_type = column_spec['type']
    return f'''{column_name} {column_type}'''


def table_generator(table_spec):
    cols = [column_generator(spec) for spec in table_spec['columns']]
    return f"""CREATE TABLE {table_spec['name']} ( {', '.join(cols)} ) ;"""
