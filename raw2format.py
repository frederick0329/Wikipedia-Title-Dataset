#!/usr/bin/env python
# encoding: utf-8

import json
import io
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-l','--lang', help='which language to crawl', required=True)
args = vars(parser.parse_args())


def raw2format(lang):
    inFile = './acl2017_data/' + lang + '_raw.txt'
    outFile = './acl2017_data/' + lang + '.txt'
    fo = open(outFile, 'w')
    category_count = {}
    pattern = re.compile('.*:.*')
    with io.open(inFile, 'r', encoding='utf-8') as fi:
        lines = fi.readlines()
        for i, line in enumerate(lines):
            data = json.loads(line.rstrip('\n'))
            #for i in xrange(len(data)):
            count = 0
            for d in data:
                #print d["title"]
                if not pattern.match(data[d]['title']):
                    if data[d]["category"] not in category_count:
                        category_count[data[d]["category"]] = 0
                    category_count[data[d]["category"]] += 1
                    fo.write(str(data[d]["category"]).decode('utf-8'))
                    fo.write("\t".decode('utf-8'))
                    fo.write(data[d]["title"].encode('utf8'))
                    fo.write("\n".decode('utf-8'))
                    #pid.add(d["pageid"])
                    count += 1
    print "category distribution for " + lang + " "
    print category_count
    fo.close() 
                        
                

if __name__ == '__main__':
    base_dict = {'en' : 'https://en.wikipedia.org/',
                 'zh' : 'https://zh.wikipedia.org/',
                 'ja' : 'https://ja.wikipedia.org/', 
                 'ko' : 'https://ko.wikipedia.org/'}
    lang = args['lang']
    raw2format(lang)
