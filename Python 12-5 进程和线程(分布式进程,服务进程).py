#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hina'

# Python的multiprocessing模块不但支持多进程
# 其中managers子模块还支持把多进程分布到多台机器上。
# 一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信

import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()
# 接收结果的队列
result_queue = queue.Queue()

# 从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass

# 把两个Queue都注册到网络上, callable参数关联了Queue对象
QueueManager.register("get_task_queue", callable=lambda : task_queue)
QueueManager.register("get_result_queue", callable=lambda : result_queue)

# 绑定端口5000, 设置验证码'abc'
manager = QueueManager(address=("", 5000), authkey=b"abc")

# 启动Queue
manager.start()

# 获得通过网络访问的Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()

# 放几个任务进去
for i in range(10):
    n = random.randint(0, 10000)
    print("Put task %d..." % n)
    task.put(n)

# 从result队列读取结果
print("Try get results...")
for i in range(10):
    r = result.get(timeout=10)
    print("Result: %s" % r)

# 关闭
manager.shutdown()
print("master exit.")

# Python的分布式进程接口简单，封装良好，适合需要把繁重任务分布到多台机器的环境下
# 注意Queue的作用是用来传递任务和接收结果，每个任务的描述数据量要尽量小。
# 比如发送一个处理日志文件的任务，就不要发送几百兆的日志文件本身，而是发送日志文件存放的完整路径，
# 由Worker进程再去共享的磁盘上读取文件。
