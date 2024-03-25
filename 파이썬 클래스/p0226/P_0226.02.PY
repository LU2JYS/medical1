
#퀴즈>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

age=int(input("나이를 입력하세요>>>"))
height=int(input("키를 입력하세요>>>"))
if (age>=10) and (height>=150):
    print("탑승가능합니다")
else:
    print("탑승불가능합니다")
    
cal=input("수식을 입력하세요(+,/,*,-)")
n1=int(input("첫번째를 숫자를 입력하세요>>>"))
n2=int(input("두번째를 숫자를 입력하세요>>>"))
n3=int(input("세번째를 숫자를 입력하세요>>>"))
if cal =="+":
    print("{}+{}+{}={}입니다".format(n1,n2,n3,n1+n2+n3))
elif cal =="-":
    print("{}-{}-{}={}입니다".format(n1,n2,n3,n1-n2-n3))
elif cal =="*":
    print("{}*{}*{}={}입니다".format(n1,n2,n3,n1*n2*n3))    
elif cal =="/":
    print("{}/{}/{}={:.2f}입니다".format(n1,n2,n3,n1/n2/n3))    
