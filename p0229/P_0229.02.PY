#while 반복문이다
'''
for i in range("시작,끝+1,증가값)
    수행할문자

while 조건식:
    실행할 문자
    
변수 = 시작값 ex) i=0
while 변수<끝값 : #이 조건이 참일때
    반복구문
    변수 =변수+증가값 #i=i+1

'''
''' 
# for 문으로 안녕하세요 3번 출력
for i in range(0,3,1):
    print("for :안녕하세요")
    
#while문으로 작성
i=0
while i <3:
    print("while :안녕하세요")
    i=i+1
    
for i in range(0,11):
    print(i, end=" ")
    
i=0 
while i<11:
    print(i)
    i=i+1
'''
'''
i=1
while i<11:
    if i %3 ==0:
        print(i)
    i=i+1
    
i=1
while i<101:
    if i %3 ==0:
        print(i)
    i=i+1
    

i=1
sum=0
while i in range(1,101):
    sum+=i
    print(sum)
sum1=0

j=1
while j<=100:
    sum1+=j
    j+= 1
print(sum1)
'''
'''
n=0
while n<100:
    print(n, end=" ")
    if n==4:
        break #1-100까지인데 4에서 브레이크를 걸어서 0-4까지만 출력된다.
    n=n+1
    
breakletter= input("중단할 문자를 입력하세요")
for letter in "python":
    if letter ==breakletter:
        break
    print(letter)
    
while True:
    n=input("숫자를 입력해주세요")
    print(n)
    if n =="0":
        print("종료")
        break
print("프로그램 종료")
'''
#무한 계산기 프로그램>>>>>>>>>>>>중요
while True:
    n1=int(input("첫번째 숫자를입력 하세요>>>"))
    if n1 ==0:
        print("종료되었습니다.")
        break
    n2=int(input("두번째 숫자를입력 하세요>>>"))
    cal=input("(+,-,/,*,)입력 하세요>>>")
    if cal =="+":
        print("{}+{}={}입니다".format(n1,n2,n1+n2))
    elif cal =="-":
        print("{}-{}={}입니다".format(n1,n2,n1-n2))
    elif cal =="*":
        print("{}*{}={}입니다".format(n1,n2,n1*n2))
    elif cal =="/":
        print("{}/{}={}입니다".format(n1,n2,n1/n2))
print("프로그램 종료")

    