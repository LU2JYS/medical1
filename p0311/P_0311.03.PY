# a=1 #변수
# print() #이름뒤에 ()있으면 함수 /첫글자면 함수/
# #Cl=클래스 #앞에 대문자면 클래스


import co

coffee = 0
while True:
    print("1. 보통커피")
    print("2. 설탕커피")
    print("3. 블랙커피")
    coffee = int(input("어떤 커피를 드릴까요?"))
    print()
    # 함수호출
    co.machine(coffee)