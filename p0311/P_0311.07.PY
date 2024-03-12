# #함수선언
# def plus(v1,v2):
#     result=0
#     result=v1+v2
#     return result

# #함수호출

# hap= plus(100,200) #변수 갯수를 맞춰서 넣어준다....>>>>>>>>>>>중요
# print(hap)
# print("프로그램종료")
# 
# # print(plus(100,200)) #다른 방법도 있다.
while True:
    def cal(v1,v2,op):
        result=0
        if op =="1":
            result= v1+v2
        elif op =="2":
            result=v1-v2
        elif op == "3": 
            result=v1*v2  
        elif op == "4": 
            result=v1/v2   
            
        return result     #무조건 리턴안에서 선언되서 활용한다 (지역변수) 

#aaa=0 #전역변수
    print("1. 더하기 2. 빼기 3. 곱하기 4. 나누기")
    a_input=input("계산하려고하는 방식을 입력하세요")
    var1=int(input("첫번째 수를 입력하세요>>"))
    var2=int(input("두번째 수를 입력하세요>>"))

    data = cal(var1,var2,a_input)

    print("결과값 : ",data) #함수내의 선언되는것은 안에서만 사용해야한다. 밖에서는 선언이 불가능하다....사용불가능

    