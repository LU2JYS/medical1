# 1-25까지 숫자를 랜덤으로 섞은 다음
#2차원 리스트에 넣어보세요

#[
# [1,2,3,4,5],
# [6,7,8,9,10],
# [11,12,13,14,15],
# [16,17,18,19,20],
# [21,22,23,24,25]
#]

#랜덤으로 섞어서 출력하세요
#1-25까지 리스트를 생성하고
#랜덤으로 섞기
#2차원 리스트에 넣기
import random
save_num=[]
num=random.randint(1,100)
cnt=1 stuNo="k"+str(count)
print("정답:",num)
# 숫자맞추기 프로그램 구현
#1-10까지 숫자를 생성하여 숫자를 맞추는 게임
#몇번만에 맞추었는지 입력하세요
while True:
    in_num=int(input("1~100까지의 숫자를 넣어주세요>>>"))
    if num>in_num:
        save_num.append(in_num) #저장
        print("입력한 숫자보다 더 큽니다")
    elif num<in_num:
        print("입력한 숫자보다 더 작습니다")
    else:
        print("정답입니다.")
        print("{}번째 도전을 하였습니다.".format(cnt))
        break
    cnt+=1