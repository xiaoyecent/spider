# spider
抓取 http://bobao.360.cn/news 新闻资讯 只抓了4页 有需要者可以改变for i in range(1,n)实现抓取n-1页

git clone https://github.com/xiaoyecent/spider/
```
Usage: anquanke_spider.py [options]

Options:
  -h, --help            show this help message and exit
  -o OUTFILE, --out=OUTFILE
                        output file

```

程序print在shell中  并写入文件 

-o支持自定义写入文件位置 默认为写入当前目录下一个文件内

---------------------------------------------------
---------------------------------------------------
aqk_spider_v2.0.py  其实就是换了种写法,把optparse换成了argparse

ubuntu&win 下测试正常  抓到的咨询保存到了txt里,已经上传

sudo python aqk_spider_v2.0.py -h
```
usage: aqk_spider_v2.0.py [-h] [-o OUTFILE]

anquanke spider by xiaoye

optional arguments:
  -h, --help            show this help message and exit
  -o OUTFILE, --output OUTFILE
                        outputfile

```
