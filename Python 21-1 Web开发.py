#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hina'

# 为什么要使用Chrome浏览器而不是IE呢？因为IE实在是太慢了，并且，IE对于开发和调试Web应用程序完全是一点用也没有。

# 我们需要在浏览器很方便地调试我们的Web应用，而Chrome提供了一套完整地调试工具，非常适合Web开发。

# WSGI：Web Server Gateway Interface

def application(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/html")])
    return [b"<h1>Hello, web!</h1>"]

def application2(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/html")])
    body = "<h1>Hello, %s!</h1>" % (environ["PATH_INFO"][1:] or "Web")
    return [body.encode("utf-8")]

# Python内置了一个WSGI服务器，这个模块叫wsgiref，它是用纯Python编写的WSGI服务器的参考实现。
# 所谓“参考实现”是指该实现完全符合WSGI标准，但是不考虑任何运行效率，仅供开发和测试使用。

from wsgiref.simple_server import make_server

httpd = make_server("", 8000, application2)
print("Serving HTTP on port 8000...")
httpd.serve_forever()

# 无论多么复杂的Web应用程序，入口都是一个WSGI处理函数。HTTP请求的所有输入信息都可以通过environ获得，
# HTTP响应的输出都可以通过start_response()加上函数返回值作为Body。

# 复杂的Web应用程序，光靠一个WSGI函数来处理还是太底层了，
# 我们需要在WSGI之上再抽象出Web框架，进一步简化Web开发。
