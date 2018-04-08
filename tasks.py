#!/usr/bin/env python  
# -*- coding: utf-8 -*- 

""" 
@version: v1.0 
@author: FireInDark
@contact: 993378951@qq.com 
@software: PyCharm 
@file: tasks.py
@time: 2017/11/20 19:18 
"""  
import time
from celery import Celery

app = Celery('tasks',backend="amqp", broker="amqp://guest@localhost//")

@app.task
def add(x, y):
    time.sleep(5)
    return x+y

# if __name__ == '__main__':
#     add.delay(1, 2)