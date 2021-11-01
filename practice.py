#1
"""
pin = '880122-1234567'
birthday = pin.split('-')[0]
gender = pin.split('-')[1]
if(gender[0]=='1'): gender = '남자'
else: gender = '여자'
print( '홍길동님 생년월일 : {} '.format( birthday ) )
print('성별 : {} '.format( gender ) )
"""
#2
"""
a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)
"""

#3
"""
a = ['독도는','대한민국의','아름다운','섬입니다']
result = " ".join(a)
print(result)
"""

#4
"""
a = (1,2,3)
a = a + (4,)
print(a)
"""

#5
"""
a = b = [1,2,3]
a[1] = 4
print(b) #a는 b를 가리키고 있으니까 a를바꾸게되면 b값도 같이 바뀌게된다
"""

#6
"""
target = 0
while True:
    if(target == 6): break;
    print('*' * target)
    target = target + 1
"""

#7
kor_score = [77, 88, 76, 44, 56]
math_score = [96, 99, 100, 55, 66]
eng_score = [50,60,70,80,90]
midterm_score = [kor_score, math_score, eng_score]

"""
for i in range(0,5):
    score = kor_score[i] + math_score[i]+ eng_score[i]
    total_score.append(score)
for i in range(0,5):
    print("총점 :" + str(total_score[i]) + "   "+ "평균: " +str(total_score[i]/3))
"""
print(midterm_score)

life = {'animal':{'cats':('Kim','Lee','Choi'),'octopi':(),'emus':()},
        'plants':{},
        'other':{}}
