# 0-20사이의 5의 배수로 이루어진 리스트를 리스트를 만들어보세요
'''
num=[]
for i in range(21):
    if i%5==0:
        num.append(i)     
print(num)
'''
'''
lan=["c","python","java","jquery","css"]
for n in lan:
    print(n)

for i in range(len(lan)):
    print(lan[i])
    
for i in range(len(lan)):
    print(str(i+1)+".",lan[i]) # str 앞에 문자나 숫자 출력 가능, +로 "부호" 가능
'''    
'''  
num=[1,-1,2,3,-4,5,6,-8,9,-10]
#양수면 양수 음수면 음수 출력
#1 :음수 
#-1 :음수 
#2 :양수 
for i in range(len(num)):
    if num[i]>0:
        print(num[i],":양수")
    else:
        print(num[i],":음수")
'''  
# 이름,아이디,비밀번호 (input)으로 입력받아라
# 5명을 입력받아서 member list 들어가게


member=[] #예시[[홍길동,aaaa,1111],[유관순,bbbb,2222]]
for i in range(5):
    name=input("이름을 입력하세요>>>")
    id=input("아이디를 입력하세요>>>")
    pwd=int(input("비밀번호를 입력하세요>>>"))    
    p=[name,id,pwd]
    member.append(p)

print("-"*35)  
print("이름\t아이디\t비밀번호")
for i in range(len(member)):   
    print("{}\t{}\t{}".format(member[i][0],member[i][1],member[i][2]))

    

    














