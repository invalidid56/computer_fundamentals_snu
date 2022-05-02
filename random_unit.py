import random

people = '''강준서
민지호
김주형
홍다현
김재윤
안승채
박지후
배진우
안승채
민지호
박기연
윤지호
이효선
조희연
김서윤
신진오
변영우
김예원
조수민
유윤상
윤재영
우철승
황리치
최수민
조세훈
이유진
김동욱
김현수
신채우
유승현
박종현
손창인
진수민
정은우
조진모
김종은
김민성
박시현
한도환
황인애
배진우
오승인
천아현
허선정
허선정
권인진
강성준
박지수
성지윤
최연우'''
people = people.split('\n')

units = 7
leaders = ['강준서', '신채우', '변영우', '허선정', '신진오', '김재윤', '윤성빈']
temp = [[] for _ in range(7)]

for person in people:
    if person in leaders:
        continue
    else:
        temp[random.randint(0, 6)].append(person)

print(temp)
