def count(num):
    if num>=1:
        print(num,end="  ")
        count(num-1) #함수를 다시 호출 : 재귀함수
    else:
        return
count(10)

#두가지 방법이 있다.
# for i in range(10,0,-1):
#     print(i,end=" ")