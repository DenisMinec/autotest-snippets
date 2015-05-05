# coding: utf-8
# http://selenium-python.readthedocs.org/en/latest/page-objects.html
import pytest
from fixtures import driver
from base import LoginPage
import allure
# from allure.constants import Severity


   
@pytest.mark.parametrize('login, password', [
    ('test', 'test'),
    ('test2', 'test2')
])
def test_login(driver, login, password):
    
    login_page = LoginPage(driver)
    
    with allure.step('type_login'): 
        login_page._type_login(login)
    
    with allure.step('type_password'): 
        login_page._type_password(password)
    
    with allure.step('click login'):
        login_page._click_login_button()
    
