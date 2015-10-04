import hello

hello.test()

#类似__xxx__这样的变量是特殊变量，可以被直接引用，
#但是有特殊用途，比如上面的__author__，__name__就是特殊变量，
#hello模块定义的文档注释也可以用特殊变量__doc__访问，
#我们自己的变量一般不要用这种变量名

#_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用

def _private_1(name):
    return "Hello, %s" % name
def _private_2(name):
    return "Hi, %s" % name
def  greeting(name):
    if len(name) > 2:
        return _private_1(name)
    else:
        return _private_2(name)
print(greeting("Quu"))
print(greeting("UU"))

#在Python中，安装第三方模块，是通过包管理工具pip完成的

#如果你正在使用Windows，请参考安装Python一节的内容，
#确保安装时勾选了pip和Add python.exe to Path。

#第三方库都会在Python官方的pypi.python.org网站注册

#pip install Pillow

#默认情况下，Python解释器会搜索当前目录、
#所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量

import sys
print(sys.path)

#如果我们要添加自己的搜索目录，有两种方法
#sys.path.append('/Users/michael/my_py_scripts')

#第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中




