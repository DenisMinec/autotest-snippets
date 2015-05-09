import pytest

def pytest_runtest_makereport(item, call):
    if call.excinfo is not None:
        setattr(item, 'error', call.excinfo)
        # pass
