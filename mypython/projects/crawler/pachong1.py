import urllib.request
from urllib import request
from bs4 import BeautifulSoup

url = 'https://www.buxiuse.com/'

req = request.Request(url)
req.add_header('user-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36')
response = urllib.request.urlopen(req, timeout=20)
print(response.code)
contents = response.read()
print(contents)






