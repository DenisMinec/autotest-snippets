import sys
import pytest
import allure
from selenium import webdriver
from urllib.parse import urljoin
from allure.constants import AttachmentType
from datetime import datetime
from conftest import *

BASE_URL = 'http://ya.ru'

def Driver(klass, base_url):
      
    class WebDriverWrapper(klass):
         
        def __init__(self, base_url, *args, **kwargs):
            self._base_url = base_url
            super().__init__(*args, **kwargs)
             
        def get(self, url):
            url = urljoin(self._base_url, url)
            return super().get(url)
      
    return WebDriverWrapper(base_url) 

def ids_yield_fixture(scope, params, autouse=False):
    return pytest.yield_fixture(
        scope=scope, 
        ids=list(map(lambda i: i[0], params)), 
        params=list(map(lambda i: i[1], params)),  
        autouse=autouse
    )

@ids_yield_fixture(scope="module", params=[
#     ('Firefox', webdriver.Firefox), 
    ('PhantomJS', webdriver.PhantomJS),
])
def driver(request, base_url=BASE_URL):
    _driver = Driver(request.param, base_url)   
#     _driver.get('/')
    yield _driver
  
    if ec.errors:
        _driver.save_screenshot(str(datetime.today()) + '.png')
        allure
    _driver.quit()

# def pytest_runtest_makereport(item, call):
#     if call.excinfo is not None:
#         setattr(item, 'error', item)







     
