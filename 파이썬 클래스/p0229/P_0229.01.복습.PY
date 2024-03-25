'''
for 변수 in 반복가능데이터:
    수행문장
    
    
    
for 요소 in 리스트명:
    반복하고싶은 실행문
    
for i in range(시작값,끝값+1,증가값):
        반복하고싶은 실행문
        >>실행문이 i가 시작값부터 끝값까지 반복
        
for i in range(반복수1):
        실행문1
        for j in range(반복수2):
        실행문2
        
>>>>실행문1이 반복수1만큼 반복
>>>>실행문2는 반복수1*반복수2 반복
'''
'''
for i in range(5):
    print("i=",i)
    print("-"*25)
    for j in range(3):
        print("j=",j)
    print("하단부","-"*25)
    
#구구단
#2단출력
for i in range(1,10):
    print("{}*{}={}".format(2,i,2*i))
    
#구구단 전체 출력
for i in range(2,10):
    print("{}단".format(i))
    for j in range(1,10):
        print("{}*{}={}".format(i,j,i*j),end="")
    print()
            
for i range(1,10):
    for j in range(2,9):
            print("{}*{}={}".format(j,i,i*j),end="\t")
            print()
            
'''

# 리스트변수명 =[요소1, 요소2, 요소3......]
#요소가 될수있는 타입이 :bool, int , float,string,list

fruit=["딸기","사과","배","수박","귤"]
print(fruit[4])
print(fruit[-1])

fruit.append("포도")
print(fruit)
fruit.remove("배")
print(fruit)
del(fruit[3])
print(fruit)

if "한라봉" in fruit:
    print("있음")

for f in fruit:
    print(f)
    
for i in range(len(fruit)):
    print(fruit[i])
    
num=[[10,20,30],
    [100,200,300],
    [1,2,3]]
for n in num:
    print(n)
for n in num:
    for a in n:
        print(a)
        
for i in range(len(num)):
    for j in range(len(num)):
        print(num[i][j])
        
#리스트에 숫자를 넣을때 한줄로 표현하기>>>>>>>>>>>>>>>>>>중요

a=[i for i in range(1,11)]
print(a)
a=[0 for _ in range(10)]
print(a)

#[표현식 for 항목 in리스트if조건문]>>>>>>>>>>>>>>>>>>>중요
a=[i for i in range(100) if i%2==0]
print(a)
b=[i for i in range(1,11)]
print(b)
c=[i+1 for i in b]
print(c)

names=["홍길동","유관순","이순신","강감찬","김구"]
for i in range(len(names)):
    print("{}.{}".format(i+1,names[i]))
    
i=0
for name in names: # index : 0부터 시작
    i=i+1
    print("{}.{}".format(i,names))
    
for i , name in enumerate(names,start=1): # index : 1부터 시작
    print("{}.{}.".format(i+1,name))
    
    for i , name in enumerate(names): # index : 0부터 시작
        print("{}는{}번째에 있습니다.".format(name,i))
    