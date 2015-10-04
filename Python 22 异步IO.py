#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hina'

def A():
    print('1')
    print('2')
    print('3')

def B():
    print('x')
    print('y')
    print('z')

# 像多线程，但协程的特点在于是一个线程执行
# 最大的优势就是协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，
# 因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。
# 第二大优势就是不需要多线程的锁机制，
# 因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好了，
# 所以执行效率比多线程高很多

# 因为协程是一个线程执行，那怎么利用多核CPU呢？
# 最简单的方法是多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能

# Python对协程的支持是通过generator实现的

# 在generator中，我们不但可以通过for循环来迭代，还可以不断调用next()函数获取由yield语句返回的下一个值。

# 但是Python的yield不但可以返回一个值，它还可以接收调用者发出的参数

# consumer函数是一个generator，把一个consumer传入produce后

def consumer():
    r = ""
    while True:
        # consumer通过yield拿到消息，处理，又通过yield把结果传回；
        n = yield r
        if not n:
            return
        print("[CONSUMER] Consuming %s..." % n)
        r = "200 OK"

def produce(c):
    # 首先调用c.send(None)启动生成器；
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print("[PRODUCER] Producing %s..." % n)
        # 然后，一旦生产了东西，通过c.send(n)切换到consumer执行；
        r = c.send(n)
        # produce拿到consumer处理的结果，继续生产下一条消息；
        print("[PRODUCER] Consumer return: %s" % r)
    # produce决定不生产了，通过c.close()关闭consumer，整个过程结束。
    c.close()

c = consumer()
produce(c)

# 整个流程无锁，由一个线程执行，
# produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务

# asyncio是Python 3.4版本引入的标准库，直接内置了对异步IO的支持
# asyncio的编程模型就是一个消息循环。
# 我们从asyncio模块中直接获取一个EventLoop的引用，
# 然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。

import asyncio

@asyncio.coroutine
def hello():
    print("Hello world!")
    r = yield from asyncio.sleep(1)
    print("Hello again!")
#loop = asyncio.get_event_loop()
#loop.run_until_complete(hello())
#loop.close()

"""
loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
# 两个coroutine是由同一个线程并发执行的
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
"""

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()
"""
loop3 = asyncio.get_event_loop()
tasks3 = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop3.run_until_complete(asyncio.wait(tasks3))
loop3.close()
"""
# asyncio提供了完善的异步IO支持；
# 异步操作需要在coroutine中通过yield from完成；
# 多个coroutine可以封装成一组Task然后并发执行。

# asyncio可以实现单线程并发IO操作。
# 如果仅用在客户端，发挥的威力不大。
# 如果把asyncio用在服务器端，例如Web服务器，由于HTTP连接就是IO操作，
# 因此可以用单线程+coroutine实现多用户的高并发支持。
# asyncio实现了TCP、UDP、SSL等协议，
#
# aiohttp则是基于asyncio实现的HTTP框架。
# pip install aiohttp

import asyncio
from aiohttp import web

def index(request):
    return web.Response(body=b"<h1>Index</h1>")
def hello(request):
    yield from asyncio.sleep(0.5)
    text = "<h1>hello, %s!</h1>" % request.match_info["name"]
    return web.Response(body=text.encode("utf-8"))
@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route("GET", "/", index)
    app.router.add_route("GET", "/hello/{name}", hello)
    srv = yield from loop.create_server(app.make_handler(), "127.0.0.1", 8000)
    print("Server started at http://127.0.0.1:8000...")
    return srv
loop=asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
