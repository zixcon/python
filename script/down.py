import urllib.request

url = 'http://www.cbrc.gov.cn/chinese/files/2017/BF2D2E4669B1458CB1655D0762AD0F60.pdf'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req = urllib.request.Request(url=url, headers=headers)
data = urllib.request.urlopen(req)
with open("去库存-urllib.pdf", "wb") as code:
    code.write(data.read())
