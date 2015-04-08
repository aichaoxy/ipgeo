import urllib2
import json
class GeoInfo:
    def __init__(self):
        pass

    @property
    def country(self):
        return self._country
    @country.setter
    def country(self, c):
        self._country = c

    @property
    def region(self):
        return self._region
    @region.setter
    def region(self, r):
        self._region = r

    @property
    def city(self):
        return self._city
    @city.setter
    def city(self, c):
        self._city = c

    @property
    def isp(self):
        return self._isp
    @isp.setter
    def isp(self, i):
        self._isp = i

    def full_name(self):
        return "".join([self.country, self.region, self.city])

def query(ip):
    response = urllib2.urlopen('http://ip.taobao.com/service/getIpInfo.php?ip='+ip)
    data = json.load(response)
    if data['code'] == 0:
        info = GeoInfo()
        info.country = data['data']['country']
        info.region  = data['data']['region']
        info.city    = data['data']['city']
        info.isp     = data['data']['isp']
        return info
    else:
        return None

