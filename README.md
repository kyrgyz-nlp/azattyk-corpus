# Project Name

A scraper that collects article texts from Azattyk.org

## Installation

Create a virtual environment:

```bash
python3 -m venv env
```

Activate the virtual environment:

```bash
source env/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required packages.

```bash
pip install -r requirements.txt
```

## Usage

0. See if articles_urls folder already has files with article URLs (there might be new artciles on the website since 01.05.2023). If you are OK with them, skip the following steps and use the URLs in your crawlers. In case you want to refresh the URLs, follow the instructions given below.

1. Run opera proxy (Azattyk is blocked in Kyrgyzstan). You might want to install Golang and build an executable for your platform. Checkout the project [repo](https://github.com/Snawoot/opera-proxy), it contains binary files for popular platforms.

```
./opera-proxy
```

2. Pull sitemap URLs from the main sitemap:

```python
python scripts/get_sitemaps_from_root.py
```

3. Pull article URLs from secondary sitemaps:

```python
python scripts/get_article_urls_from_sitemaps.py
```

4. Use URLs from articles_urls in your spider to collect article texts.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

TBD
