import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x_data = np.random.randn(1000)
print(x_data)
y_data = pd.date_range('1/1/2000', periods=1000)
print(y_data)

ts = pd.Series(x_data, index=y_data)
ts = ts.cumsum()
ts.plot()
plt.show()

df = pd.DataFrame(np.random.randn(1000, 4), index=y_data, columns=list('ABCD'))
df = df.cumsum()
plt.figure()
df.plot()
# 增加后即可展示图片，否则pycharm不展示图片
plt.show()
