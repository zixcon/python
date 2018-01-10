import numpy as np
import csv
import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd

csv_reader = csv.reader(open('ball_items.csv', encoding='utf-8'))

x_data, y_data = [], []
for row in csv_reader:
    x_data.append(row[3])
    y_data.append(row[2])
x_data, y_data = x_data[1:], y_data[1:]
print(x_data)
print(y_data)

# plt.plot(y_data, x_data, c='r')
# plt.show()
#
# ts = pd.Series(x_data, index=y_data)
# ts.plot()
# df = pd.DataFrame(x_data, index=y_data, columns=list('A'))
# plt.figure()
# df.plot()

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()
plt.show()

df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))
df = df.cumsum()
plt.figure()
df.plot()
# 增加后即可展示图片，否则pycharm不展示图片
plt.show()
