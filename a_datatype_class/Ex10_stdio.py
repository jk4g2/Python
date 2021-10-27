"""
    [ 콘솔 입력 처리 함수 ]
    - input() : 기본적으로 문자열로 입력받음
    - eval() : 함수로 감싸면 숫자 처리됨
    - int() / float() / str() 자료형변환  ( eval() 사용보다는 형변환을 권장 )
"""

"""
name = input('이름을 입력해주세요\n')
#print("당신은 ", name, '입니다')

# %를 활용해서 출력
msg = "당신은 {} 입니다\n"
print(msg.format(name))


#-------------------------------------------
# 나이를 입력받아 +1을 하여 출력하고 키를 실수형으로 입력받아 출력

age = int(input("나이를 입력해주세요\n"))
print(str(age+1) + "살")
print()
height = float(input("키를 입력해주세요\n"))
print("키는 " + str(height) +" 입니다")
print("키는 %.1fcm 입니다" %(height))
print()
print('%s님은 %d세이고, 신장은 %.1f cm 입니다' %(name,age,height))
"""


"""
print('1+2')
print(eval('1+2'))
"""

#----------------------------------
# 단을 입력받아 구구단을 구하기
"""
dan = int(input("단을 입력해주세요\n"))
for i in range(1,10,1):
    print(str(dan) + "x" + str(i) + "=" + str(dan * i))
"""
#-----------------------------------------
# print() 함수
"""
print("안녕" + '친구')
print("안녕", '친구')
print("안녕" '친구')

for i in range(10):
    print(i, end=',')
print()
for i in range(1,10):
    print(i, end=',')
print()
for i in range(1,10,3):
    print(i, end=',')
print()

for i in range(1,10,3):
    print(i, end=',' if i<5 else "")
147,

"""


#1
"""
list1 = []
for i in range(0,5):
    c = int(input("정수를 입력하세요: "))
    list1.append(c)
sum = 0
for i in list1:
    sum += i
print(float(sum//5))
"""
#2
"""
input = input("문자열 입력: ")
print(input[::-1])
"""

"""
list1 = list(map(int,input("정수리스트입력: ").split()))

sum = 0
for i in list1:
    sum += i
print(sum/5)

import numpy
print(numpy.std(list1))
print()
"""


input_str = input("문자열을 입력하시오: ")
count = 0
num = 2

#Dictionary 세팅
dictionary = {}
for i in range(65,91): # 아스키코드 65..91 은 (A..Z+1)
    if(count==3): #규칙이
        num = num + 1
        count = 0;
    if(i == 90): #9번 키패드가 4개이므로.
        dictionary[chr(int(i))] = num-1
    elif(i == 83): #7번키패드 4개
        dictionary[chr(int(i))] = num-1
        count = 0;
    else:
        dictionary[chr(int(i))] = num
        count = count + 1

answer = "" #answer 값 출
for i in input_str:
    answer += str(dictionary[str(i)])

print(answer)


# -------------------------------------------------------
# 명령행 매개변수 받기 - java의 main() 함수의 인자
# [ 콘솔에서 실행 ] python Ex10_stdio.py ourserver scott tiger
#                                   0      1      2      3
