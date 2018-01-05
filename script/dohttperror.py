import urllib.request
from urllib.error import HTTPError, URLError  # 要调用urllib.error模块

req = urllib.request.Request('http://www.baidusxxxx.com')
try:
    response = urllib.request.urlopen(req)
except HTTPError as e:  # 注意HTTPError别写错了，
    print("http error:", e.reason)
    print("httperror code:", e.code)
except URLError:
    print("url error:", URLError.reason)
else:
    print(response.read().decode('utf-8'))
