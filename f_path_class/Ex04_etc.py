"""
경로 이동은  Path 모듈로 안되어 os 모듈이 필요하다
"""
from pathlib import Path
import shutil

#파일 복사
#shutil.copy('Ex01_Path.py',Path('temp2/test2/abc/test.py'))

#폴더 복사
#shutil.copytree('temp2','../copytemp')

#폴더 삭제
shutil.rmtree("temp2")