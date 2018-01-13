from deep.ssq.visual.ssq_data import *

data = readData()
title, date, red_ball, blue_ball = getBall(data)
visual(red_ball, date)
visual(blue_ball, date)


