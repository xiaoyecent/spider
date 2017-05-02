'''
@author: xiaoye
'''
#coding: utf-8
import requests
import re
from bs4 import BeautifulSoup as bs
from argparse import ArgumentParser

import sys
reload(sys)
sys.setdefaultencoding('utf8')

arg = ArgumentParser(description='anquanke spider by xiaoye')
arg.add_argument('-o', '--output', dest='outfile', help='outputfile', default='anquanke.txt')
result = arg.parse_args()

def spider(url='http://bobao.360.cn/news/&page=1'):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    r = requests.get(url, headers=headers, timeout=4)
    #print r.content
    soup = bs(r.content, 'lxml', from_encoding='utf-8')
    bqs = soup.find_all(name='li', attrs={'class':'clearfix'})
    for bq in bqs:
        #print bq.get_text()
        title = bq.div.find(name='a', attrs={'class':'title'})
        print title.get_text()
        content = bq.div.find(name='p', attrs={'class':'desc'})
        print content.get_text() + '\n'
        
        with open(result.outfile, 'a') as f:
            f.write(title.get_text() + '\n' + content.get_text() + '\n' + '\n')
    


if __name__ == '__main__':
    for i in range(1,5):
        url = 'http://bobao.360.cn/news/&page=' + str(i)
        spider(url)
