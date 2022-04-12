# 강준서 식물생산과학부 2022-14673
# tempconv.py: define methods for calculating

def fahr2cels(fahr):    # 화씨-섭씨
    """
    convert Fahrenheit to Celsius
    :param fahr:
    :return:
    """
    return (fahr-32)*(5/9)


def cels2fahr(cels):    # 섭씨-화씨
    """
    convert Celsius to Fahrenheit
    :param cels:
    :return:
    """
    return (cels) * (9/5) + 32
