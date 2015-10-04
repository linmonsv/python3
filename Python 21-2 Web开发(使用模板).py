#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hina'

# 传说中的MVC：Model-View-Controller，中文名“模型-视图-控制器”

# Flask默认支持的模板是jinja2，所以我们先直接安装jinja2：
# pip install jinja2

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run()
