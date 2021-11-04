#1
# zip(alist,blist) = ('A','ㄱ') 이런식으로 묶이게된다
# 여기에서 enumerate을 했을경우 index와 같이 묶이게 된다
"""
0 ('A', 'ㄱ')
1 ('B', 'ㄴ')
2 ('C', 'ㄷ')
"""
# 그래서 for loop에서 a의 값은 index를 가리키고 b의값은 튜플값이 된다.
# for loop 에서 a가 0일떄, b의 값은 : ('A', 'ㄱ') ==>  b[0]는 'A'가 되고 그 값을 result 리스트에 추가
# a가 1일떄, b의 값은 ('B', 'ㄴ') ==> b[1]은 'ㄴ' 가 되고 그 값을 result 리스트에 추가
# a가 2일때, b의 값은 ('C', 'ㄷ') ==> 가되는데 a가 2인데 b의 튜플의 길이는 2 이지만 index는 0,1 밖에 없으므로 Error 입력된다
# 그래서 result 값을 출력했을시 ['A', 'ㄴ', 'Error']가 출력이된다.
# 답은 ['A', 'ㄴ', 'Error']
# ['A', 'ㄴ', 'Error']



#2
#result data_a의 인덱스가 0일떄(값은 1) 모든 j의 요소를 더하는데
#result 값은 계속 data_b의 요소와 1 을 더했을때 값이 갱신이 된다
#안쪽 에 있는 for loop이 끝났을때 result 값은 5이고 그 루프가 끝나자마자
# return이 되므로 값은 5가된다
# 5

#3
class Calculator:
    def __init__(self,list): #생성
        self.list = list

    def sum(self):#Calculator sum 메소드
        return sum(self.list)

    def avg(self): #Calculator avg 메소드
        return sum(self.list)/len(self.list)

cal = Calculator([1,2,3,4,5])
cal.sum()
cal.avg()
#print(cal.sum())
#print(cal.avg())
print("=============================================================")

#4
korean = int(input("국어점수를 입력->"))
english = int(input("영어점수를 입력->"))
math = int(input("수학점수를 입력->"))
print("총점 -> " + str(sum([korean,english,math])))
print("평균 -> " + str(sum([korean,english,math])/3))

print("=============================================================")

#5
result = []
inputStr = input("문자열을 입력 : ")
inputList = inputStr.split()

prohibitionStr = input("금지어를 입력 : ")
prohibitionList = prohibitionStr.split()
found = False
for i in inputList:
    for j in prohibitionList:
        if(i==j):
            found = True #같은문자를 찾았을시 True로 변경
            result.append("*"*len(i))
    if(not found):
        result.append(i) #같은문자를 못찾았을시 문자를 result  리스트에 append
    found = False #found가 True일 경우도 있으니까, 새로운 문자를 위해 False로 변경

#출력
for i in result:
    print(i, end=" ")
print()
print("=============================================================")

#6
avg = 0
try:
    with open('score.txt','r', encoding='utf-8') as f:
        fromscoretxt = f.read() #fromscoretxt 변수에 scoretxt전체를 받은뒤
        lists = fromscoretxt.split("\n") #\n split 해서 기준으로 list형식으로 받는다
        for i in lists:
            avg = avg + float(i) #여기에선 총 합을 구한뒤
        avg = avg / len(lists) #여기에서 평균값을 구한다
except ValueError:
    pass

with open('score.txt','a', encoding='utf-8') as f:
    f.write("\n"+"평균값 : " + str(avg)) #평균값 입력
print("6번답은 파일 확인!")
print("=============================================================")
