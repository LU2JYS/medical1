'''
for i in range(1,10):
    print("2*{}={}".format(i,2+i))
    
for i in range(2,10)
    n=int(input("단을 쓰세요"))
    for i in range(1,10):
        print("{}*{}={}".format(n,i,n*1))
        '''
'''        
for i in range(3):
    print('안녕')
    for j in range(2):
        print('반가워')
        
for i in range(2,10):
    for j in range(1,10):
        print("{}*{}={}".format(i,j,i*j))
'''   
'''       
for j in range(5):
    print(j+1,"번째 출력")
    for i  in range(1,6):
        print(i,end=" ")
    print()
print("for끝")
'''  
'''
for i in range(1,10):
    if i %2==0:
        print("[{}단]".format(i))
        for j in range(1,10):
            print("{}*{}={}".format(i,j,i*j),end=" ")
    print()
    
for i in range(1,10):
    if i %2==1:
        print("[{}단]".format(i))
        for j in range(1,10):
            print("{}*{}={}".format(i,j,i*j),end=" ")
    print()
        
'''
'''
n1=int(input("숫자를 입력하세용>>>"))
n2=int(input("숫자를 입력하세용>>>"))
if n1>n2: #크기비교해서 n1이 더크면 n2,n1값
    n1,n2=n2,n1
for i in range(n1,n2+1):
        print("[{}단]".format(i))
        for j in range(1,10):
            print("{}*{}={}".format(i,j,i*j),end=" ")
        print()
'''
# 한줄주석은 control+/
#tab :들여쓰기
# shift + tab (들여쓰기 삭제)
# alt + shift + 위아래 방향키
'''
num=[100,200,300,400]
#for 문을 사용해서 하나씩 출력해보자
for n in num:
    print(n)
    
for i in range(len(num)):
    print(num[i],end="\t")
    
numlist=[[1,2],[3,4],[5,6]]
for n in numlist:
    for a in  n:
        print(a, end="")
    print()
    # print(n,end="\t")
    
for i in range(len(numlist)):
    for j in range(len(numlist[i])):
        print(numlist[i][j],end=" ")
    print()
    
'''
'''
f= [["딸기",100,1000],["수박",100,500]
    ,["사과",100,1200],["귤",100,300]]
for n in f:
    print(n)

for i in range(len(f)):
        
        print(f[i][0],end=" ")
        print()
'''  
   
#스코어 안에 다 더한값을 나타내어라
score=[90,80,70,100,95,85,100]
total=[]
sum=0
for s in score:
    sum += s        
print(sum)

    
