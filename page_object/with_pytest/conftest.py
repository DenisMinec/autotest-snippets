import pytest
from errors_collector import ErrorsCollector

def pytest_runtest_makereport(item, call):
    if call.excinfo is not None:
        ec = ErrorsCollector()
        ec.errors = dict( trace=call.excinfo, item=item )