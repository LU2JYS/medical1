#대입연산자
# =
a=3 #3을a에 넣는다
a +=1 #이런식으로 많이 줄여쓴다.
print(a)

a+=2
print(a)
a+=100
print(a)

# +=, -=, *=, /=, %=, //=, **=
# 즉 좌변과 우변에 동일한 변수명이 사용될 경우
# 변수명을 생략하고 축약할수있다.

a=3
b=2
a*=2+b # a = a*(2+b) 이렇게 계산이된다.
# a = a*2+b 오답
print(a)

print('-----------------------------------------quiz')
#num이 20에서 시작해서 값이 누락됨 밑으로 누적이된다
num=20
num += 2 #num = num +2
print(num)
num -= 2 #num = num -2
print(num)
num *= 2
print(num)
num /= 2
print(num)