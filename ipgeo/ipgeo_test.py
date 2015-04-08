#encoding=utf8
import ipgeo
info = ipgeo.query('182.138.127.93')
print info.country
print info.region
print info.city
print info.full_name()