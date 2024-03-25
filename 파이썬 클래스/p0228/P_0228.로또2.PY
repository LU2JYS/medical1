from random import*
lotto=[]
mynum=[2,5,1,9,3,7]

num =[1,2,3,4,5,6,7,8,9,10]
for i in range(10):
    tmp=randint(0,9)
    print(tmp)
    num[0],num[tmp]=num[tmp],num[0]
    print(num)
    
for i in range(6):
    lotto.append(num[1])
    print(lotto)
ok=[]
for i in range(len(mynum)):
    #print(mynum[i])
    if 2 in lotto:
        ok.append(mynum[i])
print(ok)
            