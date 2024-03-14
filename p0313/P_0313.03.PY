#랜덤으로 숫자 1개 생성 1-100
#입력한 숫자보다 크면 작은수를 입력하세요
#입력한 숫자보다 작으면 큰수를 입력하세요.라고 나오게
#정답을 맞추면


# 현재까지 입력했던 숫자를 모두 출력하시요.

import random

ran_num=random.randint(1,100)
in_num=0
cnt=0
s_list=[]
while True:
    print("[랜덤숫자 맞추기 게임]")
    in_num=int(input(f"{cnt}번째 도전. 1-100까지의 숫자를 입력하세요>>>>"))
    s_list.append(in_num)
    if ran_num > in_num:
        print("다시 큰수를 입력하세요")
    elif ran_num < in_num:
        print("다시 작은수를 입력하세요")
    else:
        print("정답입니다.")
        break
    cnt+=1
    
#--------------------종료후


print("총 입력한 횟수 : {}회".format(cnt))
print("현재까지 입력한 숫자: : {}".format(s_list))
#총 입력한 횟수 : 7회
# 현재까지 입력한 숫자: 1,5,7,4,8,4,50

    

