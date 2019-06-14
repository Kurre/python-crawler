#!/usr/bin/python
# filename: run.py
import re
from crawler import Crawler, CrawlerCache

if __name__ == "__main__":
    # Using SQLite as a cache to avoid pulling twice
    crawler = Crawler()
    root_re = re.compile('^/$').match
    crawler.crawl('https://some-site.net/', no_cache=root_re)
    print(crawler.content['some-site.net'].keys())
