# 注意CookieJar()是属于http.cookiejar模块，而不是http.cookies模块，否则会报错： 'module' object has no attribute 'CookieJar'

import urllib.request
import http.cookiejar

# 声明一个CookieJar对象实例来保存cookie
cookie = http.cookiejar.CookieJar()
# 利用urllib.request库的HTTPCookieProcessor对象来创建cookie
handler = urllib.request.HTTPCookieProcessor(cookie)
# 通过handler来构建opener
opener = urllib.request.build_opener(handler)
# 此处的open方法同urllib.request的urlopen方法，也可以传入request
response = opener.open("http://www.jianshu.com/")
for item in cookie:
    print('name=', item.name)
    print('value=', item.value)



