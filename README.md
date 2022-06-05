ipgeo
===========

<font color="red">!!!IMPORTANT: This repo, with the corresponding PyPI lib, is no longer maintained.
`ip.taobao.com` has been shutdown since 2022.3.31 [<sup>1</sup>].</font>

[![PyPI version](https://badge.fury.io/py/ipgeo.svg)](http://badge.fury.io/py/ipgeo)


Geo info retriever for ipv4 address using chinese taobao service.

Python 2.x/3.x Compatible.

Inspired by [huacnlee/ip-location](https://github.com/huacnlee/ip-location).

## Goal

Retrieve geo info for ip address via [ip.taobao.com](http://ip.taobao.com) .

## Limit

* The official limit: for every user, qps < 10. [ref](http://ip.taobao.com/restrictions.php)

## Usage

```python
#encoding=utf8

from ipgeo import ipgeo

info = ipgeo.query('182.138.127.93')
print(info.country)      # 中国
print(info.region)       # 四川省
print(info.city)         # 成都市
print(info.full_name())  # 中国四川省成都市
```

## Refer
- [1] 淘宝IP地址库 https://web.archive.org/web/20220501170356/https://ip.taobao.com/