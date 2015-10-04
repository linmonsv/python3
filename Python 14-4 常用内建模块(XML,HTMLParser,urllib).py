#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hina'

from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print("sax:start_element: %s, attrs： %s" % (name, str(attrs)))
    def end_element(self, name):
        print("sax:end_element: %s" % name)
    def char_dataA(self, text):
        print("sax:char_data: %s" % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_dataA
parser.Parse(xml)

# 99%的情况下需要生成的XML结构都是非常简单的，因此，最简单也是最有效的生成XML的方法是拼接字符串
L = []
L.append(r'<?xml version="1.0"?>')
L.append(r'<root>')
L.append(('some & data'))
L.append(r'</root>')
print("".join(L))

# 如果要生成复杂的XML呢？建议你不要用XML，改成JSON
# 解析XML时，注意找出自己感兴趣的节点，响应事件时，把节点数据保存起来。解析完毕后，就可以处理数据

# http://weather.yahooapis.com/forecastrss?u=c&w=2161853
# 解析天气预报

from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
# feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，可以一部分一部分塞进去。
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')

# 特殊字符有两种，一种是英文表示的&nbsp;，一种是数字表示的&#1234;，
# 这两种字符都可以通过Parser解析出来。

# 找一个网页，例如https://www.python.org/events/python-events/，
# 用浏览器查看源码并复制，然后尝试解析一下HTML，输出Python官网发布的会议时间、名称和地点

# urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应：
from urllib import request

with request.urlopen("https://api.douban.com/v2/book/2129650") as f:
    data = f.read()
    print("Status:", f.status, f.reason)
    for k, v in f.getheaders():
        print("%s: %s" % (k, v))
    print("Data:", data.decode("utf-8"))

# 如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，
# 通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器

# 模拟iPhone 6去请求豆瓣首页
req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
# 这样豆瓣会返回适合iPhone的移动版网页

# 如果要以POST发送一个请求，只需要把参数data以bytes形式传入
# 我们模拟一个微博登录，
# 先读取登录的邮箱和口令，
# 然后按照weibo.cn的登录页的格式以username=xxx&password=xxx的编码传入

from urllib import request, parse

print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent',
               'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer',
               'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

# 如果还需要更复杂的控制，比如通过一个Proxy去访问网站，我们需要利用ProxyHandler来处理
proxy_handler = request.ProxyHandler({'http': 'http://www.example.com:3128/'})
proxy_auth_handler = request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = request.build_opener(proxy_handler, proxy_auth_handler)
with opener.open('http://www.example.com/login.html') as f:
    pass

# urllib提供的功能就是利用程序去执行各种HTTP请求。
# 如果要模拟浏览器完成特定功能，需要把请求伪装成浏览器。
# 伪装的方法是先监控浏览器发出的请求，再根据浏览器的请求头来伪装，
# User-Agent头就是用来标识浏览器的

# 利用urllib读取XML，将XML一节的数据由硬编码改为由urllib获取
