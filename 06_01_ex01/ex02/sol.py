# sol.py
# solving math problems
# 식물생산과학부 2022-14673 강준서


def answer01():
    result = 0.0
    for i in range(1, 31):
        result += 1/i
    return result


def answer02():
    result = 0.0
    for n in range(1, 51):
        for m in range(1, 31):
            result += n/m
    return result


def answer03():
    result = 0.0
    for i in range(100):
        result += (i/100)**2
    result = result * (1/100)
    return result
