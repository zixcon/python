import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from deep.ssq.visual import base

# filename可以直接从盘符开始，标明每一级的文件夹直到csv文件，header=None表示头部为空，sep=' '表示数据间使用空格作为分隔符，如果分隔符是逗号，只需换成 ‘，’即可。
data = pd.read_csv('../ball_items.csv', header=None, sep=',')

rows = data.shape[0]
colums = data.shape[1]
print("rows", rows, "colums", colums)

origin = np.matrix(data)
print(origin)
print(origin.shape)
print("origin.dtype: ", origin.dtype)

title = origin[0:1, 0:colums]
ball_data = origin[1:rows, 0:colums]

date = ball_data[:, 0:1]
red_ball = ball_data[:, 2:8]
# 数据类型转换 astype
red_ball = red_ball.astype(int)
print("red_ball.dtype: ", red_ball.dtype)
blue_ball = ball_data[:, 8:9]
blue_ball = blue_ball.astype(int)
print(title)
# print(ball_data)
print(date)
print(red_ball)
print(blue_ball)

show_title = title[:, 2:8]
print(base.flat(show_title))
# df = pd.DataFrame(red_ball, index=date, columns=(x for x in show_title))
df = pd.DataFrame(red_ball, index=date, columns=list('123456'))
plt.figure()
df.plot(linewidth=0.05)
plt.show()
