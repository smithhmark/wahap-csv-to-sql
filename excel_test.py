import pytest
import openpyxl

import excel

@pytest.fixture
def example_path():
    return "test_data/Export Data Specs.xlsx"

@pytest.fixture
def example_excel(example_path):
    return openpyxl.load_workbook(filename=example_path)

@pytest.fixture
def english_example(example_excel):
    return example_excel['EN'] 

@pytest.fixture
def factions_location():
    return "A8"

def test_get_link(example_excel, factions_location):
    sheet = example_excel['EN']
    target = excel.get_link_target(sheet, factions_location)
    assert target == "http://wahapedia.ru/wh40k9ed/Factions.csv"

def test_get_active_sheet(example_path, factions_location):
    english = excel.get_active_sheet(example_path)
    assert english[factions_location].value == 'Factions.csv'
    russian = excel.get_active_sheet(example_path, 'RU')
    assert russian[factions_location].value == 'Factions.csv'

def test_coord():
    assert excel._coord(1, 'a') == 'A1'
    assert excel._coord(1, 'A') == 'A1'

def test_colnum():
    assert excel._colnum('A') == 1
    assert excel._colnum('Z') == 26
    assert excel._colnum('AA') == 27
    assert excel._colnum('AB') == 28
    assert excel._colnum('BA') == 53

def test_address():
    assert excel._cell(0, 0) == "A1"
    assert excel._cell(0, 1) == "B1"
    assert excel._cell(1, 0) == "A2"
    assert excel._cell(1, 1) == "B2"
    assert excel._cell(17, 2) == "C18"

def test_get_table_header(english_example):
    headers = excel.get_table_header(english_example, 0, 16, 2)
    assert headers == ["Field", "Type"]

def test_get_table(english_example):
    table = excel.get_table(english_example, 0, 16, 2, True)
    print(table)
    assert len(table) == 7
