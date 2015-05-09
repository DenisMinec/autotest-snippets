from selenium.webdriver.common.by import By


class BasePage(object):
    
    def __init__(self, driver):
        self.driver = driver

    def type(self, selector, text):
        self.driver.find_element(*selector).send_keys(text)

    def click(self, selector):
        self.driver.find_element(*selector).click()
    

class LoginPage(BasePage):
    
    # locators
    # it is possible to separate locators and define another class
    LOGIN_FIELD = (By.XPATH, "//input[@name='username']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@type='submit']")
    
    # private methods
    def _type_login(self, login):
        self.type(self.LOGIN_FIELD, login)
        
    def _type_password(self, password):
        self.type(self.PASSWORD_FIELD, password)
        
    def _click_login_button(self):
        self.click(self.LOGIN_BUTTON)
    
    # public methods    
    def is_title_matches(self):
        return 'Login Page' in self.driver.title
    
    def login(self, login, password):
        self._type_login(login)
        self._type_password(password)
        self._click_login_button()
