# 강준서 식물생산과학부 2022-14673
# solve.py
# answer*(): return answers to each problem

import finance
import physics


def answer01():
    return physics.force(7.3*10**22, 5.97*10**24, 3.84*10**8)   # 문제 1번, 지구와 달 사이의 인력


def answer02():
    return physics.force(5.97*10**24, 0.24, 6400)   # 문제 2번, 지구와 사과 사이의 인력


def answer03():
    return finance.fv(2.5*10**(-2), 5, 1000) - finance.fv((2.5*10**(-2))/12, 5*12, 1000)    # 문제 1번, 월복리와 연복리의 차이


