#!/usr/bin/env python
# encoding: utf-8

import urllib2
import urllib
import json
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-l','--lang', help='which language to crawl', required=True)
parser.add_argument('-n','--num', type=int, help='the number of pages to crawl for each category', required=True)
args = vars(parser.parse_args())

recursion_limit = 950 #sys.getrecursionlimit()

def to_utf8(text):
    if isinstance(text, unicode):
        # unicode to utf-8
        return text.encode('utf-8')
    else:
        # maybe utf-8
        return text.decode('utf-8').encode('utf-8')

def crawl(base, category, limit, depth, data, category_idx, category_count, visited):
    if category_count[category_idx] >= limit or depth >= recursion_limit:
        return
    category = urllib.quote(to_utf8(category.replace(' ', '+')))
    query = '/w/api.php?action=query&format=json&prop=&list=categorymembers'+ \
            '&meta=&cmtitle='+category+'&cmprop=ids%7Ctitle%7Ctype'+ \
            '&cmtype=page%7Csubcat&cmlimit=max'
    url = base+query
    try:
        response = urllib.urlopen(url)
        pages = json.loads(response.read())
        if 'query' in pages and 'categorymembers' in pages['query']:
            pages = pages['query']['categorymembers']
            for page in pages:
                if page['pageid'] in visited:
                    continue
                visited.add(page['pageid'])
                if page['type'] == 'page':
                    pid = page['pageid']
                    if pid not in data:
                        data[pid] = {}
                        data[pid]['title'] = page['title']
                        data[pid]['category'] = category_idx
                        data[pid]['depth'] = depth
                        category_count[category_idx] += 1
                    else:
                        if data[pid]['depth'] > depth:
                            data[pid]['depth'] = depth
                            category_count[data[pid]['category']] -= 1
                            category_count[category_idx] += 1
                            data[pid]['category'] = category_idx
                elif page['type'] == 'subcat':
                    crawl(base, page['title'], limit, depth + 1, data, category_idx, category_count, visited)
    except urllib2.HTTPError: # 404, 500, etc..
        pass

def readCategoryFile(lang):
    inFile = 'category_list_' + args['lang'] + '.txt'
    fi = open(inFile, 'r')
    ret = []
    with open(inFile) as fi:
        lines = fi.readlines()
        for line in lines:
            cat = line.split()
            #ret.append([])
            #for sub in cat:
            ret.append('Category:' + cat[0])
    return ret             

if __name__ == '__main__':
    base_dict = {'en' : 'https://en.wikipedia.org/',
                 'zh' : 'https://zh.wikipedia.org/',
                 'ja' : 'https://ja.wikipedia.org/', 
                 'ko' : 'https://ko.wikipedia.org/'}
    lang = args['lang']
    limit = args['num']
    base = base_dict[lang]
    categories = readCategoryFile(lang)
    print categories
    outFile = lang + '_raw.txt'
    fo = open(outFile, 'w')
    data = {}
    category_count = []
    for i, category in enumerate(categories):
        category_count.append(0)
        visited = set()
        crawl(base, category, limit, 1, data, i, category_count, visited)
        print 'Current Cateogry Distribution after crawling ' + category + ': '
        print category_count
    json_string = json.dumps(data, ensure_ascii=False).encode('utf8')
    fo.write(json_string)
    fo.write('\n'.decode('utf-8'))
    fo.close()
