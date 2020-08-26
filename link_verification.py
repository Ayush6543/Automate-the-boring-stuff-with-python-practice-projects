# link_verification.py - given the url of a webpage download evey linked page.


import requests
import bs4

search_link = input('Which link you want to search? ')
url = 'http://www.' + search_link

res = requests.get(url)

try:
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    page_links = [link.get('href') for link in soup.select('a') if link.get('href')]

    for link in page_links:
        if link.startswith('http'):
            res1 = requests.get(link)

            try:
                res1.raise_for_status()
                print('Good link %s' % link)

            except Exception as Ex:
                print('Broken link %s' % link)

except Exception as ec:
    print('There was a problem %s' % ec)
