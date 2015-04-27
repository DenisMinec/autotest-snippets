# coding: utf-8
import pytest


def check_usr(usr, pwd):
    if usr == 'Peter' or not pwd:
        return False
    else:
        return True


@pytest.mark.parametrize('usr, pwd, expected', [
    ('test', 'test', True),
    ('Peter', 'test', False),
    ('', '', False),
    ('', 'test', False),
    ('login', '', False)
])
def test_login(usr, pwd, expected):
    assert check_usr(usr, pwd) == expected