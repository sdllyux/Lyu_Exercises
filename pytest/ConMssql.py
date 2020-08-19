# encoding: utf-8
"""
@author: IanLyu
@contact: sdllyux@163.com
@software: PyCharm
@file: ConMssql.py
@time: 2020/8/17 14:54

"""
import collections
import re

path = 'test.txt'
with open(path, 'r') as f:
    word_list = []
    word_reg = re.compile(r'\w+')
    for line in f:
        line_words = line.split()
        word_list.extend(line_words)

    words_dict = dict(collections.Counter(word_list))  # 使用Counter统计
    for k, v in words_dict.items():
        print(k, v)
