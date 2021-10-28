"""
    [ 함수 ]

     - 반복적인 구문을 만들어 함수로 선언하여 간단하게 호출만 하고자 한다
     - 역할별 구문을 작성한다

     def 함수명(매개변수):
        수행할 문장들

"""
# (0) 인자도 없고 리턴값도 없는 함수
"""
def func():
    print('inside function')

func()
result = func()
print(result)
"""

# (1) 리턴값이 여러개인 함수 => 튜플 하나로 리턴됨
"""
def func(args):
    return args+1, args-1

result = func(10)
print(result)

first, second = func(10)
print(first, ":", second)
print(first + second)
"""


# (2) 위치인자 (positional argument)
"""
def func(greeting,name):
    print(greeting, '!!!!!!', name, '님')

func("하이",'백길동')
func("김길동",'안녕')
"""


# (3) 키워드 인자 (keyword argument)
"""func(name='김길동2',greeting='안녕2')"""

# (4) 매개변수의 기본값
#func("올라","세뇨라","바이")
"""
def func(greeting,name="아무개"):
    print(greeting, '!!!!!!', name, '님')


func('올라')
func('올라','김길동')

def method(a,b,c=100):
    return a+b+c
print(method(1,2,3))
print(method(c=1,b=2,a=30))
print(method(10,20))
"""


#----------------------------------------------------------------
# (5) 위치 인자 모으기 (*)

'''
첫번째와 두번째는 인자가 반드시 들어가고 세번째는 인자가 들어갈 수도 있고 없으면 0으로 초기화한다
그러나 네번째 인자부터는 정확히 모른다면?

print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))       # args에 7,8,9가 튜플로 들어간다

def func(a,b,c=0, *args): #추가로 매개변수가 더 있을경우 *args가 tuple로 가져옴, *args 변수명은 국룰
    sum = a + b + c
    for i in args:
        sum += i
    return sum

print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))
'''

#----------------------------------------------------------------
# (6) 키워드 인자 모으기 (**)
def func(a,b,c=0, **kwargs): """#키워드가 존재하지않을 경우,""" # **kwarg는 dictionary형태로 지정되지 않은 애들의 값을 받아준다
    sum = a + b
    for k in kwargs:
        sum += kwargs[k]
    return sum

print()
print(func(1, 2, 3, kor=100, math=50))
print(func(1, 2, kor=50, math=60, eng=40))
print(func(1, 2, kor=50, java=40))
