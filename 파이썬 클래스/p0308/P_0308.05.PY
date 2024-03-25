# a= 1000000
# b="안녕하세요. 반갑습니다. 저는 홍길동입니다"
# print(len(b)) #문자열 길이를 출력
# print(b[0]) #문자열 위치를 출력가능
# print(b[2])
# print(len(str(a)))
# print(b[2:5]) #마지막번호 앞까지 출력




# 문자열
# a="안녕"
# b=100000
# c=20000
# d="1000000"
# print(b+c)
# print(b+int(d)) #타입이 같아야 사칙연산이 가능하다.

# a=input("문자를 입력하세요")
# print("현재 입력한 문자 길이: len(a)")

# a = [1234,11111,1,145,20,1323456547]
# #리스트에 각 숫자에 길이를 출력하세요
# # print(len(str(a[0])))
# for i in a:
#     if i%2==0:
#         print("숫자 : {}, 길이 :{} ".format(i,len(str((i)))))
        
# title="혼자공부하는파이썬수업"
# for i in range(len(title)):
#     print(title[i])

# print(1,2,3,4,5,sep="*")


# #역순으로 출력해보자>>>>>>>>>>>>>>중요
# title=input("문자를 입력하세요")
# for i in range(len(title)): #5번 돈다.
#     print(title[(len(title)-1)-i],end="")    

shape=["spadE","diamonD","hearT","cloveR"]
for i in shape:
    print(i.upper())
    print(i.title())
    print(i.swapcase())
    


