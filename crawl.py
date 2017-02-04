import os
import math
import sys
import argparse

if __name__ == '__main__':



    parser = argparse.ArgumentParser()
    parser.add_argument('-l','--lang', help='which language to crawl', required=True)
    parser.add_argument('-n','--num', type=int, help='the number of pages to crawl for each category', required=True)
    parser.add_argument('-d','--dir', type=int, help='directory to save the crawled files', required=True)
    args = vars(parser.parse_args())
    lang = args['lang']
    num = args['num']
    directory = args['dir']

    if not os.path.exists(directory):
        os.makedirs(directory)
    
    #Crawling wiki
    print "Crawling..." + lang + " wikipedia"
    os.system('python WikiCrawler.py -l ' + lang + ' -n ' + str(num))

    #raw dictionary to txt file
    print "Raw to Format..."
    os.system('python raw2format.py -l ' + lang)



    
