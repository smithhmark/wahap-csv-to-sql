import pytest
import openpyxl
import excel

@pytest.fixture
def example_path():
    return "test_data/Export Data Specs.xlsx"

@pytest.fixture
def example_excel(example_path):
    return openpyxl.load_workbook(filename=example_path)

def test_get_link(example_excel):
    sheet = example_excel['EN']
    target = excel.get_link_target(sheet, "A8")
    assert target == "http://wahapedia.ru/wh40k9ed/Factions.csv"
