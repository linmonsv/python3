#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，
#否则，Python就把这个目录当成普通目录，而不是一个包

"a test module 任何模块代码的第一个字符串都被视为模块的文档注释"

__author__ = "Michael Liao 公开源代码后别人就可以瞻仰"

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print("Hello, world")
    elif len(args) == 2:
        print("Hello, %s!" % args[1])
    else:
        print("Too many arguments!")
        
#如果在其他地方导入该hello模块时，if判断将失败
if __name__ == "__main__":
    test()
#因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，
#最常见的就是运行测试

















