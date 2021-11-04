
#1
words = []
try:
    f = open("sample.txt", 'r', encoding="utf-8") #파일 읽기
    contents = f.read()
    words = contents.split()

except FileNotFoundError as e:
    print("파일 찾을때 오류있음")
else:
    f.close()

#불러들인 값들의 sum값 구하기
sum = 0
for i in words:
    sum = sum + int(i) #str값이기에 int값으로 변환
#print(sum)

result = ["sum = " + str(sum), "average = " + str(sum//len(words))] #출력값을 넣어줄 리스트 생성
with open("result.txt", 'w', encoding="utf-8") as f:
    for i in result: #리스트를 읽으면서 파일에 붙이기
        f.write(i + "\n")
print()
print("=============================================================")
print()

#2
line = []
with open('dream.txt','r', encoding='utf-8') as f:
    while True:
        idx = 0
        line = f.readlines() #readlines는 모든 줄을 읽어서 각각의 줄을 요소로 같는 리스트로 돌려줌.
        if(not line): break;
        for idx,val in enumerate(line): #인덱스와 함꼐 출력하기 위해서 enumerate()사용
            print(str(idx) + "---" + val, end="") #line에 보면 str값 마지막에 개행해주는 \n가 있어서 end="" 로 해줌
print()
print()
print("=============================================================")
print()
#3
with open("dream.txt", 'r', encoding="utf-8") as f: #파일 읽기
    contents = f.read()
    print("총 글자의 수 : " + str(len(contents))) #txt파일에 있는 모든 값을 하나의 str으로 불러들여서 그거에대한  길이를 구함
    words = contents.split()
    print("총 단어의 수 : " + str(len(words))) # 스페이스를 기준으로 split을 해서 그 리스트에 대한 길이를 구하면 단어의 수가된다
    print("총 줄의 수 " + str(len(contents.split("\n")))) #개행을 기준으로 split()해서 그 리스트에 대한 길이를 구하면 줄의 수가 된다.
print()
print("=============================================================")

#4
print()
print("4번답은 파일확인 ")
print()
print("=============================================================")
import os
import random
import datetime
if(not os.path.isdir("./logtemp")): os.mkdir("./logtemp") #logtemp디렉토리가 없을시, 디렉토리 생성
if(not os.path.isfile("./logtemp/temp_log.txt")): # ./logtemp 디렉토리안에 temp_log.txt가 없을시 생성
    with open("./logtemp/temp_log.txt", 'x', encoding="utf-8") as f:
        pass

with open("./logtemp/temp_log.txt", 'a', encoding="utf-8") as f: #temp_log에 뒤에 값을 붙여야하기때문에 with open()으로 옵션을 a로 해준뒤
    for i in range(10): #for loop을 이용해서 10번동안 시간과, int값을 넣어준다
        f.write(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "      " + str(random.randint(0,2^31-1)) + "\n")
    f.write("\n") #10개가 다 넣어지면 한줄 개행
