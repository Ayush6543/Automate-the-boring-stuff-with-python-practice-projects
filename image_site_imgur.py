# image_site_imgur.py - Downloads image from imgur.
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import requests
import bs4
import os

url = 'http://www.imgur.com'
print('Opening Imgur...')
search_word = input('Which word you wanna search? ')
browser = webdriver.Chrome('C:\\Users\\chromedriver.exe')
time.sleep(2)
browser.get(url)
search_input = browser.find_element_by_class_name('Searchbar-textInput')
search_input.send_keys(search_word)
search_input.send_keys(Keys.ENTER)

os.makedirs('imgur_downloader', exist_ok=True)

res = requests.get('http://imgur.com/search?q=' + ' ' + search_word)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")
matches = [img.find('img')['src'] for img in soup.find_all('a', attrs={'class': 'image-list-link'})]


dlurl = ['http:' + url for url in matches]
print(len(dlurl))
for link in dlurl:
    print('Downloading images %s...' % (link))
    res = requests.get(link)
    res.raise_for_status()

    imageFile = os.path.join('imgur_downloader', os.path.basename(link))
    with open(imageFile, 'wb') as f:
        for chunk in res:
            f.write(chunk)
print('Done')
