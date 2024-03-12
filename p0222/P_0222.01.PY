a=1 #함수(함수는 중괄호를 사용)
print() # 파이썬에서 기본적으로 제공
print('hello world') #문자열을 출력
print(20)
print(100+200) #숫자출력이 가능하고 사칙연산을 할 수있다.
print('10',20) # ,를 사용하면 변수 타입이 달라고 출력이 가능
print('10',+20) # +를 사용할 경우에는 같은 타입만 출력만 가능
print(int('10')+20) 
print('10'+str(20))

print('hello'*10)

# %d는 정수 %f는 실수 %s 문자열을 나타낸다
print('%d,%d'%(5,2))
print('%d,%f,%s'%(5,2.14,"abc"))

# 소수점까지만 출력
print('%.2f'%(123.456789))

#총 10자리 빈칸은 0으로 소수점은 3자리까지 출력
print('%010.3f'%(123.456789))

print("{:.1f}, {:d}, {:s}".format(758.12,50,"string"))

# \n은 줄바꿈
print('파이썬 수업을 진행합니다.\n파이썬 기본편입니다.')
# \t은 띄어쓰기
print('파이썬 수업을 진행합니다.\t파이썬 기본편입니다.')

print('파이썬 수업을 진행합니다.\
파이썬 기본편입니다.')

#print","의 사용
print('산에 올라가면 "야호"하고한다')
print("산에 올라가면 '야호'하고한다")

#변수사용
#변수 bool, int, float,str형이 있다.
#변수는 대소문자를 구분한다
myvar = 10
myvar = 20

#변수는 언더바를 포함할수있고 숫지로 시작하면 된다.
num1 = 10
num2 = 20

#변수는 예약어를 사용할수없다.
# if = 100
# True = 100

#변수는 마지막으로 입력된것을 저장한다.
a = 10
b = 30

print(a)
print(a+b)
print(a-b)
var2 = 200
var1 =var2 +100
print(var1,var2)

#입력받기
# input() : 입력을 받기위한 함수이다.

#name = input('이름을 입력하세요 :')
#print('당신의 이름은,'+name+'입니다')

#age = input('나이을 입력하세요 :')

#숫자로 바궈주기
# 1. age = int(input('나이를 입력하세요:'))
# 2. age = int(age)
# 3.
 #print('당신의 나이은 {}입니다'.format(int(age)+1))

print('-----------------------------------------quiz')
num1=input('구구단을 입력하시요:')
print('구구단 2*1 ={} 입니다'.format(int(num1)*1))
print('구구단 2*2 ={} 입니다'.format(int(num1)*2))
print('구구단 2*3 ={} 입니다'.format(int(num1)*3))

print('-----------------------------------------quiz')
num1=10
num2=3
print("{}+{}={}".format(num1,num2,num1+num2))
print("{}-{}={}".format(num1,num2,num1-num2))
print("{}*{}={}".format(num1,num2,num1*num2))
print("{}/{}={:.3f}".format(num1,num2,num1/num2))

print('-----------------------------------------quiz')
kor= 100
eng= 90
math= 80
avrg=(kor+eng+math)/3
print("평균은 :{}점 입니다".format(int(avrg)))

print('-----------------------------------------quiz')
kor= 100
eng= 100
math= 100
print('평균은 :',(int(kor)+int(eng)+int(math))/3,"점 입니다")

print('-----------------------------------------quiz')
kor=input("국어점수를 입력하시요")
eng=input("영어점수를 입력하시요")
math=input("수학점수를 입력하시요")
print('평균은 :',(int(kor)+int(eng)+int(math))/3,"점 입니다")

print('-----------------------------------------quiz')
kor=input("국어점수를 입력하시요")
eng=input("영어점수를 입력하시요")
math=input("수학점수를 입력하시요")
kor =int(kor)
eng =int(eng)
math =int(math)
avg=(kor+eng+math)/3
print("평균은 :{}점 입니다.".format(avg))