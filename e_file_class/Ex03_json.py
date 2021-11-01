# Ex03_json.py

import json
with open('./data/temp.json','r',encoding='utf-8') as f:
    data = f.read()
    print(data)

print('-'*50)
items = json.loads(data)
print(items)

print(type(data))
print(type(items))

for k,v in items.items():
    print(k, ">>>>>>>>", v)
    print(v['Job'])