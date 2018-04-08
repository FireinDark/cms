#!/usr/bin/env python  
# -*- coding: utf-8 -*- 

""" 
@version: v1.0 
@author: FireInDark
@contact: 993378951@qq.com 
@software: PyCharm 
@file: reciv.py 
@time: 2017/11/20 21:09 
"""  

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

channel = connection.channel()

channel.queue_declare(queue="hello")

def callback(ch, method, properties, body):
    print "[x] Received %r" % (body,)

channel.basic_consume(callback, queue="hello", no_ack=True)

print "[*] Waiting for messages. To exit press Ctrl+C"

channel.start_consuming()