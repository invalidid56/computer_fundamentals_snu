# 강준서 식물생산과학부 2022-14673
# filter.py - read file, calculate and write result

import sys
from weather.tempconv import *


def main(min, max, file):
    for temp in file:
        t = float(temp)
        if min < fahr2cels(t) < max:
            print(str(t)+' '+str(fahr2cels(t)), file=sys.stdout)  # Python의 print() 함수는 기본적으로 stdout으로 출력합니다
            # sys.stdout.write(str(t)+' '+str(fahr2cels(t)), file=sys.stdout)


if __name__ == '__main__':
    main(float(sys.argv[1]), float(sys.argv[2]), sys.stdin)
