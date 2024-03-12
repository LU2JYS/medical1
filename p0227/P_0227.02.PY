'''
#반목문

for ,while

for 변수 in 반복 가능한데이터:
   수행문
   
for 카운터변수  in range (시작값, 끝값+1, 증감값)

for i in range(0,10,1): #0,1,2,3,4,5,6,7,8,9
    print(i,"1: 수행문입니다.")
    
for i in range(10,0,-2): #0,1,2,3,4,5,6,7,8,9
    print(i, "2: 수행문입니다.")
    
for i in range(0,3): #세번 반복해라
    print("두번째 수행문입니다.")
    
for i in range(5): #5번 반복해라
    print("세번째 수행문입니다.")
print("-"*35)
for i in range(3):
    print(i)
    
for _ in range(7):
    print("안녕하세요")
'''
'''
l1=[100,200,300,400,500,600]
for n in l1:
    print(n)
    
for i in range(len(l1)):
    print(i)
    print(l1[i])
'''    
'''  
for i in range (1,101,2):
    print(i,end='')

for i in range(100):  
    if (i+1)%2==1:
        print(i+1, end="")  
        
for i in range(48,0,-6): 
    print(i,end="")
'''      



    
    
l1=[100,200,300,400,500,600]
for n in l1:
    print(n)
    
for i in range(len(l1)):
    print(i)
    print(l1[i])