import sys
import unittest
from config import Config
from base_test_case import BaseTestCase
from tests import TestCase

 
BaseTestCase.browser = Config.default_browser

if len(sys.argv) == 2:
    browser = sys.argv[1]
    print('browser:', browser)
    if browser in Config.browsers:
        BaseTestCase.browser = Config.browsers[browser]

suite = unittest.TestSuite()
for l, p in Config.auth.items():
    suite.addTest(BaseTestCase.parametrize(TestCase, auth={l: p}))
# unittest.TextTestRunner(verbosity=2).run(suite)
unittest.TextTestRunner().run(suite)
