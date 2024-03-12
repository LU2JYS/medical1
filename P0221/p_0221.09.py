#두 수를 입력받아서 사칙연산을 출력해보아라
#예시 : 30 ,6을 input입력받아서
# 출력 : 
#30+6=36
#30-6=30
#30*6=180
#30/6=5.0

n1= input("첫번째 숫자를 입력하세요")
n2= input("두번째 숫자를 입력하세요")
print("두 수의 합 : ",int(n1)+int(n2)) #숫자로 계산을 하려면 int를 붙이고 계산이 들어가야함>>>>>중요
print("두 수의 빼기 : ",int(n1)-int(n2))
print("두 수의 곱 : ",int(n1)*int(n2))
print("두 수의 나누기 : ",int(n1)/int(n2))


#변수를 사용하여 출력하기
num1 =30
num2 =6
print("{}+{}={}".format(num1,num2,num1+num2))
print("{}-{}={}".format(num1,num2,num1-num2))
print("{}*{}={}".format(num1,num2,num1*num2))
print("{}/{}={}".format(num1,num2,num1/num2))


n1= (int(input("첫번째 숫자를 입력하세요"))) #숫자로 계산을 하려면 int를 앞에 감싸고  계산이 들어가야함>>>>>중요
n2= (int(input("두번째 숫자를 입력하세요")))
print("두 수의 합 : ",n1+n2) 
print("두 수의 빼기 : ",n1-n2)
print("두 수의 곱 : ",n1*n2)
print("두 수의 나누기 : ",n1/n2)