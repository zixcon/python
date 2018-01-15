from deep.ssq.visual.ssq_data import *

data = readData()
title, date, red_ball, blue_ball = getBall(data)
visual(red_ball, date)
visual(blue_ball, date)

# 参照：
https://machinelearningmastery.com/regression-tutorial-keras-deep-learning-library-python/
http://blog.csdn.net/qq_36511757/article/details/77895316
