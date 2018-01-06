# http post 请求

import urllib.request
import urllib.parse

values = {'username': "xx@qq.com", 'password': 'xxxx'}
data = urllib.parse.urlencode(values)
binary_data = data.encode('utf-8')
# 发送请求，传送表单数据，这是用构造Request法来抓取网页的
req = urllib.request.Request("http://www.jianshu.com/sign_in", binary_data)
print(req.get_method())
print(req.get_full_url())
# 接受反馈的信息
response = urllib.request.urlopen(req)
# 读取反馈信息
data = response.read()
data = data.decode('UTF-8')
print(data.encode('gb18030'))
# 返回获取的真实的URL
print(response.geturl())
