#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from signac.contrib.crawler import SignacProjectCrawler
from signac.contrib.crawler import MasterCrawler


class IdealGasProjectCrawler(SignacProjectCrawler):
    pass



def get_crawlers(root):
    return {'main': IdealGasProjectCrawler(os.path.join(root, 'workspace'))}


if __name__ == '__main__':
    master_crawler = MasterCrawler('.')
    for doc in master_crawler.crawl(depth=1):
        print(doc)