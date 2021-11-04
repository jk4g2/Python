#1
"""
alist = ["A","B","C"]
blist = ["ㄱ","ㄴ","ㄷ"]
result = []

for a, b in enumerate(zip(alist, blist)):
    try:
        result.append(b[a])
    except IndexError:
        result.append("Error")

print(result)
"""

#2
"""
def sum_data( data_a, data_b ):
    for i in data_a:
        for j in data_b:
            result = i + j
        return result

a=[1,2]
b=[3,4]
print(sum_data(a,b))
"""

#3
class Calculator:
    def Calculator(self,list):

    def sum(self):
