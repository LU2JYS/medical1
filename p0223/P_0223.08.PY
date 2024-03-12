#  점수를 입력받ㅇ아서
# 90점 이상이면 a 80점이상이면 b 70점 이상이면 
num=int(input("학생의 점수를 입력하시요"))
if num>=90:
    print("A학점입니다")
    if num>=98:
        print("A+학점입니다")
    elif num>93:
        print("A학점입니다")
    else:
        print("A-학점입니다")   
elif num>=80:
    print("B학점입니다")
    if num>=88:
        print("B+학점입니다")
    elif num>83:
        print("B학점입니다")
    else:
        print("B-학점입니다")
elif num>=70:
    print("C학점입니다")
    if num>=78:
        print("C+학점입니다")
    elif num>73:
        print("C학점입니다")
    else:
        print("C-학점입니다")

    
