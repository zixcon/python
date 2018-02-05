from deep.ssq.visual.ssq_data import *
import tensorflow as tf

#  读取数据
data = readData()
title, date, red_ball, blue_ball = getBall(data)

# 走势图
visual(red_ball, date)
visual(blue_ball, date)

# 线性回归


