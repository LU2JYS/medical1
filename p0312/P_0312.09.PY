def para_func(*num): #가변 매개변수 하나의 매개변수로 모든 값을 계산해 준다.
    # print(num)
    sum=0
    for n in num:
        sum+=n
    print("합계 : ",sum)


#함수를 1,2,3,4,5,6,7,8,9,10
#더하기 결과값을 출력하시요
para_func(1)
para_func(1,2)
para_func(1,2,3)
para_func(1,2,3,4)