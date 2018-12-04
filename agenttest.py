import requests
import urllib
url = 'http://www.baidu.com'
proxies = {
    'http': '175.155.24.39:808',
    'https': '175.155.24.39:808'
           }
try:
    prixyh =  urllib.request.ProxyHandler(proxies)
    openr = urllib.request.build_opener(prixyh)
    resp = openr.open(url, timeout=2)
    # resp = requests.get(url, proxies=proxies, timeout=3)
    print(resp.read() .decode ('utf-8'))
except Exception as e:
    print(e)
