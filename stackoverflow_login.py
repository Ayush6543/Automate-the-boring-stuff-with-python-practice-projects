from selenium import webdriver

browser = webdriver.Chrome('C:\\Users\\chromedriver.exe')
browser.get('http://www.stackoverflow.com/users/login')
email_elem = browser.find_element_by_id('email').send_keys('your email')
browser.find_element_by_id('password').send_keys('your password')
browser.find_element_by_id('submit-button').click()
