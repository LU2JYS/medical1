gender=input("성별을 입력하시요>>>")
height=float(input("키를 입력하시요>>>"))
if gender=="남자":
    print("남자입니다")
    if height>= 172.5:
        print("평균이상")
    else :
        print("평균이하")
elif gender=="여자":
    print("여자입니다")
    if height>=159.6:
        print("평균이상")
    else:
        print("평균이하")
    
    
    
    