'''
a=[]
for i in range(0,26):
    a.append(i+1)
print(a)
'''

#이차원 리스트만들기 
#예제 1번
b=[]
b_i=[]
for i in range(0,25):
    if (i+1)%5==0:
        b_i.append(i+1)
        b.append(b_i) #[1,2,3,4,5,6,]
        b_i=[]
    else:
        b_i.append(i+1)
print(b)
        

#예제 2번
#a=[[],[],[],[],[]]
#a=[[0]*5 for _ in range(5)]
a=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]] #초기화방법
value=1
for i in range(0,5): #0,1,2,3,4
    for j in range(0,5): #0,1,2,3,4
        a[i][j]=value
        value+=1

print(a)






