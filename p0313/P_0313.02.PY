
#함수호출 이름()
# 매개변수: 함수로 데이터전달하는 변수,매개변수 개수는 항상 같아야 한다.
# 가변매개변수 선언은 일치하지 않아도된다.
#리스트,딕셔너리 매개변수는 주소값이 전달이 된다.

#퀴즈.1
# 함수를 사용하여 두수를 입력받아, 더하기,빼기,곱하기,나누기 결과값을 출력하시요

                        #20번씩 쳐보자>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def cal(num1,num2):
        r_list= [0]*6
        r_list[0]=num1
        r_list[1]=num2
        r_list[2] =num1 + num2
        r_list[3] =num1 - num2
        r_list[4] =num1 * num2
        r_list[5] =num1 / num2
    
        return  r_list

save_list=[]
while True:         
    # 두수이력을 받아 리턴을 받아 출력
    num1=int(input("1번째 숫자를 입력하시요(0. 종료)>>>"))
    if num1==0:
        break
    num2=int(input("2번째 숫자를 입력하시요>>>"))
    # print("1.+ 2.- 3.* 4./")
    # c= input("원하는 사칙연산을 입력하세요")

    #함수호출 >>>>>>>>>cal()로 호출을 한다.
    #===========================================
    r_list=cal(num1,num2)
    save_list.append(r_list)

    print("{},{} 결과값: {},{},{},{}".format(*r_list))
    
# 현재까지 입력한 숫자와 결과값을 모두 출력하세요
print("[현재까지 입력한 숫자,결과값]")
for s in save_list:
    print("{},{} 결과값: {},{},{},{}".format(*r_list))

#10,20결과값 : 30,-10,200,0,0.5