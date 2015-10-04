#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hina'

import threading

# 全局变量local_school就是一个ThreadLocal对象
local_school = threading.local()

def process_student():
    std = local_school.student
    print("Hello, %s (in %s)" % (std, threading.current_thread().name))

def process_thread(name):
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread, args=("Alice",), name="Thread-A")
t2 = threading.Thread(target=process_thread, args=("Bob",), name="Thread-B")
t1.start()
t2.start()
t1.join()
t2.join()

# 一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。
# ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。
