import first  # first 모듈을 가져옴

print('second.py __name__:', __name__)  # __name__ 변수 출력
"""
본인이 본인을 실행하게되면 __name__ = __main__ 가되고
다른 파일을 import가 되는곳은 그 파일의 이름이 된다.
"""
