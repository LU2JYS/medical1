import random
alist=[0]*25

for i in range(5):
    alist[i]=1
    
random.shuffle(alist)

checkList=[[0]*5 for i in range(5)]
for i in range(5):
    for j in range(5):
        checkList[i][j]=alist[5*i*j]
        
viewlist=[["추첨"]*5 for i in range(5)]
c_count=1
answer_count=0
my_xy=[]
while True:
    print("/t[5*5 좌표]")