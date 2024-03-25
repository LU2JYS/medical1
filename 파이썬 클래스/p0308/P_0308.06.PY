import random

#주택복권
#2조711
#1조740

f_num=random.randint(1,9)
last_num=random.randint(0,999999)


# lotto="1조740042"
lotto=str(f_num)+"조"+"{:06d}".format(last_num)
print(lotto)


l_input=input("복권을 입력하세요. (예 :1조111111)")
cnt=0
for i in range(len(lotto)):
    if lotto[i-1] == l_input[i-1]:
        if i ==1: continue #조는 건너뛴다
        break 
    else:
        cnt+=1 #맞는 횟수 1증가
        
if cnt == 0:
    print("완전 꽝입니다")
elif cnt ==1:
    print("6번째 자리가 맞았습니다. 당첨금액 : 1만원")
elif cnt ==2:
    print("5,6번째 자리가 맞았습니다. 당첨금액 : 10만원")
elif cnt ==3:
    print("4,5,6번째 자리가 맞았습니다. 당첨금액 : 100만원")
elif cnt ==4:
    print("3,4,5,6번째 자리가 맞았습니다. 당첨금액 : 1000만원")
elif cnt ==5:
    print("2,3,4,5,6번째 자리가 맞았습니다. 당첨금액 : 1억원")
elif cnt ==6:
    print("1,2,3,4,5,6번째 자리가 맞았습니다. 당첨금액 : 10억원")
    
        


print("맞는개수: ",cnt-1)
    






