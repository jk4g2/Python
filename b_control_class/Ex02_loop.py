
# ------------------------------------------------------
"""
   (2) for문
        for <타켓변수> in 집합객체 :
            문장들
        else:
            문장들

        ` 반복문 뒤에 else는 반복하는 조건에 만족하지않으면 실행

   (3) while 문
        while 조건문 :
            문장들
        else :
            문장들

"""
a = 112                  # 숫자형
b = ['1','2','3']       # 리스트
c = '987'                # 문자열
d = tuple(b)             # 튜플
e = dict(k=5, j=6)       # 딕셔너리

for entry in e: # a는 반복이 안되지만 b부터 e까지는 반복된다.
    print(entry)
    print(e[entry])

for k,v in e.items():
    print(k, '-', v)

#-------------------------------------------------------
'''
    for(int i =0;i<10;i++){
    }
'''
#for i in range(10):

#1~10
for i in range(1,11):
    print(i, end=" ")
print()

"""
sum = 0;
for i in range(1,11):
    if(i%2 == 1):
        sum+=i
print('홀수의 합은',sum)
"""
"""
sum = 0;
for i in range(1,11,2):
    sum+=i
print('홀수의 합은',sum)
"""
"""
[과제] 2단부터 9단까지 이중 반복문으로 출력
"""
for i in range(2,10):
    print(i,"단")
    for j in range(1,10):
        print(i, "*", j, "=", i*j)
    else:
        print()
