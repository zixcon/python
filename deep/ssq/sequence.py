import csv

import matplotlib.pyplot as plt
import pandas as pd

csv_reader = csv.reader(open('ball_items.csv', encoding='utf-8'))

x_data, y_data = [], []
i = 0
for row in csv_reader:
    if i != 0:
        x_data.append(int(row[3]))
        y_data.append(row[0])
    i = i + 1
# X, Y = x_data[1:], y_data[1:]
X, Y = x_data, y_data
print(X)
print(Y)

# plt.plot(y_data, x_data, c='r')
# plt.show()

ts = pd.Series(X, index=Y)
# ts = ts.cumsum()
ts.plot(linewidth=0.05)
plt.show()

df = pd.DataFrame(X, index=Y, columns=list('A'))
# df = df.cumsum()
plt.figure()
df.plot(linewidth=0.05)
plt.show()
