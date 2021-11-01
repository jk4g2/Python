from pathlib import Path

# ------------------------------------------------
# 1. 경로의 상태보기
print(Path.cwd())
print(Path.home())


# ----------------------------------------------------
# 2. 경로(파일) 생성시간 알아보기
p1 = Path('Ex03_createPath.py')
tm = p1.stat().st_ctime
print(tm)

from datetime import datetime
print(datetime.fromtimestamp(tm))

# ------------------------------------------------
# 3. 디렉토리 생성
"""
p1 = Path('imsi')
p1.mkdir(exist_ok=True)

p2 = Path('temp2/test2/abc')
p2.mkdir(parents=True, exist_ok=True)
"""
# ------------------------------------------------
# 4. 파일 생성




# ------------------------------------------------
#  5. 경로 제거  #빈디렉토리일 경우 지워지고 아닐경우 지울수 없다.
p3 = Path('temp2')
p3.rmdir()