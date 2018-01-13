import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def readData():
    data = pd.read_csv('../ball_items.csv', header=None, sep=',')
    return data


def getBall(data):
    origin = np.matrix(data)

    title = origin[0:1, 0:colums]
    ball_data = origin[1:rows, 0:colums]

    date = ball_data[:, 0:1]
    red_ball = ball_data[:, 2:8]
    red_ball = red_ball.astype(int)
    blue_ball = ball_data[:, 8:9]
    blue_ball = blue_ball.astype(int)
    return title, date, red_ball, blue_ball


def visual(data, index, linewidth):
    df = pd.DataFrame(data, index=index)
    plt.figure()
    if linewidth is None:
        linewidth = 0.1
    df.plot(linewidth=linewidth)
    plt.show()
