#함수선언

def cal(num1,num2):
        sum=0
        return sum

    #1,10>1+2+3+....10=55
    #두수를 입력받아, 입력한 사이의 합계를 구하는 프로그램을 구현하시요
x=1
sum=0
while x<11:
        sum=sum+x
        x=x+1
        
num1 =int(input("1번째 숫자를 입력하세요"))
num2=int(input("2번째 숫자를 입력하세요"))

cal(num1,num2)

print("합계 :",sum)
    
    
    #함수선언
def cal(num1,num2):
        sum=0
        if num1>num2:
            num1,num2 =num2,
        for i in range(num1,num2+1):
            sum+=i
        return sum
    #1,10>1+2+3+....10=55
    #두수를 입력받아, 입력한 사이의 합계를 구하는 프로그램을 구현하시요
    
sum=0
num1 =int(input("1번째 숫자를 입력하세요"))
num2=int(input("2번째 숫자를 입력하세요"))

sum =cal(num1,num2)

print("합계 :",sum)