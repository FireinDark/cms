#!/usr/bin/env python  
# -*- coding: utf-8 -*- 

""" 
@version: v1.0 
@author: FireInDark
@contact: 993378951@qq.com 
@software: PyCharm 
@file: send.py 
@time: 2017/11/20 21:09 
"""  
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

channel = connection.channel()

channel.queue_declare(queue="hello")

channel.basic_publish(exchange='',
                      routing_key="hello",
                      body="hello world!")

print "[x] Sent 'Hello World!"

connection.close()
