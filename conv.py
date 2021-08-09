import cv2
import numpy as np
import copy
import math

a = [[1, 9, 8, 5, 9, 4], [9, 0, 6, 2, 4, 6], [2, 6, 1, 1, 8, 4], [5, 2, 1, 4, 4, 1], [5, 3, 6, 0, 2, 5], [7, 8, 8, 5, 3, 1]]


hx = [[1,2,1], [0,0,0], [-1,-2,-1]]
hy = [[1,0,-1], [2,0,-2], [1,0,-1]]

pos_mul = [[-1, -1], [-1, 0], [-1, 1], 
        [0, -1], [0, 0], [0, 1],
         [1, -1], [1, 0], [1, 1]]

def add_zero_padding(source):
    c_num = len(source[0])
    # add top padding
    res = [[0] * (len(source[0]) + 2)]
    # body padding
    for row in source:
        new_row = [0] + row + [0]
        res.append(new_row)
    # add foot padding
    res.append([0] * (len(source[0]) + 2))
    return res

padded_a = add_zero_padding(a)

def conv(source, kernel):
    res = copy.deepcopy(source)
    for r_index in range(1, len(source) - 2):
        row = res[r_index]
        for c_index in range(1, len(row) - 2):
            # print("pos: [{}, {}]".format(r_index, c_index))
            new_ele = 0
            for pos in pos_mul:
                # print("r_index: {}".format(r_index + pos[0]))
                # print("c_index: {}".format(c_index + pos[1]))
                val = source[r_index + pos[0]][c_index + pos[1]] * kernel[pos[0] + 1][pos[1] + 1]
                new_ele += val
                # print("val: {}".format(val))
            row[c_index] = new_ele
    return res

Ix = conv(padded_a, hx)
Iy = conv(padded_a, hy)

print("Ix[2][2]: {}".format(Ix[2][2]))
print("Iy[2][2]: {}".format(Iy[2][2]))

can = math.sqrt(12 * 12 + 0 * 0)
atam = math.atan2(Ix[2][2], Iy[2][2])

print(can)
print(atam)