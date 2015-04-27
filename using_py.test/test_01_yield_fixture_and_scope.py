# coding: utf-8
import pytest


@pytest.yield_fixture(scope='function')  # default
def f1():
    print('f1 start')
    yield 'f1 mid'
    print('f1 end')


@pytest.yield_fixture(scope='class')
def f2():
    print('f2 start')
    yield 'f2 mid'
    print('f2 end')


@pytest.yield_fixture(scope='module')
def f3():
    print('f3 start')
    yield 'f3 mid'
    print('f3 end')


@pytest.yield_fixture(scope='session')
def f4():
    print('f4 start')
    yield 'f4 mid'
    print('f4 end')


def test_01(f1, f2):
    print(f1)
    print(f2)


def test_02(f1, f2):
    print(f1)
    print(f2)


class TestCase:
    def test_03(self, f1, f2):
        print(f1)
        print(f2)

    def test_04(self, f1, f2):
        print(f1)
        print(f2)