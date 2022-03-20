'''
run.py
print cellcius fahrenheit descrete_temp
'''

import tempconv

temprature = temperatures = [62, 67, 73, 83, 87, 96, 100, 100, 97, 88, 84, 70]


def cool(temp):     # 덥고 추움을 판단하는 함수
    if temp >= 30:
        return 'hot'
    elif 30 > temp >= 20:
        return 'warm'
    elif 20 > temp >= 10:
        return 'mild'
    else:
        return 'cool'


for t in temprature:
    print('{0} {1} {2}'.format(t, tempconv.fahr2cels(t), cool(t)))  # 출력 구문
