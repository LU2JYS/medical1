'''
member=[]
for i in range(3):
    name=input("이름을 입력하세요>>")
    score=int(input("점수을 입력하세요>>"))
    member=[name,score]
    member.append(i)
'''
'''
member=[["홍길동",90],["유관순",91],["이순신",95]]
for i in range(len(member)):
    print(member[0][0])
    print(member[1][0])
    print(member[2][0])
    print(member[0][1])
    print(member[1][1])
    print(member[2][1])
    
    if i in range(3):
        name=member[i][0]
        score= member[i][1]
        if score >=60:
            print("{}님 {}합격입니다".format(name,score))
        else:
            print("{}님 {}불합격입니다".format(name,score))
'''  
'''           
t=0
for i in range(1,101):
    t=t+i
    print(t)

t=0
for i in range(1,101):
    if i %2==0:
        t=t+i
        print(t)
        
t=0
for i in range(1,101):
    if i %2==1:
        t=t+i
        print(t)
'''     
'''  
t=0
for i in range(1,11):
    t=t+i
    print(t)
        
        
num=[1,2,3,4,5,6,7,8,9,10]
s1=0
for i in range(len(num)):
    s1=s1+num[i]
    print(s1)
'''
n1=int(input("첫번째 숫자를 입력해주세요>>>"))
n2=int(input("두번째 숫자를 입력해주세요>>>"))
sum=0

if n1<n2:
    for i in range(n1,n2+1):
        sum=sum+i
        print(sum)
    print("합은 : {} 입니다".format(sum))
    

odd_list=[]
for i in range(n1,n2+1):
    if i %2==1:
        odd_list.append(i)    
print(odd_list)


