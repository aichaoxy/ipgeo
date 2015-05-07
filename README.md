ipgeo
===========
[![Build Status](https://travis-ci.org/aichaoguy/ipgeo.svg?branch=master)](https://travis-ci.org/aichaoguy/ipgeo)

Inspired by [huacnlee/ip-location](https://github.com/huacnlee/ip-location).

[PyPi page](https://pypi.python.org/pypi/ipgeo/0.2.2) of ipgeo.

## Goal

Retrieve geo info for ip address via [ip.taobao.com](http://ip.taobao.com) .

## Limit

* The official limit: for every user, qps < 10. [ref](http://ip.taobao.com/restrictions.php)

## Usage

```python
#encoding=utf8
from ipgeo import ipgeo
info = ipgeo.query('182.138.127.93')
print info.country      #中国
print info.region       #四川省
print info.city         #成都市
print info.full_name()  #中国四川省成都市
```
![](https://github.com/aichaoguy/ipgeo/raw/master/ipgeo_test.png)
