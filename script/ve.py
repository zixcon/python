import numpy as np
import csv
import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd

csv_reader = csv.reader(open('ball_items.csv', encoding='utf-8'))

x_data, y_data=[],[]
for row in csv_reader:
    x_data.append(row[3])
    y_data.append(row[6])
x_data, y_data=x_data[1:],y_data[1:]
print(x_data)
print(y_data)  

plt.plot(y_data, x_data, c='r')
plt.show()

df = pd.DataFrame(x_data,index = y_data,columns=list('A'))
df
#

# http://usyiyi.cn/translate/Pandas_0j2/visualization.html
# https://amaozhao.gitbooks.io/pandas-notebook/content/%E6%97%B6%E9%97%B4%E5%BA%8F%E5%88%97%E7%BB%98%E5%9B%BE.html

