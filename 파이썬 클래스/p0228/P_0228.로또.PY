from random import*

n1=randrange(1,11)
n2=randint(1,10)

#랜덤한숫자6개 넣고 로또리스트에 넣고
#내가 입력한 6개는 mynum리스트에 넣어주세요
lotto=[]
for i in range(6):
    a=randint(1,11)
    lotto.append(a)


mynum=[]
for i in range(6):
    b=int(input("숫자를 입력해주세요"))
    mynum.append(b)

print(lotto)
print(mynum)