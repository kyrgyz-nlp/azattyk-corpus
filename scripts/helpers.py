import requests
from bs4 import BeautifulSoup as Soup

WINDOWS_10 = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36'


def get_sitemap_from_url(url):
    response = requests.get(url, headers={
        "User-Agent": WINDOWS_10,
        'Content-Type': 'text/html'
        })
    response.raise_for_status()
    
    # we didn't get a valid response, bail
    if 200 != response.status_code:
        return False
	
    return response.content


def parse_top_level_sitemap(content):
    soup = Soup(content)
    sitemaps_urls = soup.find_all('loc')
    if not sitemaps_urls:
        return False
    out = []
	#extract what we need from the url
    for u in sitemaps_urls:
        loc = u.string
        out.append(loc)
    return out
