# encoding: utf-8
"""
@author: IanLyu
@contact: sdllyux@163.com
@software: PyCharm
@file: ActivationCode.py
@time: 2020/8/17 13:18

"""
import random
import string


def get_key(length):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for i in range(length))


def save_key(content):
    f = open('C:\\Users\\p0152550\\Desktop\\key.txt', 'a')
    f.write(content)
    f.write('\n')
    f.close()


# 程序入口
if __name__ == '__main__':
    for i in range(200):
        value = get_key(20)
        print(value)
        save_key(value)
