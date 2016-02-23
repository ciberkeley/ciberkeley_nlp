
# coding: utf-8

# In[1]:

import scipy
import pandas as pd
import numpy as np
import math
import pymongo
import MySQLdb as sql
import _mysql
import random
import csv
import time
import re
import matplotlib.pyplot as plt; import matplotlib.pylab as pylab
#%matplotlib inline
pd.options.display.mpl_style = 'default'
pylab.rcParams['figure.figsize'] = 12, 6
from dateutil import parser
import Quandl
from pymongo import MongoClient
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import urllib2


# ## Get A BeautifulSoup Object

# In[11]:

def get_search_soup(text):
    url =  ('http://www.bloomberg.com/search?query=' + str(text))
    soup = get_soup(url)
    return soup
def get_soup(url):
    page = urllib2.urlopen(url).read()
    soup = BeautifulSoup(page)
    return soup
def get_search_page_links(soup):
    article_list = []
    for item in soup.find_all('h1'):
        try:
            if 'video' in item.a['href']:
                #print 'Video Link Skipped: ' + item.a['href']
                continue
            if 'http' in item.a['href']:
                #print item.a['href']
                article_list.append(item.a['href'])
            else:
                #print 'http://www.bloomberg.com/' + item.a['href']
                article_list.append('http://www.bloomberg.com/' + item.a['href'])
        except:
            continue
    return article_list
def get_text_body(article_url):
    final_text = ""
    soup = get_soup(article_url)
    query = soup.find_all('div',  class_="article-body__content")
    for item in query:
        for text in item.find_all('p'):
            final_text = final_text + '\n\n' + str(text.text.encode('utf-8'))
    return final_text


# In[12]:

soup = get_search_soup('apple')


# In[13]:

url_list = get_search_page_links(soup)
temp = get_text_body(url_list[1])
print temp


# In[ ]:




# In[ ]:




# In[ ]:



