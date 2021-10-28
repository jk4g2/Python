#myfile.py

# 1. 전체 모듈을 임포트 했을 때,
"""
import mymodule

print(mymodule.get_date())
print(mymodule.get_weather())
"""


# = > 실행 순서: mymodule.py 파일 싹다 => myfile

# 2. 별칭 부여시
"""
import mymodule as my
print(my.get_date())
print(my.get_weather())
"""

# 3. 모듈에서 필요한 부분만 임포트 할때
"""
import mymodule from get_weather
print(get_weather()) # 모듈명을 쓰면 안됨
print(get_date()) #필요한부분 (get_weather())만 임포트 했기때문에 get_Date는 사용 불가능.
"""

"""
import mymodule from get_weather,get_date()
print(get_weather())
print(get_date())
"""

# 4. 함수 별칭 부여시..
"""
from mymodule import get_weather as gw
print(gw())
"""
