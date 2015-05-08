try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

import codecs
import json

reader = codecs.getreader("utf-8")


class GeoInfo:
    def __init__(self, _country, _region, _city, _isp):
        self.country = _country
        self.region = _region
        self.city = _city
        self.isp = _isp

    def full_name(self):
        return "".join([self.country, self.region, self.city])


def query(ip):
    response = urlopen('http://ip.taobao.com/service/getIpInfo.php?ip='+ip)
    data = json.load(reader(response))
    if data['code'] == 0:
        country = data['data']['country']
        region = data['data']['region']
        city = data['data']['city']
        isp = data['data']['isp']
        info = GeoInfo(country, region, city, isp)
        return info
    else:
        return None
