#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hina'

import winsound
from time import *

total = 60 * 10
for i in range(3):
    sleep(1)
    winsound.Beep(1000, 500)
    pass

s = time()
while True:
    e = time()
    #print(e)
    sleep(1)
    d = e - s
    print(int(total - d))
    if d > 60 * 10:
        break

for i in range(10):
    sleep(1)
    winsound.Beep(600, 1000)
    pass
