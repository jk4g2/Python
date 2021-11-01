# Ex03_json_exam.py

'''
    sample.json 파일을 읽어서 총 과일의 금액을 출력하기
'''
import json
with open('./data/sample.json','r',encoding='utf-8') as f: #sample.json 파일을 읽기만 할거야
    data = f.read() #데이터들을 읽어서 data변수에 넣어줘
    #print(data)

items_from_sample = json.loads(data)
#데이터변수를 json파일 형식으로 돌려서 items_from_sample이라는 변수에 넣어줘

sum = 0
for k,v in items_from_sample.items():
    print((int(v["price"]) * int(v["count"])))
    sum = sum + (int(v["price"]) * int(v["count"]))

print(sum)