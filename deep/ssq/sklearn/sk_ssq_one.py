import csv
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn import linear_model

#### 准备数据

csv_reader = csv.reader(open('../ball_items.csv', encoding='utf-8'))


def read_arr(arr, i):
    y_data = []
    index = 0
    for row in arr:
        y_data.append(row[i])
        index = index + 1
    return y_data


def read_data():
    x_data, y_data = [], []
    i = 0
    tmp = csv_reader
    for row in tmp:
        if i != 0:
            arr = [row[3], row[1], row[5], row[7], row[8], row[4], row[2]]
            # x_data.append(row[a])
            x_data.append(arr)
            y_data.append(row[6])
            # y_data.append(i)
        i = i + 1
    # X, Y = x_data[1:], y_data[1:]
    X, Y = y_data, x_data
    print(X)
    print(Y)

    X_data = np.array(X).astype(np.int64).reshape(-1, 1)
    Y_data = np.array(Y).astype(np.int64)
    print(X_data)
    print(Y_data)
    return X_data, Y_data


# index = int(i / 3)
# print(index)

# 粗糙划分训练集和测试集数据
# X_test = X_data[0:index].reshape(-1, 1)
# y_test = Y_data[0:index].reshape(-1, 1)
# X_train = X_data[index:].reshape(-1, 1)
# y_train = Y_data[index:].reshape(-1, 1)
# print(X_test)
# print(y_test)
# print(X_train)
# print(y_train)
#
# print(X_train.shape)
# print(y_train.shape)


# 建模
# from sklearn import model_selection
# from tpot import TPOTClassifier, TPOTRegressor
# import numpy as np
# import pandas as pd
#
# X_data, arr = read_data()
# Y_data = read_arr(arr, 3)
# X_trian, X_test, Y_train, Y_test = model_selection.train_test_split(X_data, Y_data, test_size=0.2)
#
# tpot = TPOTRegressor(generations=100, verbosity=2)
# # tpot = TPOTClassifier(generations=6, verbosity=2)
# tpot.fit(X_trian, Y_train)
# tpot.score(X_test, Y_test)
# # 导出
# tpot.export('pipeline.py')

# Warning: xgboost.XGBClassifier is not available and will not be used by TPOT.
# Optimization Progress:  29%|██▊       | 200/700 [11:16<22:13,  2.67s/pipeline]Generation 1 - Current best internal CV score: 0.1952023751448296
# Optimization Progress:  43%|████▎     | 300/700 [17:11<18:47,  2.82s/pipeline]Generation 2 - Current best internal CV score: 0.1952023751448296
# Optimization Progress:  58%|█████▊    | 407/700 [20:22<20:01,  4.10s/pipeline]Generation 3 - Current best internal CV score: 0.1968668769903536
# Optimization Progress:  71%|███████   | 497/700 [23:57<02:20,  1.44pipeline/s]Generation 4 - Current best internal CV score: 0.1968668769903536
# Optimization Progress:  86%|████████▌ | 600/700 [27:33<03:06,  1.86s/pipeline]Generation 5 - Current best internal CV score: 0.1968668769903536
#                                                                               Generation 6 - Current best internal CV score: 0.1968668769903536
#
# Best pipeline: DecisionTreeClassifier(input_matrix, criterion=gini, max_depth=3, min_samples_leaf=12, min_samples_split=5)

# Optimization Progress:  99%|█████████▉| 10023/10100 [2:29:17<01:09,  1.11pipeline/s]Generation 99 - Current best internal CV score: -27.313179287395638
# Optimization Progress: 100%|█████████▉| 10058/10100 [2:29:39<00:25,  1.66pipeline/s]Generation 100 - Current best internal CV score: -27.313179287395638
#
# Best pipeline: LassoLarsCV(SelectPercentile(Normalizer(SelectPercentile(RBFSampler(input_matrix, gamma=0.05), percentile=2), norm=l2), percentile=11), normalize=False)



from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier
X_data, arr = read_data()
for row in range(0, 7):
    Y_data = read_arr(arr, row)
    X_trian, X_test, Y_train, Y_test = model_selection.train_test_split(X_data, Y_data, test_size=0.2)

    clf = DecisionTreeClassifier(criterion='gini', max_depth=3, min_samples_leaf=12, min_samples_split=5)
    clf.fit(X_trian, Y_train)

    accuracy = clf.score(X_test, Y_test)
    print(accuracy)
    result = clf.predict([[2018004]])
    # arr.append(result[0])
    print(result)


# from sklearn import model_selection
# from sklearn.linear_model import LassoLarsCV
# from sklearn.feature_selection import SelectPercentile
# from sklearn.kernel_approximation import RBFSampler
# from sklearn.preprocessing import Normalizer
# 
# X_data, arr = read_data()
# for row in range(0, 7):
#     Y_data = read_arr(arr, row)
#     X_trian, X_test, Y_train, Y_test = model_selection.train_test_split(X_data, Y_data, test_size=0.2)
# 
#     clf = LassoLarsCV(
#         SelectPercentile(Normalizer(SelectPercentile(RBFSampler(gamma=0.05), percentile=2), norm='l2'), percentile=11),
#         normalize=False)
#     clf.fit(X_trian, Y_train)
# 
#     accuracy = clf.score(X_test, Y_test)
#     print(accuracy)
#     result = clf.predict([[2018004]])
#     # arr.append(result[0])
#     print(result)
