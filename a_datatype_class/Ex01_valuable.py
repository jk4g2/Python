"""
    파이션  - 무료이지만 강력하다
        ` 만들고자 하는 대부분의 프로그램 가능
        ` 물론, 하드웨어 제어같은 복잡하고 반복 연산이 많은 프로그램은 부적절
        ` 그러나, 다른언어 프로그램을 파이썬에 포함 가능 
        
    [주의] 줄을 맞추지 않으면 실행 안됨

    [실행] Run 메뉴를 클릭하거나 단축키로 shift + ctrl + F10

    [도움말] ctrl + q

@파이선 자료형
1. 기본자료형
    ' 숫자형 ( 정수형 int / 실수형 float )
            숫자형 종류
                  -정수형
                  -실수형
                  -복소수형
                  -8진수 : 0o25
                  -16진수: 0x25
    ' 문자형
    ' 논리형
    ' 날짜형

      1. 기초연산자
            +,-,*,/(나누기 실수값 결과),//(나누기 정수값 결과),%(나머지), **(n제곱)
            [참고]
                  자바: 3/2 => 1
                  파이썬: 3/2 => 1.5
      2. 관계연산자
            <, >, <= ,>= ,== ,!=
      3. 논리 연산자
            not or and
      4. 이진(비트) 연산자
            ~ : 이진 not
            | : 이진 or
            & : 이진 and
            ^
      5. 대입연산자
            =. +=, -=, *=, /=, //= %=

      6. 기타연산자


2. 집합자료형
    - list
    - tuple(*) : list와 유사하지만, 값 변경이 안됨
    - set
    - dictionary

    [ 참고 ] 자바의 Collection
        - List
        - Set
        - Map

"""

""" 여러
줄 주석 """




# 한줄 주석

# 문자열표시
print("헬로우")
print('hel'
      ''
      'lo')

print('''올라''')
print("""안


녕""")
# 실행 : shift + ctrl + F10

'''
변수란
    파이션의 모든 자료형은 객체로 취급한다
    a = 7
            7 객체을 가리키는 변수 a이다. ( 저장한다는 표현 안함 )
            변수 a는 7이라는 정수형 객체를 가리키는 레퍼런스이다.
            여기서 7은 기존 프로그램언어에 말하는 상수가 아닌 하나의 객체이다.
    
    [변수명 규칙]
    - 영문자 + 숫자 + _ 조합
    - 첫글자에 숫자는 안됨
    - 대소문자 구별
    - 길이 제한 없음
    - 예약어 사용 안됨       
'''


import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
#파이썬에서는 True, False  => true x false x
"""

print()

a = 7
b = 7
print(id(a))

"""
a = 777
b = 777
print(id(a))
print(id(b))

# 여러 변수 선언
a, b = 10,20
print('a + b = ',a+b)

# 두 변수의 값을 swap 할때
a, b = 10, 20
print(a, "   ", b)

a, b = b, a
print(a, "   ", b)

add = a + b;
print('a + b = ', add)
print('a + b = ' + str(add))

print (a is b)

####################################
# 변수명으로 str 사용 X

a, b = 3, 2;
print(a/b)
print(a//b)
print(a**b)

print(1j+2j) #3j
print('Hello' is 'Hello') #True 같은 주소인지...
print('Hello' is not 'Hello') #False

print('H' in 'Hello') #True
print('H' not in 'Hello') #False


a = 3.5
b = int(3.5)
print(a**((a // b) * 2))
print(((a - b) * a) // b)
b = 1.75
print((a * 4) % (b * 4))
