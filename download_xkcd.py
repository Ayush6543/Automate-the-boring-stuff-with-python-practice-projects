# ! python3
# download.py - Downloads every single XKCD comic.

import requests, bs4, os

# starting url
url = 'http://xkcd.com'
# store comics in ./xkcd
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find the URL of the comic image.

    # Download the image.
    comic_elem = soup.select('#content img')
    if comic_elem == []:
        print('Could not find comic image.')
    else:
        comic_url = comic_elem[0].get('src').strip('http://')
        comic_url = 'http://' + comic_url
        # Download the image.
        print('Downloading image %s...' % comic_url)
        res = requests.get(comic_url)
        res.raise_for_status()

    # Save the image to ./xkcd
    image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
    for chunk in res.iter_content(100000):
        image_file.write(chunk)
    image_file.close()

    # Get the Prev button's url.
    prev_link = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prev_link.get('href')

print('Done')
