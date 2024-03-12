import datetime #날짜 관련 기능을 가져옴
now=datetime.datetime.now()
print(now)
print(now.year) #연도
print(now.month) #월
print(now.day) #일

print(now.hour)
print(now.minute)
print(now.second)

print("-------------------------------------------")

h=now.hour
if h<12:
    print("현재는 {}시로 오전입니다".format(h))
else: 
    print("현재는 {}시로 오후입니다".format(h))
    
print("-------------------------------------------")
m=now.month
if m %2==0:
    print("현재는 {}월로 짝수달입니다".format(m))
if m %3==0:
    print("현재는 {}월로 홀수달입니다".format(m))
    
print("-------------------------------------------")

if 3<=m<=11:
    print("월로 겨울이 아닙니다")
else:
    print("겨울입니다")