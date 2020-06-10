import datetime
print(datetime.datetime.now()) #2020-06-10 23:16:09.900577
start_time = datetime.datetime.now()
print(type(start_time)) # <class 'datetime.datetime'>

# replace() 함수는 본인을 바꾸는 것이 아니라 본인을 바꾼값을 return
# 바뀐 값을 저장하려면 별도로 지정이 필요하다.
start_time = start_time.replace(year=2017, month=2, day=1)
print(start_time) #2017-02-01 23:17:35.988094

# 날짜 설정 : 년 월 일 시 분 초 설정 가능
start_time = datetime.datetime(2016, 2, 1, 0, 0)
print(start_time) #2016-02-01 00:00:00

# datetime class는 - 연산을 지원
how_lond = start_time - datetime.datetime.now()
print(type(how_lond))
#<class 'datetime.timedelta'> = days 와 second로 남은 시간을 계산

print(how_lond) #-1592 days, 0:38:16.494339
print(how_lond.seconds, how_lond.days) #2106 -1592
