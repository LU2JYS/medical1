import stuUpdate

stu = [1,'홍길동',100,100,100,300,100.0,1]
s_title = ["","국어","영어","수학"]
while True:
    print("-"*40)
    print("학생데이터 : ",stu)
    print("3.학생성적수정")
    choice = int(input("원하는 번호를 입력하세요.>> "))
    if choice == 3: #학생성적수정
        print("[ 학생성적수정 ]")
        print("1. 국어   2. 영어   3. 수학")
        choice = int(input("원하는 번호를 입력하세요.>> "))
        if choice == 1:
            stuUpdate.s_update(choice,s_title,stu)
        elif choice == 2:
            stuUpdate.s_update(choice,s_title,stu)
        elif choice == 3:
            stuUpdate.s_update(choice,s_title,stu)