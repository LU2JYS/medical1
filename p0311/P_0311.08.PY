# def plus(v1,v2):
#     v1=v1+100
#     v2=v2+200 #지역함수이다
#     return v1,v2 #함수밖에서 사용하려면 리턴값을 돌려줘야함
# #함수호출
# v1=1
# v2=2
# v1,v2=plus(v1,v2) #위에 있는 v1,v2는 다른 변이당 변수에 담아줘야 리턴값이 먹힌다..

# #출력
# print(v1,v2)
def cal(input1,input2):
    result1=input1+input2
    result2=input1-input2
    result3=input1*input2
    result4=input1/input2

    return result1,result2,result3,result4 #데이터를 넘기는 방법이다
        
input1=int(input("첫번째 숫자를 입력하세요"))
input2=int(input("두번째 숫자를 입력하세요"))

data=cal(input1,input2) #튜플형태로 받은것!!
print("결과값:",data)

#함수의 리턴값을 사용하여 입력된 두수의 사칙연산 결과값을 출력해보시요
#20,10
#결과값 : 30,10,200,2