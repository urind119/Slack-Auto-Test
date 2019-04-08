import time
import unittest
import HtmlTestRunner
from selenium import webdriver
from POM.Pages.loginPage import LoginPage

class LoginTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='/Users/wind/chromedriver/chromedriver')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_login_by_valid_account(self):
        driver = self.driver
        driver.get('https://slack.com')
        login = LoginPage(driver)
        
        domain_name = 'loctesting'
        domain_url = 'https://' + domain_name + '.slack.com/'
        
        login.click_signin()
        login.enter_domain(domain_name)
        login.click_submit()
        login.verify_domain(domain_url)
        
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/wind/eclipse-workspace/SlackAutoTest/POM/Report'))