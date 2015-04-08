#encoding=utf8
from ipgeo import ipgeo
info = ipgeo.query('182.138.127.93')
print info.country      #中国
print info.region       #四川省
print info.city         #成都市
print info.full_name()  #中国四川省成都市