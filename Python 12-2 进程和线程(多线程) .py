#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hina'

import time, threading

def loop():
    # 它永远返回当前线程的实例
    print("thread %s is running..." % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print("thread %s >>> %s" % (threading.current_thread().name, n))
        time.sleep(1)
    print("thread %s ended." % threading.current_thread().name)

print("thread %s is running..." % threading.current_thread().name)

t = threading.Thread(target=loop, name="LoopThread")
# 子线程的名字在创建时指定
# 如果不起名字Python就自动给线程命名为Thread-1，Thread-2……

t.start()
t.join()
print("thread %s ended." % threading.current_thread().name) # 主线程实例的名字叫MainThread

balance = 0
def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n
def run_thread0(n):
    for i in range(100000):
        change_it(n)
lock = threading.Lock()
def run_thread(n):
    for i in range(100000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

import threading, multiprocessing
def loop():
    x = 0
    while True:
        x = x * 1
for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()

# 启动与CPU核心数量相同的N个线程，在4核CPU上可以监控到CPU占用率仅有102%，也就是仅使用了一核。
# 用C、C++或Java来改写相同的死循环，直接可以把全部核心跑满
# 因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，
# 任何Python线程执行前，必须先获得GIL锁，
# 然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。
# 这个GIL全局锁实际上把所有线程的执行代码都给上了锁，
# 所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。
# Python虽然不能利用多线程实现多核任务，
# 但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁

# 多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。

# Python解释器由于设计时有GIL全局锁，
# 导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。
