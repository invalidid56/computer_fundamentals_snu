# sol.py
# 강준서
# 2022-14673

from reusable import *


def answer_sum1():
    return sum_r(range(1, 101))


def answer_sum2():
    return sum_r(range(11, 1001))


def answer_sum3():
    return sum_r(range(1, 51)) * sum_r(range(51, 101))


def answer_sumlines():
    temp = 0
    with open('pp\sumline.txt', mode='r') as f:
        for line in f.readlines():
            temp += float(line)
    return temp
