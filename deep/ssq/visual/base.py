import numpy as np


def flatten(input_list):
    output_list = []
    while True:
        if input_list == []:
            break
        for index, i in enumerate(input_list):

            if type(i) == list:
                input_list = i + input_list[index + 1:]
                break
            else:
                output_list.append(i)
                # input_list.pop(index)
                break
    return output_list


def flat(arr):
    output_list = []
    for x in arr:
        for y in x:
            output_list.append(y)
    return output_list


a = np.random.rand(2, 2)
print(a)
print(a.shape)
print(a.reshape(1, 4)[0])
print(flat(a))
