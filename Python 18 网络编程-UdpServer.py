#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hina'

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("127.0.0.1", 9999))
print("Bind UDP on 9999...")
while True:
    data, addr = s.recvfrom(1024)
    print("Received from %s:%s." % addr)
    s.sendto(("Hello, %s!" % data.decode("utf-8")).encode("utf-8"), addr)

# 服务器绑定UDP端口和TCP端口互不冲突，也就是说，UDP的9999端口与TCP的9999端口可以各自绑定。
