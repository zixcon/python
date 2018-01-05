import urllib.request
import http.cookiejar

#### 保存cookie ####
# 设置保存cookie的文件，必须放在同级目录下
filename = ('baidu.cookie')
cookie = http.cookiejar.MozillaCookieJar(filename)

handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open("http://www.baidu.com/")

# 保存cookie到文件
cookie.save(ignore_discard=True, ignore_expires=True)
for item in cookie:
    print('name=', item.name)
    print('value=', item.value)

#### 读取cookie ####
# 创建MozillaCookieJar实例对象
cookie = http.cookiejar.MozillaCookieJar()
# 从文件中读取cookie内容到变量
cookie.load(filename, ignore_discard=True, ignore_expires=True)

handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)

req = urllib.request.Request('http://www.baidu.com')
req = urllib.request.Request('')
response = opener.open(req)

print(response.read())
