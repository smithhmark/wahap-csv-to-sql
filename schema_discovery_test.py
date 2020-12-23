import pytest

import schema_discovery as sd

@pytest.fixture
def toy_column_spec():
    return { "name": "col1",
                    "type": "text",
                    }


@pytest.fixture
def toy_table_spec(toy_column_spec):
    return {"name": "my table",
            "columns": [
                toy_column_spec,
                {
                    "name": "column two",
                    "type": "int",
                    },
                ]
            }

@pytest.fixture
def ex_table():
    return [
            {"field": "id", "type": "string"},
            {"field": "name", "type": "string"},
            {"field": "cost", "type": "int"},
            {"field": "date", "type": "date"},
        ]

@pytest.fixture
def ex_spec_bare():
    return {
            "name": "example_table",
            "columns": [
                {"name": "id", "type": "text"},
                {"name": "name", "type": "text"},
                {"name": "cost", "type": "int"},
                {"name": "date", "type": "date"},
                ],
            }

def test_transform_column():
    given = {"field": "id", "type": "string"}
    expect = {"name": "id", "type": "text"}
    rcvd = sd._transform_column(given, {"string": "text"})
    assert rcvd == expect

def test_table_to_spec(ex_table, ex_spec_bare):
    rcvd = sd.to_spec("example_table", ex_table)
    print(rcvd)
    print(ex_spec_bare)
    assert rcvd == ex_spec_bare

@pytest.mark.xfail
def test_table_to_sql(ex_table):
    pass

@pytest.mark.xfail
def test_override_type():
    pass

def test_column_generator(toy_column_spec):
    expected = f'''{toy_column_spec['name']} {toy_column_spec['type']}'''
    assert sd.column_generator(toy_column_spec) == expected

def test_table_generator(toy_table_spec):
    expect = f"""CREATE TABLE {toy_table_spec['name']} ( {toy_table_spec['columns'][0]['name']} {toy_table_spec['columns'][0]['type']}, {toy_table_spec['columns'][1]['name']} {toy_table_spec['columns'][1]['type']} ) ;"""

    assert sd.table_generator(toy_table_spec) == expect
