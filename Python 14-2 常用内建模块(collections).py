#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hina'

from collections import namedtuple
# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，
# 并可以用属性而不是索引来引用tuple的某个元素。
Point = namedtuple("Point", ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)

from collections import deque
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
q = deque(['a', 'b', 'c'])
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，
# 这样就可以非常高效地往头部添加或删除元素。
q.append('x')
q.appendleft('y')
print(q)

from collections import defaultdict
# 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的
dd = defaultdict(lambda : "N/A")
dd["key1"] = "abc"
print(dd["key1"])
print(dd["key2"])

from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
print(od)
# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key

from collections import Counter
# Counter是一个简单的计数器，例如，统计字符出现的个数：
c = Counter()
for ch in "programming":
    c[ch] = c[ch] + 1
print(c)

