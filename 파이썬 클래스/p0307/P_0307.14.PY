import random
alist=[0]*25
for i in range(5):
    
    alist[i]=1
random.shuffle(alist)

checklist=[[0]*5 for i in range(5)]
for i in range(5):
    for j in range(5):
        checklist[i][j]=alist[5*i+j]
        

viewlist=[["추첨"]*5 for i in range(5)]
for i in range(5):
    c_count = 1
answer_count=0

while True:
    print("\t      [5*5 checklist]")
    print("-"*45)
    print("",0,1,2,3,4,sep="\t")
    print("-"*45)
    for i in range(5):
        print(i,end="\t")
        for j in range(5):
            print(checklist[i][j],end="\t")
        print()
    print("-"*45)
    
    print("\t       [5*5 viewlist]")
    print("-"*45)
    print("",0,1,2,3,4,sep="\t ")
    print("-"*45)
    for i in range(5):
        print(i,end="\t")
        for j in range(5):
            print(viewlist[i][j],end="\t")
        print()
    print("-"*45)
    
    print("현재 도전 횟수 : {}번 째".format(c_count))
    x=(int(input("x좌표를 입력하세요")))
    y=(int(input("y좌표를 입력하세요")))
    if checklist[x][y]==1:
        viewlist[x][y]="당첨"
        answer_count+=1
    else:
        viewlist[x][y]="[꽝]"
        
    if answer_count==5:
        print("모두 정답확인")
        
    c_count+=1
    if c_count==10:
        print("모든 도전 종료")
        break
