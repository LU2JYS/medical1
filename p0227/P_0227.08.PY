from random import*
'''
n1 =randrange(1,10)
n2 =randrange(10)
n3 =randrange(1,10)

print(n1,n2,n3)
'''
lotto=[]#로또 리스트에 랜던하게 배열된다.>>>>>>>중요
for i in range(6): #범위대로 숫자갯수가 나타난다...
    a=randint(1,10) #1에서 10까지 랜덤하게 나온다
    lotto.append(a) 
print(lotto)    
    
mynum=[]# 하나하나씩 쌓여서 리스트에 들어간다.>>>>>중요
for i in range(6): 
    b=int(input("숫자를 입력하세요>>"))
    mynum.append(b)

print(lotto)
print(mynum)

