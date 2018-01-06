import urllib.request
import urllib.parse

values = {'user_name': 'xx@qq.com', 'pass_word': 'xx'}
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.89 Safari/537.36'
headers = {"User-agent": user_agent, 'referer': "https://passport.csdn.net/account/login?ref=toolbar"}
url = "https://passport.csdn.net/account/login?ref=toolbar"
data = urllib.parse.urlencode(values)
# 注意只是针对values进行了解码，而headers没有。
bianary_data = data.encode('utf-8')
req = urllib.request.Request(url, bianary_data, headers)
response = urllib.request.urlopen(req, timeout=10)
print(response.read().decode("utf-8"))
print(response.geturl())
