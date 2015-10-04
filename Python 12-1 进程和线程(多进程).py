#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hina'

"""
import os
print("process (%s) start..." % os.getpid())
pid = os.fork()
if pid == 0:
    print("I am child process (%s) and my parent is %s." % (os.getpid(), os.getppid()))
else:
    print("I (%s) just created a child process (%s).") % (os.getpid(), pid)
"""

# 如果你打算编写多进程的服务程序，Unix/Linux无疑是正确的选择。
# 由于Windows没有fork调用

# 由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。
# multiprocessing模块就是跨平台版本的多进程模块

from multiprocessing import Process
import os

def run_proc(name):
    print("Run child process")

"""
if __name__ == "__main__":
    print("Parent process %s." % os.getpid())
    p = Process(target = run_proc, args = ("test", ))
    print("Child process will start.")
    p.start()
    p.join()# 等待子进程结束后再继续往下运行，通常用于进程间的同步
    print("Child process end.")
"""

# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print("Run task %s (%s) ..." % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print("Task %s runs %0.2f seconds." % (name, (end - start)))
"""
if __name__ == "__main__":
    print("Parent process %s." % os.getpid())
    p = Pool() # 默认大小是CPU的核数 Pool(9)就可以同时跑了
    for i in range(9):
        p.apply_async(long_time_task, args = (i, ))
    print("Waiting for all subprocesses done...")

    p.close() # 调用join()之前必须先调用close()
    # 调用close()之后就不能继续添加新的Process了

    p.join() # 等待所有子进程执行完毕

    print("All subprocesses done.")
"""
# 请注意输出的结果，task 0，1，2，3是立刻执行的，
# 而task 4要等待前面某个task完成后才执行，这是因为Pool的默认大小在我的电脑上是4，
# 因此，最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制

# 子进程
# subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出
import subprocess
print("$ nelookup www.python.org")
r = subprocess.call(["nslookup", "www.python.org"])
print("Exit code:", r)

# 果子进程还需要输入，则可以通过communicate()方法输入
print("$ nslookup")
p = subprocess.Popen(["nslookup"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b"set q=mx\npython.org\nexit\n")
#print(output.decode("utf-8")) windows 跑不了
print("Exit code:", p.returncode)

# 进程间通信
from multiprocessing import Process, Queue
import os, time, random

def write(q):
    print("Process to write: %s" % os.getpid())
    for value in ['A', 'B', 'C']:
        print("Put %s to queue..." % value)
        q.put(value)
        time.sleep(random.random())
def read(q):
    print("Process to read: %s" % os.getpid())
    while True:
        value = q.get(True)
        print("Get %s from queue." % value)
if __name__ == "__main__":
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate() #  pr进程里是死循环，无法等待其结束，只能强行终止:

# 在Unix/Linux下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节。
# 由于Windows没有fork调用，
# 因此，multiprocessing需要“模拟”出fork的效果，
# 父进程所有Python对象都必须通过pickle序列化再传到子进程去，
# 所以，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了

# 在Unix/Linux下，可以使用fork()调用实现多进程。

# 要实现跨平台的多进程，可以使用multiprocessing模块。

# 进程间通信是通过Queue、Pipes等实现的。
