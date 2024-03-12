#산술 연산자
# +-/*
a=5
b=3
result=a+b
result=a-b
result=a*b
result=a/b
print(result)

result =a//b #몫
print(result)

result =a&b #나머지 >>>>>>>>>>>>꼭 기억하기
print(result)

result=3**5 #제곱
print(result)

c=10
d=20
c,d = 100, 200

#산술연산자 우선순위
#곱셉,나눗셈 먼저하고 그다음 덧셈 뺄쌤 순으로 진행
# (괄호가 있으면) 먼저 계산진행 왼쪽에서 오른쪽으로 진행
r1=2+2-2*2/2*2

#괄호사용으로 추천 #곱하기 나눗셈이 먼저이므로 괄호를 하여줌으로써 보기편하다
r2= 2-(2/2)

#다른 자료형으로 연산
str1 ="문자열"
n1 =10
print(str1*n1)
# print(str1+n1) #에러

#문자열이 정수나 실수일 경우 int() float()를 사용해서 변환
s1= "100"
s2="10.123"
print(int(s1)+1)
print(float(s2)+1)

# n= int("안녕하세요") #오류발생 숫자가 아닌것을 변환 불가능

s1= 100
s2=10.123
print(str(s1)+"1")
print(str(s2)+"1")

p=12345679
print("010"+str(p))#문자를 숫자로 변경

#숫자 두개를 입력받아서 나누기값, 몫, 나머지값을 구하시요

#n1=4
#n2=2
#result=n1/n2
#print(result)

#result=n1//n2
#print(result)

#result=n1&n2
#print(result)

print('-----------------------------------------quiz')
n1=input("값을 입력하시요")
n2=input("값을 입력하시요")
n1=int(n1)
n2=int(n2)
print("나누기값은 {}은 입니다".format(n1/n2))
print("몫값은 {}은 입니다".format(n1//n2))
print("나머지값은 {}은 입니다".format(n1&n2))

print('-----------------------------------------quiz')
n1=input("값을 입력하시요")
n2=input("값을 입력하시요")
n1,n2=int(n1),int(n2)
print("나누기: {:.1f}\n몫: {}\n나머지: {} ".format(n1/n2,n1//n2,n1&n2))