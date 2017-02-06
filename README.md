# Wikipedia_title_dataset
This is an implementation for crawling the title and its corresponding categories of an Wikipedia page.
The crawler will crawl the categories according to category_list_lang.txt 

The dataset is already in the folder acl2017_data.

with the following command 

python crawl.py -l zh -n 100000
python crawl.py -l ja -n 100000
python crawl.py -l ko -n 100000

Running the crawler again will cover the data in the folder.


# Usage
python crawl.py [-h] -l LANG -n NUM 

optional arguments:

  -h, --help            show this help message and exit
  
  -l LANG, --lang LANG  which language to crawl [zh, ja, ko]
  
  -n NUM, --num NUM     the minimun number of pages you wish to crawl for each category (may not be able to reach this number)
