# 2048.py- A game in which you will score points by moving tiles.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from time import sleep

print('Opening 2048 game...')
browser = webdriver.Chrome('C:\\Users\\chromedriver.exe')
browser.get('https://play2048.co/')
game_console = browser.find_element_by_css_selector('html')
sleep(2)
gameStatusElem = browser.find_element_by_css_selector('.game-container p')
while True:
    game_console.send_keys(Keys.UP)
    game_console.send_keys(Keys.DOWN)
    game_console.send_keys(Keys.RIGHT)
    game_console.send_keys(Keys.LEFT)

