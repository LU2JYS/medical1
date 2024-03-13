# #두수를 입력받아 두수 사이의 합계를 구하시요



# #함수선언
# def cal(s_list):
#                     #지역변수//위아래 썸은 다른썸이다...
#     for i in range(s_list[0],s_list[1]+1):
#         s_list[2] +=i
#     # return sum

# sum=0
# num1=int(input("1번째 숫자를 입력하세요"))
# num2=int(input("2번째 숫자를 입력하세요"))
# s_list=[num1,num2,sum]
# cal(s_list) #전역변수 //위아래 썸은 다른썸이다...
# print("s_list :",s_list)
        
        
print("-"*45)

#1,10 1-10까지의 더하기 빼기 곱하기 결과값을 출력하시요
#파이썬 언어는 인터프리터 언어, 컴파일러 언어

def cal(s_list):
                    #지역변수//위아래 썸은 다른썸이다...
    #더하기
    for i in range(s_list[0],s_list[1]+1):
        s_list[2] +=i
    #빼기
        s_list[3] -=i
    #곱하기    
        s_list[4] *=i


num1=int(input("1번째 숫자를 입력하세요"))
num2=int(input("2번째 숫자를 입력하세요"))
s_list=[num1,num2,0,0,1]
cal(s_list) #전역변수 //위아래 썸은 다른썸이다...
print("더하기 결과값 :",s_list[2])
print("빼기 결과값 :",s_list[3])
print("곱하기 결과값 :",s_list[4])
