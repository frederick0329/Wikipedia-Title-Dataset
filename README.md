# Wikipedia_title_dataset
This is an implementation for crawling the title and its corresponding categories of an Wikipedia page.
The crawler will crawl the categories according to category_list_lang.txt 

The dataset is already in the folder acl2017_data.
Running the crawler will cover the data in the folder.

# Usage
python crawl.py [-h] -l LANG -n NUM 

optional arguments:

  -h, --help            show this help message and exit
  
  -l LANG, --lang LANG  which language to crawl [zh, ja, ko]
  
  -n NUM, --num NUM     the minimun number of pages to crawl for each category
