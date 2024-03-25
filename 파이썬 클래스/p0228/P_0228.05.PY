from random import*

n1=randrange(1,11)
n2=randint(1,10)

#랜덤한숫자6개 넣고 로또리스트에 넣고
#내가 입력한 6개는 mynum리스트에 넣어주세요

lotto=[]
l=[1,2,3,4,5,6,7,8,9,10]
for i in range(50):
    tmp=randint(0,9)
    l[0],l[tmp]=l[tmp],l[0]
print(l)
'''
for i in range(6):
    lotto.append(i)
print(lotto)

mynum=[]
for i in range(6):
    b=int(input("숫자를 입력해주세요"))
    mynum.append(b)
print(mynum)
'''