import io
import gzip
import requests
from bs4 import BeautifulSoup as Soup
from helpers import get_sitemap_from_url


def unarchive_gz_file(file_content):
    with gzip.GzipFile(fileobj=io.BytesIO(file_content)) as uncompressed:
        return uncompressed.read()


def parse_sitemap(content):
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


def parse_articles_sitemap(content):
    soup = Soup(content)
    urls = soup.find_all('url')
    if not urls:
        return False
    out = []
	#extract what we need from the url
    for u in urls:
        loc = u.find('loc').string
        prio = u.find('priority').string
        change = u.find('changefreq').string
        last = u.find('lastmod').string
        out.append([loc, prio, change, last])
    return out


def get_content_from_local_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    return content


def save_sitemap_to_folder(sitemap, folder_path):
    encoding = 'utf-8'
    with open(folder_path, 'w', encoding=encoding) as f:
        f.write(sitemap.decode(encoding))


def parse_filename(url):
    return url.split('/')[-1].split('.')[0]


def main():
    sitemaps_urls = get_content_from_local_file('sitemap_urls.txt').split('\n')
    for url in sitemaps_urls:
        file_prefix = parse_filename(url)
        file_path = f"sitemaps/{file_prefix}.xml"
        content = get_sitemap_from_url(url)
        sitemap = unarchive_gz_file(content)
        save_sitemap_to_folder(sitemap, file_path)
        urls = parse_articles_sitemap(sitemap)
        if not urls:
            print('There was an error!')
        txt_filename = f'articles_urls/urls_{file_prefix}.txt'
        with open(txt_filename, 'w') as out:
            for u in urls:
                out.write('\t'.join(u) + '\n')


if __name__ == '__main__':
    main()
