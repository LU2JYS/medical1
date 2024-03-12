'''
print("2단출력")
for i in range(1,10):
    print("2*{}={}".format(i,2*i))
    
for _ in range(5):
    n=int(input("단을 쓰세요>>>"))
    for i in range(1,10):
        print("{}*{}={}".format(n,i,n*i))
'''      
#중요>>>>>>>>>>>>>>>>>>>>
num=[]
#for문 을 사용해서 1-10까지 숫자를 채우세요
for i in range(1,11):
    num.append(i)
print(num)
num2=[]
for i in range(1,11):
    if i % 2==0:
        num2.append(i)
print(num2)

#1-10까지 짝수를 num2 리스트에 넣으세요

# 현재 1-10의합을 for을 통해 사용할수있다.
num=[1,2,3,4,5,6,7,8,9,10]
#num리스트를 사용해서 1-10의합을 구해봐라

s2=0
for i in range(len(num)):
    s2=s2+num[i]
    print(s2)
s3=0  
for n in num2:
    s3=s3+n
    print(n, end="")
s4=0
for i in range(len(num2)):
    s4= s4+num2[i]
    print(s4)
    
    
    

