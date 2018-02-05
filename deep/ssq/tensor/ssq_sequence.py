from deep.ssq.visual.ssq_data import *
import tensorflow as tf

#  读取数据
data = readData()
title, date, red_ball, blue_ball = getBall(data)

# 走势图
visual(red_ball, date)
visual(blue_ball, date)

# 线性回归


# 参照：
# https://machinelearningmastery.com/regression-tutorial-keras-deep-learning-library-python/
# http://blog.csdn.net/qq_36511757/article/details/77895316
