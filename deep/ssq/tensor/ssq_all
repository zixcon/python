import csv
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

#### 准备数据

csv_reader = csv.reader(open('ball_items.csv', encoding='utf-8'))

x_data, y_data = [], []
i = 0
for row in csv_reader:
    if i != 0:
        arr = [row[3], row[1], row[5], row[7], row[8], row[4], row[2]]
        x_data.append(arr)
        y_data.append(row[6])
        # y_data.append(i)
    i = i + 1
# X, Y = x_data[1:], y_data[1:]
X, Y = y_data, x_data
# print(X)
# print(Y)

# X_data = np.array(X).astype(np.float32)
# Y_data = np.array(Y).astype(np.float32)

X_data = np.array(X).astype(np.int64)
Y_data = np.array(Y).astype(np.int64)
print(X_data)
print(Y_data)

index = int(i/3)
print(index)

# 转为n*7
ones = np.ones([1,7])
print(ones)
data = X_data.reshape(-1, 1)
X_data_re = np.dot(data,ones)

# 粗糙划分训练集和测试集数据
X_test = X_data_re[0:index].reshape(-1, 7)
y_test = Y_data[0:index].reshape(-1, 7)
X_train = X_data_re[index:].reshape(-1, 7)
y_train = Y_data[index:].reshape(-1, 7)
print(X_test)
print(y_test)
print(X_train)
print(y_train)

print(X_train.shape)
print(y_train.shape)
# X_train = X_train.T
# y_train = y_train.T



#ones = np.ones([1,7])
#print(ones)
#data = X_data.reshape(-1, 1)
#res = np.dot(data,ones)
#print(res)




#### 建模

# 设置自变量x的占位符,梯度下降时真实数据输入到模型的入口点
x = tf.placeholder(tf.float32, [None, 7])
# 设置斜率(权重值)W变量
W = tf.Variable(tf.zeros([7, 1]))
# 设置截距(偏置量)b变量
b = tf.Variable(tf.zeros([7]))

# 设置线性模型y=Wx+b
y = tf.matmul(x, W) + b

# 设置占位符用于输入实际的y值
y_ = tf.placeholder(tf.float32, [None, 7])

# 设置成本函数(最小方差)
cost = tf.reduce_sum(tf.pow((y_ - y), 2))
# 使用梯度下降，以0.000001的学习速率最小化成本函数cost，以获得W和b的值
learning_rate = 0.0000000000000000001
# 1
train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

# 2
# optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate)
# gvs = optimizer.compute_gradients(cost)
# capped_gvs = [(tf.clip_by_value(grad, 1, 32), var) for grad, var in gvs]
# train_step = optimizer.apply_gradients(capped_gvs)

# 3
# learning_rate = 0.0000001
# optimizer = tf.train.AdamOptimizer(learning_rate)
# gradients, variables = zip(*optimizer.compute_gradients(cost))
# train_step = optimizer.apply_gradients(list(zip(gradients, variables)))


# 开始训练前对变量进行初始化
init = tf.global_variables_initializer()
# 创建一个会话(Sess)
sess = tf.Session()
# 在Sess中启用模型并初始化变量
sess.run(init)

# 创建一个空list用于存放成本函数的变化
cost_history = []

# 循环训练模型100次
for i in range(100):
    feed = {x: X_train, y_: y_train}
    sess.run(train_step, feed_dict=feed)
    # 存储每次训练的cost值
    cost_history.append(sess.run(cost, feed_dict=feed))
    # 输出每次训练后的W,b和cost值
    print("After %d iteration:" % i)
    print("W: " , sess.run(W))
    print("b: " , sess.run(b))
    print("cost: %f" % sess.run(cost, feed_dict=feed))
# 输出最终的W,b和cost值
# print("W_Value: %f" % sess.run(W), "b_Value: %f" % sess.run(b), "cost_Value: %f" % sess.run(cost, feed_dict=feed))

# 绘制成本函数cost在100次训练中的变化情况
plt.plot(range(len(cost_history)), cost_history)
plt.axis([0, 100, 0, np.max(cost_history)])
plt.xlabel('training epochs')
plt.ylabel('cost')
plt.title('cost history')
plt.show()


# sess.run(y, feed_dict={x: [[2018004,2018004,2018004,2018004,2018004,2018004,2018004]]})
sess.run(y, feed_dict={x: [[1474,1474,1474,1474,1474,1474,1474]]})



