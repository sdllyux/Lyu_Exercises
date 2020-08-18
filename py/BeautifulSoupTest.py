# encoding: utf-8
"""
@author: IanLyu
@contact: sdllyux@163.com
@software: PyCharm
@file: BeautifulSoupTest.py
@time: 2020/8/18 10:48

"""
import os

import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.baidu.com')
html = r.text  # 爬虫得到网站的html内容
soup = BeautifulSoup(html, 'html.parser')  # 标准解析库

# print(soup.title.string)  # 输出标题，前提是标题必须存在
body = str(soup.body)
print(body)  # 输出正文
if not os.path.exists('E:/IOTest'):  # 若文件目录不存在，则创建目录
    os.mkdir('E:/IOTest')
savingtxtmsg = open('E:/IOTest/IOTest.txt', 'a', encoding = 'utf-8')  # 获取文件对象
savingtxtmsg.write(body)  # 将body写入文件
savingtxtmsg.write('\n')
savingtxtmsg.close()
# print(soup.head)  # 输出head的内容
# print(soup.a)  # 输出a开头的内容
# print(soup.a['name'])  # 输出a的名字
# print(soup.a.string)  # 输出a的内容
# print(soup.prettify())    # 输出html内容

# for u in soup.findAll('a'):  # 打印链接
#     print(u['href'])
#
# for j in soup.findAll('img'):  # 打印链接
#     print(j['src'])
