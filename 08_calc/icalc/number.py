# number.py
# define methods to translate lang and digits
# 2022-14673 강준서


def speak(n: int):
    digits = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    units = ['', '만', '억', '조', '경', '해']
    units_mini = ['', '십', '백', '천']
    numbers = [int(x) for x in str(n)]
    numbers.reverse()

    result = ''
    for i, number in enumerate(numbers):
        if number == 0:
            continue

        if number == 1 and not i % 4 == 0:
            d = ''
        else:
            d = digits[number]
        temp = ''

        if i % 4 == 0:
            temp = units[int(i/4)]
        result = d+units_mini[i%4]+temp+result
    return result


def listen(n: str):
    digits = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    units = ['_', '만', '억', '조', '경', '해']
    n += '_'

    divided = []
    temp = ''
    prev = ''
    for i, char in enumerate(n):
        if char in units:
            if not divided:
                prev = char
            else:
                gap = abs(units.index(prev)-units.index(char))
                if gap > 1:
                    for _ in range(gap):
                        divided.append('')
                prev = char
            if temp == '' and not char == '_':
                temp = '일'
            divided.append(temp)
            temp = ''
        else:
            temp += char

    def string_to_num(l):
        u = ['십', '백', '천']
        t = 0
        for k, c in enumerate(l):
            if c in u and not k == 0:
                t += digits.index(l[k-1])*10**(u.index(c)+1)
            elif c in u and k == 0:
                t += 10**(u.index(c)+1)
            elif c not in u and k == len(l)-1:
                t += digits.index(c)
        return t

    temp = 0

    divided.reverse()
    for i, div in enumerate(divided):
        temp += string_to_num(div)*10**(3*i)

    return temp




