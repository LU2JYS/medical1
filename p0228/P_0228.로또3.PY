from random import*
mynum=[] #입력을 받아 1-45사이 입력받아 6자리생성
lotto=[] #1-45사이의 랜덤 6개 생성
ok =[]
for i in range(6):
    s=int(input("{}번째 숫자를 입력해주세요>>".format(i)))
    mynum.append(s)

l=[]
for i in range(1,46):
    l.append(i)
print("로또숫자 : {}".format(l))
for i in range(200):
    tmp=randint(0,44)
    l[0],l[tmp]=l[tmp],l[0]
print("로또숫자 : {}".format(l))

for i in range(6):
    lotto.append(l[i])
print("로또숫자 : {}".format(lotto))


lotto=[1,2,3,4,5,6] 
mynum=[7,8,9,10,5,7]
for i in range(6):
    if mynum[i] in lotto:
        ok.append(mynum[1])
    
print("입력한숫자 : {}".format(mynum))
print("로또 숫자 : {}".format(lotto))
print("당첨된 숫자 : {}".format(ok))
    