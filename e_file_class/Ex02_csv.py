# Ex02_csv.py
# CSV : Common String Value

import csv
"""
#1. 리스트의 데이터를 csv로 저장하기
data = [[1,'김','책임'],[2,'박','선임'],[3,'맹','연구원']]
with open('./data/imsi.csv','wt',encoding='utf-8') as f: #t는 default값
    cout = csv.writer(f)
    cout.writerows(data)
"""

#2. csv로 저장된 파일을 읽어서 리스트 저장하기
result = []
with open('./data/imsi.csv','rt',encoding="utf-8") as f:
    cin = csv.reader(f)
    result = [row for row in cin if row] # cin애라는에에서 row로 뽑아올건데.. row가 있으면 row로 뽑아오고 아니면 무시

print(result)
"""
with open("./i_have_a_dream.txt","r") as f:
    contents = f.read()
    print(contents);
"""
