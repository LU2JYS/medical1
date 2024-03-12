#변수 bool,int, float,string
a=False
b=300
c=3.14
d="문자열" #string문자열

#input() > 콘솔창에서 입력은 받는다
#e= input()#input 문자열로 입력을 받는다

# if 조건문1:
#     실행문1
#elif 조건문 2:
#      실행문2
#else:
#     실행문3
# >> elif,else 는 생략이 가능
#if를 건너뛰고싶은 경우는 pass를 사용
n=10 #(input("숫자를 입력해주세요>>"))
'''
if n>=0:
    print("양수")
    if n%2==0:
        print("짝수")
    else:
        print("홀수")
else:
    print("음수")
'''

'''
반복문
for 변수 in 반복가능한데이터:
실행문
''' 
'''
#순차적으로 커질때 range를 사용한다
for i in range(0,3,1): #range(시작값,끝값+1,증가값)
    print("hi")
    
for i in range(5):
    print(1)

for i in range(1,11):
    print(i)
    
a=10
b="안녕하세요"
for i in range(5):
    print(i)
    a=a+1
    print(a)
    
    print(b)
    
'''
'''
#입력 :이름,점수(5명의 이름과 점수를 입력받습니다.
# 60점이상이면 합격, 60점 미만이면 불합격을 출력
#출력의 형태는 홍길동님 합격입니다,불합격입니다
for i in range(5):
    name=input("이름을 넣어주세요>>>")
    score=int(input("점수을 넣어주세요>>>"))
    if score>=60:
        print("{} 합격입니다".format(name))
    else:
        print("{} 불합격입니다".format(name))
        '''


# list
# 변수명 = [요소1,요소2,.....]
'''
fruit=["딸기","사과","배","포도","한라봉"]
f1=fruit[1]
print(f1)

if "귤" in fruit:
    print("귤이 있어")
else:
    print("귤이 없어")
    
for f in fruit:
    print(f)
    
for n in [100,200,300,400]:
    print(n)
    
for i in range(len(fruit)):
    print(i)
    print(fruit[i])
'''  
'''  
num= [[1,2,3],[4,5,6],[7,8,9]]
print(num[0])
print(num[0][2])

for i in range(len(num)):
    print(num[i][0])
'''
con=["미국","영국","일본","중국","스페인"]
lang=["영어","영어","일본어","중국어","스페인어"]
con.append("프랑스")
print(con)
lang.append("프랑스어")
print(lang)

for i in range(6):
    print("{}은 {}를 사용합니다".format(con[i],lang[i]))
    