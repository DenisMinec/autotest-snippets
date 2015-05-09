from selenium import webdriver


class Config(object):

    default_browser = webdriver.PhantomJS

    browsers = {
        "firefox": webdriver.Firefox, 
        "chrome": webdriver.Chrome, 
        "phantomjs": webdriver.PhantomJS,
    }

    base_url = 'http://ya.ru'

    auth = {
        'test': 'test',
        'test2': 'test2',
    }

