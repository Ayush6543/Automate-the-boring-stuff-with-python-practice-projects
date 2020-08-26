# ! python3
# lucky.py - Opens several Google search results.

import webbrowser, bs4, requests, sys

# Display the text while downloading the Google page
print('Googling...')

res = requests.get('http://www.google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Open a browser tab for each result.
linkElems = soup.select('a[href^="/url"]')
num_open = min(2, len(linkElems))

for i in range(num_open):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))

