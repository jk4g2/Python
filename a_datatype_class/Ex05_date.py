import datetime #datetime이라는 패키지를 전부 import
today = datetime.date.today();
print('today is', today)

from datetime import date, timedelta, datetime
 #datetime이라는 패키지안에 date라는애만 import 이렇게되면 date만 사용 가능.
 #timedelta => 몇일전 몇일후 계산가능
 #datetime 시분초 출력 쌉가능
weekdays = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
today = date.today()
print('today is', today)
print('today is', today.year)
print('today is', today.month)
print('today is', today.day)
#print('today is', days[today.weekday()])

# 날짜 계산할떈 SQL에서 가져오자!

# 날짜 계산
print('어제:',today + timedelta(days=-1))
print('7일전:',today + timedelta(days=-7))
print('100일 후:',today + timedelta(days=100))

# ************************************************
# 날짜형 <-> 문자형
# date -> str : strftime()
# str -> date : strptime()

today = datetime.today()
print(today)
print(type(today))
print(today.strftime('%Y년 %m월 %d일 %H:%M')) # **********************************************************

naljja = '2021-08-10 12:50:12' #문자열 값
naljja_datetime = datetime.strptime(naljja,'%Y-%m-%d %H:%M:%S') # ***************************************
print(type(naljja_datetime))
