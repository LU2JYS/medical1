
for i in range(10): #반복하고싶은것은 맨위에 달고 들어가자
    a=int(input("첫번째 숫자를 입력하세요"))
    b=int(input("두번째 숫자를 입력하세요"))
    cal=input("수식을 입력하세요(+,/,*,-)")
    if cal =="+":
        print("{}+{}={}입니다".format(a,b,a+b))
        print(i+1,"번 실행하였습니다.")
    elif cal =="-":
        print("{}-{}={}입니다".format(a,b,a-b))
        print(i+1,"번 실행하였습니다.")
    elif cal =="*":
        print("{}*{}={}입니다".format(a,b,a*b))
        print(i+1,"번 실행하였습니다.")
    elif cal =="/":
        print("{}/{}={}입니다".format(a,b,a/b))
        print(i+1,"번 실행하였습니다.")
        