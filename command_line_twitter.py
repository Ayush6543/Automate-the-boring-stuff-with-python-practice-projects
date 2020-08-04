# ! python3
# command_line_messaging - A program that takes a text on the command line
# log in to your account and sends

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys

print('Opening Twitter...')
time.sleep(2)
browser = webdriver.Chrome('C:\\Users\\chromedriver.exe')
browser.get('http://www.twitter.com')
time.sleep(5)
browser.find_element_by_link_text('Log in').click()
time.sleep(2)
usernameInput = browser.find_element_by_name("session[username_or_email]")
passwordInput = browser.find_element_by_name("session[password]")

usernameInput.send_keys('your email')
passwordInput.send_keys('your password')
passwordInput.send_keys(Keys.ENTER)

time.sleep(2)
tweet = browser.find_element_by_xpath('''//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div
                                                      /div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div
                                                      /div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div
                                                      /div/div/div''')


tweet.send_keys(sys.argv[1:])
tweet.send_keys(Keys.COMMAND, Keys.ENTER)
time.sleep(2)
autotw1 = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'DraftEditor-root')))
autotw1.click()

sendTw = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@role="button"]/div/span/span')))
sendTw.click()
