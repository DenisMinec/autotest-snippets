import pytest

@pytest.yield_fixture(autouse=True)
def collect(request):
    yield
    if hasattr(request.node, 'error'):
        pass

def test_01():
    assert False

def test_02():
    assert True

if __name__ == '__main__':
    pytest.main(args=['-s', 'test_04_using_conftest.py'])