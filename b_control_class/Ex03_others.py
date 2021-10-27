msg = '행복해'            # 문자열
li = ['a','b','c']       # 리스트
tpl = ('ㄱ','ㄴ','ㄷ')    # 튜플
di = {'k': 5, 'j': 6, 'l':7 }    # 딕셔너리

# (1) unpacking : 각 요소를 분해(풀기)
"""
a, b, c = msg
print(a)
print(b)
print(c)

a, b, c = li
print(a)
print(b)
print(c)

a, b, c = tpl
print(a)
print(b)
print(c)

a, b, c = di
print(a)
print(b)
print(c)
"""

# (2) enumerate() 함수 : 각 요소와 인덱스를 같이 추출
user_list = ['개발자','코더', '전문가', '분석가']
for value in user_list:
    print(value, end=" ")

print()

for idx,value in enumerate(user_list): # index를 뽑고싶을때 사용하면됨!********************************
    print(idx, ':', value)

# (3) zip()
days = ['월','화','수']
doit = ['잠자기','공부','놀기','밥먹기']

print(list(zip(days,doit))) # *************************************** 각각의 요소별로 묶어준다. (튜플로 묶음)
print(dict(zip(days,doit))) # *************************************** 각각의 요소별로 묶어준다. (딕셔너리로 묶음)
