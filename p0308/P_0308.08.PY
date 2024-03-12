import random
random_num=str(random.randint(10000,99999)) #범위를 지정해준다.
print("[랜덤숫자 맞추기]")
print("랜덤숫자 : ",random_num)
a_input=input("숫자 5자리를 입력하세요")

#숫자자리로 확인해서 맞춘개수를 출력하세요
cnt=0
for i in range(len(str(random_num))):
    if random_num[i] == a_input[i]: #같은자리수를 비교한다.
        cnt+=1   
print("맞은갯수:",cnt)
        