# encoding: utf-8
"""
@author: IanLyu
@contact: sdllyux@163.com
@software: PyCharm
@file: urls.py.py
@time: 2020/8/19 15:56

"""
from django.urls import path

from hrs import views

urlpatterns = [
    path('', views.index, name='index'),
]
