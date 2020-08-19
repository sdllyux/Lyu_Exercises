# encoding: utf-8
"""
@author: IanLyu
@contact: sdllyux@163.com
@software: PyCharm
@file: CutPicture.py
@time: 2020/8/18 9:38

"""
from pathlib import Path
from PIL import Image


def modify_imgsize(fileUrl):
    p = Path(fileUrl)

    # 获取文件名
    ImgFileList = list(p.glob('*.jpg'))
    ImgFileList.extend(list(p.glob('*.png')))

    for filename in ImgFileList:
        img = Image.open(filename)
        # 获取图片大小
        (x, y) = img.size
        if x > 640 or y > 1136:
            # 进行大小修改
            x_s = 640
            y_s = 1136
            newimg = img.resize((x_s, y_s), Image.ANTIALIAS)  # 修改大小
            path1 = "E:\Image\\"
            newimg.save(path1 + 'new_' + filename.name, 'jpeg')
            print("This picture was modified:" + filename.name)
        else:
            print("This picture is availabe:" + filename.name)


if __name__ == '__main__':
    modify_imgsize('E:\Image')
