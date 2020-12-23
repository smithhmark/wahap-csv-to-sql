import pytest

import schema_discovery as sd

@pytest.fixture
def ex_column_spec():
    return { "name": "col1",
                    "type": "text",
                    }


@pytest.fixture
def ex_table_spec(ex_column_spec):
    return {"name": "my table",
            "columns": [
                ex_column_spec,
                {
                    "name": "column two",
                    "type": "int",
                    },
                ]
            }

@pytest.mark.xfail
def test_table_to_schema():
    pass

@pytest.mark.xfail
def test_override_type():
    pass

def test_column_generator(ex_column_spec):
    expected = f'''{ex_column_spec['name']} {ex_column_spec['type']}'''
    assert sd.column_generator(ex_column_spec) == expected

def test_table_generator(ex_table_spec):
    expect = f"""CREATE TABLE {ex_table_spec['name']} ( {ex_table_spec['columns'][0]['name']} {ex_table_spec['columns'][0]['type']}, {ex_table_spec['columns'][1]['name']} {ex_table_spec['columns'][1]['type']} ) ;"""

    assert sd.table_generator(ex_table_spec) == expect
