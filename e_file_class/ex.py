"""
try:

    for i in range(1, 7):

        result = 7 // i

        print(result)

except ZeroDivisionError:

    print("Not divided by 0")

finally:

    print("종료되었습니다.")
"""
"""
sentence = list("Hello Gachon")
while (len(sentence) + 1):
    try:
        print(sentence.pop(0))
    except Exception as e:
        print(e)
        break
"""
"""
for i in range(3):

    try:

        print(i, 3// i)

    except ZeroDivisionError:

        print("Not divided by 0")
"""
"""
alist = ["a", "1", "c"]
blist = ["b", "2", "d"]
for a, b in enumerate(zip(alist, blist)):
    print(b[a])

"""


alist = ["a", "1", "c"]
blist = ["b", "2", "d"]

var = enumerate(zip(alist, blist))
var2 = zip(alist, blist)

print(var2)
for a in var2:
    print(a)

"""
sentence = list("Hello Gachon")
print(sentence)
"""
