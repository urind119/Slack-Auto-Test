import time
import unittest
import HtmlTestRunner
from selenium import webdriver
from POM.Pages.locators import Locators
from POM.Pages.loginPage import LoginPage

class LoginTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='/Users/wind/chromedriver/chromedriver')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        
    def test_01_access_existing_domain(self):
        driver = self.driver
        locators = Locators(driver)
        login = LoginPage(driver)
        driver.get(locators.main_url)
        # actions
        login.click_signin_link()
        login.enter_domain(locators.domain_name)
        login.click_submit()
        login.verify_domain(locators.domain_url)
        time.sleep(2)

    def test_02_login_by_valid_account(self):
        driver = self.driver
        locators = Locators(driver)
        login = LoginPage(driver)
        # actions
        login.enter_email()
        login.enter_password()
        login.check_remember()
        login.click_signin()
        login.verify_username(locators.username)
        time.sleep(2)
        
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/wind/eclipse-workspace/SlackAutoTest/POM/Report'))