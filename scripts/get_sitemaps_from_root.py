from helpers import parse_top_level_sitemap
from helpers import get_sitemap_from_url


if __name__ == '__main__':
    url = 'https://www.azattyk.org/sitemap.xml'
    content = get_sitemap_from_url(url)
    urls = parse_top_level_sitemap(content)
    if not urls:
        print('There was an error!')
    with open('sitemap_urls.txt', 'w') as out:
        for u in urls:
            out.write(u + '\n')
