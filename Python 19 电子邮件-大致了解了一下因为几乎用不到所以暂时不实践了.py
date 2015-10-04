#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hina'

# 假设我们自己的电子邮件地址是me@163.com，对方的电子邮件地址是friend@sina.com（注意地址都是虚构的哈），
# 现在我们用Outlook或者Foxmail之类的软件写好邮件，
# 填上对方的Email地址，点“发送”，电子邮件就发出去了。
# 这些电子邮件软件被称为MUA：Mail User Agent——邮件用户代理。

# Email从MUA发出去，不是直接到达对方电脑，
# 而是发到MTA：Mail Transfer Agent——邮件传输代理，
# 就是那些Email服务提供商，比如网易、新浪等等

# 由于我们自己的电子邮件是163.com，所以，Email首先被投递到网易提供的MTA，
# 再由网易的MTA发到对方服务商，也就是新浪的MTA。
# 这个过程中间可能还会经过别的MTA，但是我们不关心具体路线，我们只关心速度。

# Email到达新浪的MTA后，
# 由于对方使用的是@sina.com的邮箱，
# 因此，新浪的MTA会把Email投递到邮件的最终目的地MDA：Mail Delivery Agent——邮件投递代理。
# Email到达MDA后，就静静地躺在新浪的某个服务器上，存放在某个文件或特殊的数据库里，
# 我们将这个长期保存邮件的地方称之为电子邮箱。

# 发件人 -> MUA -> MTA -> MTA -> 若干个MTA -> MDA <- MUA <- 收件人

# 要编写程序来发送和接收邮件，本质上就是：
# 编写MUA把邮件发到MTA；
# 发邮件时，MUA和MTA使用的协议就是SMTP：Simple Mail Transfer Protocol，后面的MTA到另一个MTA也是用SMTP协议
# 编写MUA从MDA上收邮件。
# 收邮件时，MUA和MDA使用的协议有两种：
# POP：Post Office Protocol，目前版本是3，俗称POP3；
# IMAP：Internet Message Access Protocol，目前版本是4，优点是不但能取邮件，还可以直接操作MDA上存储的邮件，

# Python对SMTP支持有smtplib和email两个模块，
# email负责构造邮件，
# smtplib负责发送邮件。

# Python内置一个poplib模块，实现了POP3协议，可以直接用来收邮件
# 收取邮件分两步：
# 第一步：用poplib把邮件的原始文本下载到本地；
# 第二部：用email解析原始文本，还原为邮件对象

