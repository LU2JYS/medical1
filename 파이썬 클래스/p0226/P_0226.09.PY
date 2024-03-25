'''
numl =[]

# 0에서 부터 5까지 넣어보세요
#append
print(numl)
numl.append(0)
numl.append(1)
numl.append(2)
numl.append(3)
numl.append(4)
numl.append(5)
print(numl)

# for i를 통해서 해보자>>>>>>>>>>>중요
num =[]
for i in range(6):
    num.append(i)
print("num[]=",num)

aa=[1,2,3,4] #index를 사용해서 읽기
for i in aa:
    print(i)
for i in range(0,4):
    print(aa[i])
'''
'''  
f=["사과","복숭아","딸기","포도","자몽"]
for i in f:
    print(i)
for i in range(len(f)):
    print(f[i])
    '''
'''
c=["미국","영국","호주","캐나다","일본","중국"]
for i in c:
    print(i)
for i in range(len(c)):
    print(c[i]) #대괄호 중요하게 생각하자
    
    
num=[]
for i in range(1,101):
    num.append(i)
print("num[]=",num)
'''
'''
#반복문 안에 if문을 사용
for i in range(10):
    print(i)
    if i == 9 :
        print("9입니다")
        
lan = ["영어","스페인어","일본어","중국어"]
for i in lan:
    if i=="영어":
        print("영어입니다")
    else:
        print("다른언어입니다.")
'''
'''
for i in range (2,102,2):
    print(i,end=", ")
    
for i in range (100):
    if (i+1) %2==0:
        print(i+1,end=", ")
    
print()
for i in range (7,101,7):
    print(i,end=", ")
for i in range (100):
    if (i+1) %7==0:
        print(i+1,end=", ")
    
aa=[100,90,86,79,72,52,98,94]
for i in aa:
    print(i)
    if i>=80:
        print("합격입니다")
'''
f=["사과","복숭아","딸기","포도","자몽"]
for i in f:
    print(i)
    if i=="딸기":
        print("딸기있습니다.")
    else:
        print("다른과일입니다.")
    

num =[1,2,5,7,9,10,23,43]
#1
for i in num:
    if i % 2 ==0:
        print(i,"짝수")
    else:
        print(i,"홀수.")

#2
for i in range (len(num)):
    if num[i]%2==0:
        print(num[i],"짝수입니다.")
    else:
        print(num[i],"홀수입니다.")