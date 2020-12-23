import excel



def column_generator(column_spec):
    column_name = column_spec['name']
    column_type = column_spec['type']
    return f'''{column_name} {column_type}'''
