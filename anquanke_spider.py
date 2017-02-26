'''
@author: xiaoye
'''
#coding: utf-8
import requests
import re
from bs4 import BeautifulSoup
from optparse import OptionParser

import sys
reload(sys)
sys.setdefaultencoding('utf8')

cont = ''

parse = OptionParser()
parse.add_option('-o', '--out', dest='outfile', type='string', default='aqk_news.txt', help='output file')
(option, args) = parse.parse_args()

def doget(url, headers=''):
    try:
        r = requests.get(url, headers=headers, timeout=6)
        if r.status_code == 200:
            cont = r.content
        soup = BeautifulSoup(cont, 'lxml', from_encoding='utf-8')
        bqs = soup.find_all('li', class_='clearfix')
        #print bqs
        for bq in bqs:
            #print bq.get_text()
            b = bq.find('a', class_='title')
            print b.get_text()
            a = bq.find('p', class_='desc')
            print a.get_text().replace(u'\u200b', u' ') + '\n'
            with open(option.outfile, 'a') as f:
                f.write(b.get_text() + '\n' + a.get_text().replace(u'\u200b', u' ') + '\n')
    except:
        pass
   
if __name__ == "__main__":
    for i in range(1,5):
        ii = '%d' % i
        url = "http://bobao.360.cn/news/&page=" + ii
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
        doget(url, headers=headers)
