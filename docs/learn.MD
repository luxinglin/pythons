1.安装编译器，下周PyCharm专业版本软件，通过Active Code的方式进行破解，破解方法同Intelij Idea类似
2.安装Python开发环境，选用3.7 Windows-64位版本。完成后使用如下命令安装pip和settoools工具。
     python -m pip install -U pip setuptools
3.开发python程序，单文件程序
    例如：使用python操作influxdb数据库，步骤：
    a）安装相关模块，python -m pip install -U influxdb 
    b）编写实际程序，参考如下：
#! /usr/bin/env python
# -*- coding:utf-8 -*-

from influxdb import InfluxDBClient

client = InfluxDBClient("10.200.132.161", 8086, "admin", "admin", "1_79e4ca664aa046638b7480064559a10d") # 初始化

result = client.query("show measurements;") # 显示数据库中的表
print("Result: {0}".format(result))

result = client.query("select * from hourly.cpu_usage_average limit 100;")
print("Result: {0}".format(result))

4.开发Python Web程序，多文件程序


--------------------------------------------------------
一步一步教你搭建IPython notebook

python有多强大就不多说了，自己百度
ipython notebook有多强大也不多说了，自己百度

直接上干货，中间对哪一步用到的东西有疑惑，自己百度

以下为windows平台的流程

首先下载python2.x最新版，2.7.9，因为2.7.9的安装包中集成了pip，如果自己会装pip那2.x哪个版本都行，看个人喜好。
安装过程中，有一步要customize，注意全部选择安装，最后一个是添加到环境变量的（然而可能并没有用），然后一路下一步就好了

安装好来测试一下，打开cmd，

如果提示python不是内部命令blabla，那还要手动添加下环境变量：
计算机右键（或者win+pause break），选择属性-高级系统设置-高级-环境变量-变量Path点编辑-在末尾加入";C:\Python27"，注意最前面有个分号，后面跟安装目录
改好之后，在测试一下，应该就没问题了。

之后安装这个东西，下载地址aka.ms/vcpython27


接下来继续在cmd中操作，正式开始搭建ipython notebook！

在cmd中输入pip install ipython，安装ipython

安装好后，重复同样的操作
pip install pyreadline
pip install pyzmq
pip install tornado
pip install jinja2
pip install jsonschema

如果按照我上面的流程来，一般是不会出错的，如果出现warning error什么的百度一下就好。。。

搞科学计算的话，还可以安装
pip install numpy
pip install matplotlib
这两个文件比较大，安装的要久一点，scipy一般是用不到的，不着急装。

最后可以输入pip freeze看一看一共安装了多少包


一切都ok了！接下来就可以使用ipython了！

新建个文件夹，写个bat文件，里面就写一句话ipython notebook，然后运行！


然后打开浏览器（不要用IE，ie不支持，chrome firefox都可以），输入网址http://localhost:8888，搞定！新建个python文件试试看


按下H可以看快捷键，具体的使用方法自己琢磨吧！


应该就是这些了！