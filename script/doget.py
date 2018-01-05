# http get 请求

import urllib.request
import urllib.parse

values = {
    'act': 'login',
    'login[email]': "admin@qq.com",
    "login[password]": "xxxx"}
# 编码工作
url = "http://www.jianshu.com/sign_in"
data = urllib.parse.urlencode(values)
req = url + "?" + data
# 发送请求、接受反馈信息、读取反馈的信息。这是由直接抓取网页法实现抓取网页
response = urllib.request.urlopen(req).read()
# 解码
data = response.decode('UTF-8')
print(data.encode('gb18030'))
print(urllib.request.urlopen(req).geturl())  # 返回获取的真实的URL
