
#1
"""
import csv
words = []
try:
    f = open("./file/sample.txt", 'r', encoding="utf-8") #파일 읽기
    contents = f.read()
    words = contents.split()

except FileNotFoundError as e:
    print("파일 찾을때 오류있음")
else:
    f.close()

print(words)

sum = 0
for i in words:
    sum = sum + int(i)
#print(sum)

result = ["sum = " + str(sum), "average = " + str(sum//len(words))] #
with open("./file/result.txt", 'w', encoding="utf-8") as f:
    for i in result:
        f.write(i + "\n")
"""

#2
"""
line = []
with open('./file/dream.txt','r', encoding='utf-8') as f:
    while True:
        idx = 0
        line = f.readlines() #readlines는 모든 줄을 읽어서 각각의 줄을 요소로 같는 리스트로 돌려줌.
        if(not line): break;
        for idx,val in enumerate(line):
            print(str(idx) + "---" + val, end="")
"""

#3
"""
with open("./file/dream.txt", 'r', encoding="utf-8") as f: #파일 읽기
    contents = f.read()
    print("총 글자의 수 : " + str(len(contents)))
    words = contents.split()
    print("총 단어의 수 : " + str(len(words)))
    print("총 줄의 수 " + str(len(contents.split("\n"))))
"""

#4
import os
import random
import datetime
if(not os.path.isdir("./logtemp")): os.mkdir("./logtemp")
if(not os.path.isfile("./logtemp/temp_log.txt")):
    with open("./logtemp/temp_log.txt", 'x', encoding="utf-8") as f:
        pass

with open("./logtemp/temp_log.txt", 'a', encoding="utf-8") as f:
    for i in range(10):
        f.write(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "      " + str(random.randint(0,2^31-1)) + "\n")
    f.write("\n")