class MainPage():

    def __init__(self, driver):
        self.driver = driver
        
        self.username_actionlink_id = 'team_menu_user_name'
        
        self.signout_actionlink_xpath = '//li[@id="logout"]//span[contains(text(),"Sign out")]'