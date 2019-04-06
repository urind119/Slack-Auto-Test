# import webdriver
from selenium import webdriver
from _ast import Exec

# function to get an element
def getElements(method, value):
    cmd = 'driver.find_element_by_' + method + '(\'' + value + '\')'
    return eval(cmd);

# open browser
driver = webdriver.Chrome('/Users/wind/chromedriver/chromedriver')
driver.get('https://slack.com')

# sign-in button on banner
btnSignin = '//header//a[text()="Sign in"]'

# click Sign-in button
getElements("xpath", btnSignin).click()

# verify login page welcome text
lblLogin = '//h1[contains(text(),"Sign in to your workspace")]'
assert "Sign in to your workspace" in getElements("xpath", lblLogin).text
 
# input mail and click Continue
getElements("id", "domain").send_keys("loctesting")
getElements("id", "submit_team_domain").click()

# verify domain
domainUrl = 'https://' + domain + '.slack.com/'
assert domainUrl in driver.current_url

# exit
driver.quit()