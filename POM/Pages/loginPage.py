from POM.Pages.locators import Locators
from POM.Pages.mainPage import MainPage

class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        
        self.signin_link_xpath = '//header//a[text()="Sign in"]'
        self.domain_textbox_id = 'domain'
        self.submit_button_id = 'submit_team_domain'
        self.email_textbox_id = 'email'
        self.password_textbox_id = 'password'
        self.remember_checkbox_name = 'remember'
        self.signin_button_id = 'signin_btn'
        
    def click_signin_link(self):
        self.driver.find_element_by_xpath(self.signin_link_xpath).click()
        
    def enter_domain(self, domain):
        self.driver.find_element_by_id(self.domain_textbox_id).clear()
        self.driver.find_element_by_id(self.domain_textbox_id).send_keys(domain)
        
    def click_submit(self):
        self.driver.find_element_by_id(self.submit_button_id).click()
        
    def verify_domain(self, domain_url):
        assert domain_url in self.driver.current_url
        
    def enter_email(self):
        locators = Locators(self.driver)
        self.driver.find_element_by_id(self.email_textbox_id).send_keys(locators.email)
        
    def enter_password(self):
        locators = Locators(self.driver)
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(locators.password)
        
    def check_remember(self):
        self.driver.find_element_by_name(self.remember_checkbox_name).click()
        
    def click_signin(self):
        self.driver.find_element_by_id(self.signin_button_id).click()
        
    def verify_username(self, username):
        main = MainPage(self.driver)
        assert username in self.driver.find_element_by_id(main.username_actionlink_id).text