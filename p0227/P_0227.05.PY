#1-5 까지의 합을 구하시요
'''
sum=1+2+3+4+5

total=0
total=total+1 #t=1
total=total+2 #t=1+2
total=total+3 #t=1+2+3
total=total+4 #t=1+2+3+4
total=total+5 #t=1+2+3+4+5
print(total)
t=0
for i in range(1,6,1):
    t=t+i
print(t)

t=0
for i in range(1,11,1):
    t=t+i
print(t)

t=0
for i in range(1,101,1):
    t=t+i
print("1부터 100의 합은 : {} 입니다".format(t))
'''

n1=int(input("첫번째 숫자를 넣으세요>>>"))
n2=int(input("두번째 숫자를 넣으세요>>>"))
t=0
for i in range(n1,n2+1):
    t=t+i

print("합은 : {} 입니다".format(t))