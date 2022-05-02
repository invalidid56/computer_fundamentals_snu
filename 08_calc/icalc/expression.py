# expression.py
# define methods to express formula
# 2022-14673 강준서


import number


def translate(formula: str):
    words = formula.split()
    calc = words[1]

    op1 = ['더하기', '빼기', '곱하기', '나누기']
    op2 = ['+', '-', '*', '/']

    calc = op2[op1.index(calc)]

    nums = [str(number.listen(words[0])), str(number.listen(words[2]))]

    return ' '.join([nums[0], calc, nums[1]])

