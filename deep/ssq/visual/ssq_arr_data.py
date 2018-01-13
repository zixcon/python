# 普通方法

import pandas as pd

# filename可以直接从盘符开始，标明每一级的文件夹直到csv文件，header=None表示头部为空，sep=' '表示数据间使用空格作为分隔符，如果分隔符是逗号，只需换成 ‘，’即可。
data = pd.read_csv('../ball_items.csv', header=None, sep=',')

# print(data)
rows = data.shape[0]
colums = data.shape[1]

date = data.values[0:rows, 0:1]
red_ball = data.values[0:rows, 2:8]
blue_ball = data.values[0:rows, 8:9]

date = date[1:]
red_ball = red_ball[1:]
blue_ball = blue_ball[1:]
print(date)
print(red_ball)
print(blue_ball)
