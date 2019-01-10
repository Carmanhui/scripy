# -*- coding:utf-8 -*-
"""@author:CMH
@file:picture_download.py
@time:2018/3/21 002110:16
"""
import requests
import re
import urllib
import os

for m in range(1,13):
    url = 'http://www.ivsky.com/bizhi/nvxing/index_'+str(m)+'.html'
    html = requests.get(url)
    print(html.text)
    pattern=re.compile('<div class="il_img">.*?<p><a href="(.*?)" target="_blank">(.*?)</a></p>',re.S)
    items= re.findall(pattern,html.text)
    print(items)
    for lib in items:
        num = 0
        url2 = 'http://www.ivsky.com'+lib[0]
        os.mkdir('./img/'+lib[1])
        print(url2)
        html2 = requests.get(url2)
        pattern2 = re.compile('<div class="il_img">.*?img src="(.*?)" alt.*?</a></p></li>', re.S)
        items2 = re.findall(pattern2, html2.text)

        print(items2)
        for mm in items2:
            mm = mm.replace('/t','/pre')
            print(mm)
            urllib.request.urlretrieve(mm,'C:\\Users\\Administrator\\Desktop\\图片爬虫\\img\\'+lib[1]+'\\'+str(num)+'.jpg')
            num+=1