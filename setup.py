from distutils.core import setup

setup(
  name = 'ipgeo',
  packages = ['ipgeo'],
  version = '0.1',
  description = 'Geo info retriver for ipv4 address using chinese taobao service',
  author = 'Ai Chao',
  author_email = 'aichaoguy@live.com',
  url = 'https://github.com/aichaoguy/ipgeo',
  download_url = 'https://github.com/aichaoguy/ipgeo/tarball/0.1', # I'll explain this in a second
  keywords = ['ip', 'geo', 'taobao'], # arbitrary keywords
  classifiers = [
      "Programming Language :: Python",
      "Environment :: Other Environment",
      "Operating System :: OS Independent",
      "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)