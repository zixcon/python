import urllib.request

enable_proxy = True
proxy_handler = urllib.request.ProxyHandler({"http": "1.9.110.1:8080"})
# 代理处理程序，代理对象，注意函数调用对象的大小写
null_proxy_handler = urllib.request.ProxyHandler({})
if enable_proxy:
    opener = urllib.request.build_opener(proxy_handler)
else:  # 构建代理
    opener = urllib.request.build_opener(null_proxy_handler)
urllib.request.install_opener(opener)  # 运行代理
