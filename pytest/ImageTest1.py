# encoding: utf-8
"""
@author: IanLyu
@contact: sdllyux@163.com
@software: PyCharm
@file: ImageTest1.py
@time: 2020/8/17 13:12

"""

from PIL import Image, ImageDraw, ImageFont

# 创建图片对象
headImage = Image.open('E:/Image/header.jpg')

# 获取图片对象的宽高
w, h = headImage.size

# 创建字体对象
font = ImageFont.truetype('C:/Windows/Fonts/msgothic.ttc', int(h / 4))

# 绘制圆形
ImageDraw.Draw(headImage).pieslice([(w / 3 * 2, 0), (w, h / 3)], 0, 360, fill='red')
ImageDraw.Draw(headImage).text((w * 0.65, h * 0.01), '呂航', font=font, fill='black')

# 展示绘制结果(使用系统默认的图片浏览器)
headImage.show()

# 保存绘制结果
headImage.save('E:/Image/wode.jpg')

