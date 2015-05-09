import os
import unittest
from datetime import datetime
from config import Config


class BaseTestCase(unittest.TestCase):
    
    browser = None

    @classmethod
    def setUpClass(cls, url=Config.base_url):
        cls.driver = cls.browser()
#         cls.driver.get(url)
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        
    def tearDown(self):
        for tc, e in self._outcome.errors:
            if e:
                dir_name = os.path.join(self.driver.name + ' - ' + str(tc))
                file_path = os.path.join(dir_name, str(datetime.today()) + '.png')
                if not os.path.exists(dir_name):
                    os.mkdir(dir_name)
                
                self.driver.save_screenshot(file_path)

    def __init__(self, methodName='runTest', **kwargs):
        super(BaseTestCase, self).__init__(methodName)
        for p, v in kwargs.items():
            setattr(self, p, v)   

    @staticmethod
    def parametrize(test_case_class, **kwargs):
        test_loader = unittest.TestLoader()
        test_names = test_loader.getTestCaseNames(test_case_class)
        suite = unittest.TestSuite()
        for name in test_names:
            suite.addTest(test_case_class(name, **kwargs))
        return suite
