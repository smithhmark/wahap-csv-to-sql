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
