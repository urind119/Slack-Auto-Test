class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        
        self.signin_link_xpath = '//header//a[text()="Sign in"]'
        self.domain_textbox_id = 'domain'
        self.submit_button_id = 'submit_team_domain'
        
    def click_signin(self):
        self.driver.find_element_by_xpath(self.signin_link_xpath).click()
        
    def enter_domain(self, domain):
        self.driver.find_element_by_id(self.domain_textbox_id).clear()
        self.driver.find_element_by_id(self.domain_textbox_id).send_keys(domain)
        
    def click_submit(self):
        self.driver.find_element_by_id(self.submit_button_id).click()
        
    def verify_domain(self, domain_url):
        assert domain_url in self.driver.current_url