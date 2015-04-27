# coding: utf-8
# py.test --alluredir [path_to_report_dir]
import pytest
import allure
# https://github.com/allure-framework/allure-python
from allure.utils import Severity
# py.test my_tests/ --allure_severities=critical,blocker
#     BLOCKER = 'blocker'
#     CRITICAL = 'critical'
#     NORMAL = 'normal'
#     MINOR = 'minor'
#     TRIVIAL = 'trivial'


@pytest.fixture
def f():
    return 'test'


@allure.step
def test_01():
    allure.attach('attach_title', 'attach_content')


@allure.step('another unuseful step')
def test_02(f):
    print(f)


@allure.feature('Feature1')
@allure.story('Story1')
@allure.severity(Severity.MINOR)
def test_minor():
    assert False


@allure.feature('Feature2')
@allure.story('Story2', 'Story3')
@allure.story('Story4')
@allure.severity(Severity.CRITICAL)
class TestBar:

    def test_bar(self):
        pass

    @allure.severity(Severity.BLOCKER)
    def test_bar_2(self):
        pass

# py.test my_tests/ --allure_features=feature1,feature2 --allure_stories=story1,story2


@allure.issue('http://jira.lan/browse/ISSUE-2')
def test_f():
    pass


@allure.testcase('http://my.tms.org/browse/TESTCASE-2')
def test_f():
    pass
