"""
    [ dictionary 형 ]

    1- 키와 값으로 구성 ( 자바의 map 와 유사 )
    2- 저장된 자료의 순서는 의미 없음
    3- 중괄호 {} 사용
    4- 변경가능

    ` 사전.keys() : key만 추출 (임의의 순서)
    ` 사전.values() : value만 추출 (임의의 순서)
    ` 사전.items() : key와 value를 튜플로 추출 (임의의 순서)
"""

print('--------- 1. 딕셔너리 요소 --------------- ')
dt = {1:'one', 2:'two', '3':'three',1:'first',3:"third"} #같은 키 값이면 덮어쓰게됨
print(dt)
print(dt[1])
print(dt[2])
print(dt['3'])
print(dt[3])


d2 = {1: 'one', 2:'two', (3,4):'threefour'}
print(d2[(3,4)])


# 키는 숫자와 문자 그리고 튜플이여야 한다. 즉 리스트는 안된다.
# 리스트의  값이 변경 가능하다. 그러나 키값을 변경하면 안되므로 리스트는 안된다
dt2 = {1:'one', 2:'two', (3,4):'turple'}


print('--------- 2. 딕셔너리 추가 및 수정  --------------- ')
# 딕셔너리에 값 추가 및 수정
d2['korea'] = 'seoul'
print(d2)
d2['korea'] = '대한민국'
print(d2)

"""
    존재하는 키값에 값을 설정해주게되면 mapping이 되버리고
    존재하지 않는 키값에 값을 설정해주게 되면 값이 생성이되버림.
"""
# 여러개 추가할 때
print('--------- 3. Key로 Value값 찾기  --------------- ')
""" .update({}) 로 여러개를 추가할 수 있다. """
d2.update({5:'five',6:'six'})
print(d2[5])
print(d2.get(5))

# Key와 Value만 따로 검색
print(d2.keys())
print(d2.values())
print(d2.items())

print()
print()
print()
for item in d2.items():
    print(item) #튜플로 나옴

for k, v in d2.items():
    print(k, '=', v) #튜플로 나옴
print('-'*100)
