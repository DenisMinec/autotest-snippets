# coding: utf-8
from selenium import webdriver
import pytest
import allure
from allure.constants import AttachmentType


@pytest.yield_fixture(scope='session')
def driver():
    _driver = webdriver.PhantomJS()
    yield _driver
    _driver.quit()


def test_ya(driver):
    with allure.step('open ya.ru and take screenshot'):
        driver.get('http://ya.ru/')
        # driver.save_screenshot('screenshot.png')
        allure.attach('screenshot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)