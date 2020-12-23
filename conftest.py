
"""
derived from: https://docs.pytest.org/en/latest/example/simple.html#control-skipping-of-tests-according-to-command-line-option

found via: https://stackoverflow.com/questions/51883573/using-a-command-line-option-in-a-pytest-skip-if-condition
"""

import pytest

def pytest_addoption(parser):
    parser.addoption(
            "--runwebtests", action="store_true", default=False, help="run tests that depend on web access")


def pytest_collection_modifyitems(config, items):
    if config.getoption("--runwebtests"):
        # --runwe given in cli: do not skip slow tests
        return
    skip_web = pytest.mark.skip(reason="need --runwebtests option to run")
    for item in items:
        if "web_test" in item.keywords:
            item.add_marker(skip_web)
