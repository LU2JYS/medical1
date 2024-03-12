# 출력 부분이 제일 중요하다 (print)
print("문자열") #문자열 출력
print(10.123) #숫자 출력
print(123*111) #사칙연산 가능

# %d는 정수 ,%f는 실수 ,%s는 문자열을 나타낸다
print("%d %f %s "%(10,12.123,"문자")) 
print("%.2f"%(22222.2222222)) #소숫점 둘째까지만

#str.format
print("문자열을 쓰고 {}".format(1))

#정수 3가지 방법이 있다.
print("{0:d}".format(123))
print("{0}".format(123))
print("{}".format(123))

#실수 버전
print("{0:f}".format(123.456789))
print("{0}".format(132.46789))
print("{}".format(123.46798))


#문자 버전
print("{0:s}".format("문자"))
print("{0}".format("하잉"))
print("{}".format("헬로"))

print("{} {} {}".format("빨", "주" ,"노"))

#변수
number =10 #정수, <<int 타입>>
pi = 3.14  #실수 ,<<float타입>>
result=True #bool타입이다
str1="문장입니다." #string
ch= "A" #문자

s1="1+1=2"
print(s1)
s2 ="{}+ {} ={}".format(1,1,2)
print(s2)

a=100
a=a+1 #a+=1 도 같은 방법이다.
print(a)

#크기 비교 참 거짓 판별
a,b, = 10,20
a=10
b=20

print(a==b)
print(a!=b)
print(a>b)
print(a>=b)

#논리연산자
# and (둘이 참이어야함 ) or (둘중하나라도 참이면 참)
#not  (참은 거짓) (거짓은 참)으로 반대로 나온다
a,b,c, = 100,200,150
result=(a>c) and (b>c)
print(result)


'''#입력받기 input("내용을 쓰시요") 은 항상 문자열이므로 숫자가 들어가면 int을 씌어줘야한다
name=input("이름을 입력하세요")
print("당신의이름은{}입니다.".format(name))
age=int(input("이름을 입력하세요"))
print("당신의이름은{}입니다.".format(age+1))
'''
# if 조건문
# if 조건문1
#   실행문1
#else :
#   실행문1

f="apple"
if f =="apple":
    print("먹는다")
else:
    print("버린다.")

