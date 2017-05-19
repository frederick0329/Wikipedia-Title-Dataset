# Wikipedia_title_dataset
This repo consists of the data used for acl 2017 

[Learning Character-level Compositionality with Visual Features](https://arxiv.org/abs/1704.04859)

This is an implementation for crawling the title and its corresponding categories of an Wikipedia page.

The crawler will crawl the categories according to category_list_lang.txt 

The dataset is already crawled in the folder acl2017_data

with the following command:  
```
python crawl.py -l zh -n 100000

python crawl.py -l ja -n 100000

python crawl.py -l ko -n 100000
```
Running the crawler again will cover the data in the folder.


# Usage
```
python crawl.py [-h] -l LANG -n NUM 
```
optional arguments:

  -h, --help            show this help message and exit
  
  -l LANG, --lang LANG  which language to crawl [zh, ja, ko]
  
  -n NUM, --num NUM     the minimun number of pages you wish to crawl for each category (may not be able to reach this number)

# Data split
The data split and the code for the paper can be found in this [repo](https://github.com/frederick0329/Learning-character-level/)
